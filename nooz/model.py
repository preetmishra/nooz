import requests
from typing import Dict, List, Union

from nooz.helper import fix_null


def fetch_news(keyword: str = '', category: str = '',
               country: str = 'us') -> List[Dict[str, str]]:
    '''
    Fetches news from newsapi.org.
    Returns either a list of articles or an empty list.

    Structure of the JSON response received:
    {
        status:
        totalResults:
        articles: [
            [
                source:{
                    id:
                    name:
                },
                author:
                title:
                description:
                url:
                urlToImage:
                publishedAt:
                content:
            ],
        ]
    }
    '''

    API_KEY = '098b7f702dcd4e9cadfe30f7f1400331'
    TOP_HEADLINES_URL = 'http://newsapi.org/v2/top-headlines'

    params: Dict[str, Union[int, str]] = {
        'apiKey': API_KEY,
        'country': country,
        'category': category,
        'q': keyword,
        'pageSize': 100,
    }

    try:
        json = requests.get(TOP_HEADLINES_URL, params=params).json()
    except Exception as e:
        return []

    if json['status'] == 'ok':
        articles = []
        for entry in json['articles']:
            article = {}

            article['author'] = fix_null(entry['author'])
            article['content'] = fix_null(entry['content'])
            article['gist'] = fix_null(entry['description'])
            article['publish_date'] = fix_null(entry['publishedAt'])
            article['source'] = fix_null(entry['source']['name'])
            article['title'] = fix_null(entry['title'])
            article['url'] = fix_null(entry['url'])

            articles.append(article)
        return articles
    else:
        # TODO: Add better exception handling.
        return []
