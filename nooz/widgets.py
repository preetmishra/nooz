import urwid


class AboutTextWidget(urwid.WidgetWrap):
    '''
    Information about the app.
    '''

    WIDGET_SIZE = 2

    def __init__(self) -> None:
        desc = 'nooz: Trending headlines right in your terminal.'
        self._w = urwid.Text(desc)
