from typing import Optional


def fix_null(response: Optional[str]) -> str:
    '''
    If the response is Null from the server, returns an empty string otherwise
    returns the response.
    '''

    return response if response else ''
