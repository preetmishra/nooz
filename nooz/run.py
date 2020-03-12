import urwid

from views import MainView


class App:
    '''
    Class for running the app.
    '''
    def __init__(self) -> None:
        self.main_view = MainView()

    def exit(self, key: str) -> None:
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()


def main() -> None:
    app = App()
    loop = urwid.MainLoop(app.main_view, unhandled_input=app.exit)
    loop.run()


if __name__ == '__main__':
    main()
