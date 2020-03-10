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
