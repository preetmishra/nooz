import urwid
from typing import Optional


CATEGORIES = [
    'business',
    'entertainment',
    'general',
    'health',
    'science',
    'sports',
    'technology',
]

COUNTRIES = {
    'argentina': 'ar',
    'australia': 'au',
    'belgium': 'be',
    'brazil': 'br',
    'bulgaria': 'bg',
    'canada': 'ca',
    'austria': 'at',
    'china': 'cn',
    'colombia': 'co',
    'cuba': 'cu',
    'czech republic': 'cz',
    'egypt': 'eg',
    'france': 'fr',
    'germany': 'de',
    'greece': 'gr',
    'hong kong': 'hk',
    'hungary': 'hu',
    'india': 'in',
    'indonesia': 'id',
    'ireland': 'ie',
    'israel': 'il',
    'italy': 'it',
    'japan': 'jp',
    'latvia': 'lv',
    'lithuania': 'lt',
    'malaysia': 'my',
    'mexico': 'mx',
    'morocco': 'ma',
    'netherlands': 'nl',
    'new zealand': 'nz',
    'nigeria': 'ng',
    'norway': 'no',
    'philippines': 'ph',
    'poland': 'pl',
    'portugal': 'pt',
    'romania': 'ro',
    'russia': 'ru',
    'saudi arabia': 'sa',
    'serbia': 'rs',
    'singapore': 'sg',
    'slovakia': 'sk',
    'slovenia': 'si',
    'south africa': 'za',
    'south korea': 'kr',
    'sweden': 'se',
    'switzerland': 'ch',
    'taiwan': 'tw',
    'thailand': 'th',
    'turkey': 'tr',
    'uae': 'ae',
    'ukraine': 'ua',
    'united kingdom': 'gb',
    'united states': 'us',
    'venuzuela': 've',
}


def fix_null(response: Optional[str]) -> str:
    '''
    If the response is Null from the server, returns an empty string otherwise
    returns the response.
    '''

    return response if response else ''


# FIXME: Add missing type annotations.
def draw_box(widget, where: str, title: str = '', title_align: str = 'center',
             title_attr=None):
    '''
    Wrapper function for urwid.LineBox() to reduce the number of parameters
    needed for each function call.
    '''
    if where == 'everywhere':
        return urwid.LineBox(widget, title, title_align, title_attr,
                             tlcorner='┌', tline='─', lline='│', trcorner='┐',
                             blcorner='└', rline='│', bline='─', brcorner='┘')
    elif where == 'top':
        return urwid.LineBox(widget, title, title_align, title_attr,
                             tlcorner='─', tline='─', lline='', trcorner='─',
                             blcorner='', rline='', bline='', brcorner='')
    elif where == 'bottom':
        return urwid.LineBox(widget, title, title_align, title_attr,
                             tlcorner='', tline='', lline='', trcorner='',
                             blcorner='─', rline='', bline='─', brcorner='─')
    elif where == 'left':
        return urwid.LineBox(widget, title, title_align, title_attr,
                             tlcorner='', tline='', lline='│', trcorner='',
                             blcorner='', rline='', bline='', brcorner='')
    elif where == 'right':
        return urwid.LineBox(widget, title, title_align, title_attr,
                             tlcorner='', tline='', lline='', trcorner='',
                             blcorner='', rline='│', bline='', brcorner='')
