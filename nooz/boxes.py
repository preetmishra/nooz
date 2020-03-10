from typing import Dict
import urwid

from helper import draw_box
from model import fetch_news


# FIXME: Add missing type annotations.
class NewsBoxes:
    def __new__(cls, keyword: str = '', category: str = '',
                country: str = ''):
        inst = super().__new__(cls)
        return inst.news_boxes(keyword, category, country)

    def build_news_box(self, article: Dict[str, str]):
        '''
        Builds and returns a news box.
        The news box is a LineBox and its content is a Pile of things to
        display from the article.

        Expected structure of the article:
        article: {
            author:
            content:
            gist:
            publish_date:
            source:
            title:
            url:
        }
        '''

        # Title.
        head = urwid.Text(article['title'])

        # Content.
        body = article['gist'] if article['gist'] else article['content']
        body = urwid.Text(body if body.endswith('.') else body + '...')

        # URL.
        foot = urwid.Text('Read more: ' + article['url'])

        news_box_contents = [
            head,
            urwid.Divider(),
            body,
            urwid.Divider(),
            foot,
        ]

        pile = urwid.Pile(news_box_contents)
        news_box = draw_box(pile, 'everywhere')
        return news_box

    def news_boxes(self, keyword: str = '', category: str = '',
                   country: str = ''):
        '''
        Returns a list whose each element is a news box.
        '''
        country = country if country else 'us'
        articles = fetch_news(keyword, category, country)
        news = [self.build_news_box(article) for article in articles]
        return news
