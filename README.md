# nooz

Trending headlines right in your terminal.

[![PyPI](https://img.shields.io/pypi/v/nooz.svg)](https://pypi.python.org/pypi/nooz)
[![Python Versions](https://img.shields.io/pypi/pyversions/nooz.svg)](https://pypi.python.org/pypi/nooz)


## Installation

You can install nooz by typing the following in your terminal.
```bash
$ pip install nooz
```

However, if you want to install nooz in a virtual environment you can do the following things in order.
```bash
$ virtualenv ~/.virtualenvs/nooz --python=python3
$ source ~/.virtualenvs/nooz/bin/activate
(nooz) $ pip install nooz
```


## Launching
To launch the app, type the following in your terminal.
```
$ nooz
```

## Keys

| Command                                               | Key                                           |
| ----------------------------------------------------- | --------------------------------------------- |
| Go left                                               | <kbd>left</kbd>                               |
| Go right                                              | <kbd>right</kbd>                              |
| Scroll up                                             | <kbd>up</kbd> / <kbd>page up</kbd>            |
| Scroll down                                           | <kbd>down</kbd> / <kbd>page down</kbd>        |
| Exit                                                  | <kbd>q</kbd> / <kbd>Q</kbd>                   |
| Refresh                                               | <kbd>F5</kbd>                                 |
| Go back                                               | <kbd>esc</kbd>                                |


## Troubleshooting

### Locale error
You can fix locale errors by adding the following in your `~/.bashrc`.
```bash
export LANG=en_US.utf-8
```


## Screenshot

![Screenshot](https://i.imgur.com/lSu2WJC.jpg)
