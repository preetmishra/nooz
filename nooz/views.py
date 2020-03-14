import urwid

from nooz.boxes import NewsBoxes
from nooz.helper import CATEGORIES, COUNTRIES, draw_box
from nooz.widgets import AboutTextWidget, CategorySearchWidget, KeywordSearchWidget


# FIXME: Add missing type annotations.
class MainView(urwid.WidgetWrap):
    '''
    The main view for the app.
    It divides the view into two (left column view and right column view)
    using urwid's Columns.
    '''

    COLUMNS = {'left': 0, 'right': 1}
    LEFT_COLUMN_SIZE = AboutTextWidget.WIDGET_SIZE \
        + CategorySearchWidget.WIDGET_SIZE \
        + KeywordSearchWidget.WIDGET_SIZE
    RIGHT_COLUMN_SIZE = 34  # Self-imposed restriction.

    def __init__(self):
        lcv = self.left_column_view()
        rcv = self.right_column_view()

        lcv = ('weight', 1, draw_box(lcv, 'everywhere'))
        rcv = ('weight', 4, draw_box(rcv, 'everywhere', title='Articles'))

        columns = urwid.Columns([lcv, rcv], dividechars=1, focus_column=1)
        self.body = urwid.Filler(columns, valign='middle')
        frame = urwid.Frame(body=self.body, footer=self.foot())
        self._w = urwid.Padding(frame, left=2, right=2)

    def foot(self):
        footer_text = [
            ('Keys'), '    ',
            ('UP'), ', ', ('DOWN'), ', ',
            ('PAGE UP'), ' and ', ('PAGE DOWN'),
            (' scroll    '),
            ('F5'), ' refreshes    ',
            ('q, Q'), ' exits',
        ]
        return urwid.Pile([urwid.Text((footer_text)), urwid.Divider()])

    def left_column_view(self):
        abw = AboutTextWidget()
        ksw = KeywordSearchWidget(self)
        csw = CategorySearchWidget(self)
        widgets = [draw_box(abw, 'bottom'), draw_box(ksw, 'bottom'), csw]
        return urwid.Pile(widgets)

    def right_column_view(self, keyword: str = '', category: str = '',
                          country: str = ''):
        articles = NewsBoxes(keyword, category, country)
        if not articles:
            error_text = "Bummer! Couldn't find anything. Press F5 to refresh."
            articles = [urwid.Text(error_text)]  # type: ignore
        content = urwid.ListBox(urwid.SimpleListWalker(articles))
        widgets = [urwid.BoxAdapter(content, self.RIGHT_COLUMN_SIZE)]
        return urwid.Pile(widgets)

    def set_main_focus(self, column: str) -> None:
        self._w.original_widget.body.body.set_focus_column(
            self.COLUMNS[column]
        )

    def update_right_column_view(self, keyword: str = '', category: str = '',
                                 country: str = '') -> None:
        news_boxes = self.right_column_view(keyword, category, country)
        self._w.original_widget.body.body.contents[self.COLUMNS['right']] = (
            draw_box(news_boxes, 'everywhere', title='Articles'),
            self.body.body.options('weight', 4)
        )

    def keypress(self, size, key: str):
        if key == 'f5':
            # Refresh: Fetch news again.
            self.update_right_column_view()
        return super().keypress(size, key)
