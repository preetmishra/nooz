import urwid


class AboutTextWidget(urwid.WidgetWrap):
    '''
    Information about the app.
    '''
    def __init__(self) -> None:
        desc = 'nooz: Trending headlines right in your terminal.'
        self._w = urwid.Text(desc)
