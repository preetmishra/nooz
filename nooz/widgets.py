from typing import Any
import urwid

from helper import CATEGORIES, COUNTRIES


class AboutTextWidget(urwid.WidgetWrap):
    '''
    Information about the app.
    '''

    WIDGET_SIZE = 2

    def __init__(self) -> None:
        desc = 'nooz: Trending headlines right in your terminal.'
        self._w = urwid.Text(desc)


# FIXME: Add missing type annotations.
class SearchWidget(urwid.WidgetWrap):
    '''
    Base class for search widgets.
    '''

    def __init__(self, controller: Any, search_text: str, body,
                 widget_size: int) -> None:
        self.controller = controller
        self.search_text = search_text
        self.search = urwid.Edit(self.search_text)
        self.body = body
        frame = urwid.Frame(body=self.body, header=self.search,
                            focus_part='header')
        self._w = urwid.BoxAdapter(frame, widget_size)

    def keypress(self, size, key: str):
        if key == 'enter' or key == 'esc':
            self.search.set_edit_text('')
            self.controller.set_main_focus('right')
        return super().keypress(size, key)


# FIXME: Add missing type annotations.
class KeywordSearchWidget(SearchWidget):
    '''
    This widget is a part of the left column view.
    It provides an interface for searching news using any keyword.
    '''

    WIDGET_SIZE = 4

    def __init__(self, controller: Any) -> None:
        body = urwid.Filler(
            urwid.Text('Examples: apple, hollywood, trump, etc.'),
            valign='bottom'
        )
        super().__init__(controller, 'Search by keyword: ', body,
                         self.WIDGET_SIZE)

    def keypress(self, size, key: str):
        if key == 'enter':
            keyword = self.search.get_edit_text().lower()
            self.controller.update_right_column_view(keyword=keyword)
        return super().keypress(size, key)


# FIXME: Add missing type annotations.
class CategorySearchWidget(SearchWidget):
    '''
    This widget is a part of the left column view.
    It provides an interface for searching news by a category.
    '''

    WIDGET_SIZE = len(CATEGORIES) + 2

    def __init__(self, controller: Any) -> None:
        categories = urwid.Pile([
            urwid.Text('* ' + category[0].upper() + category[1:])
            for category in CATEGORIES
        ])
        body = urwid.Filler(categories, valign='bottom')
        super().__init__(controller, 'Search by category: ', body,
                         self.WIDGET_SIZE)

    def keypress(self, size, key: str):
        if key == 'enter':
            category = self.search.get_edit_text().lower()
            self.controller.update_right_column_view(category=category)
        return super().keypress(size, key)
