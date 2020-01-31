from bs4 import BeautifulSoup
from .feed import Feed
import feedparser
import json
import time
import ssl
import re
import os
from sql import Sql


class RssBase(object):
    def __init__(self, path, source_urls, source):
        """[summary]

        Arguments:
            source_urls {[array]} -- [Feed urls for the source]
        """
        self.source_urls = source_urls
        self.source = source

        with open(f'{path}/abbreviations.json') as file:
            self.abbreviations = json.load(file)

        self.tags = Sql().getTags()

    def parse(self, item):
        """[summary]

        Arguments:
            item {[object]} -- Feed element from original source

        Return:
            A Feed object
        """
        return Feed(
            title=item['title'].encode(
                'ascii', errors='ignore'),
            summary=item['summary'].encode(
                'ascii', errors='ignore') if 'summary' in item.keys() else None,
            source=self.source,
            date=time.strftime(
                '%Y-%m-%d', item['published_parsed']) if 'published_parsed' in item.keys() else None,
            url=item['link'],
            tags=[i['term']
                  for i in item['tags']] if 'tags' in item.keys() else []
        )

    def get_feeds(self, url):
        """[summary]

        Arguments:
            url {[string]} -- [section or tag feed url]

        Returns:
            [array] -- [list of feedparser objects]
        """

        try:
            if hasattr(ssl, '_create_unverified_context'):
                ssl._create_default_https_context = ssl._create_unverified_context
            return feedparser.parse(url)['items']
        except NameError:
            print(NameError)
            return []

    def remove_xml(self, text):
        if text is not None:
            return BeautifulSoup(text, "lxml").text
        return ''

    def replace_abbreviations(self, text):
        return ' '.join([self.abbreviations[t] if t in self.abbreviations else t for t in text.split(" ")])

    def clean_text(self, feeds):
        for f in feeds:
            f.title = self.replace_abbreviations(
                self.remove_xml(f.title).lower())
            f.summary = self.replace_abbreviations(
                self.remove_xml(f.summary).lower())
        return feeds

    def findWholeWord(self, w):
        return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

    def classifier(self, feeds):
        """[summary]

        Arguments:
            feeds {[array]} -- [All the news returned by every feed]
        """
        results = []
        for f in feeds:
            for t in self.tags:
                if self.findWholeWord(t)(f.summary if f.summary is not None else f.title) is not None:
                    f.classifier_tags.append(t)
                    results.append(f)
                    break
        return results

    def run(self):
        result = []
        for url in self.source_urls:
            u_feeds = self.get_feeds(url)
            feeds = [self.parse(f) for f in u_feeds]
            feeds = self.clean_text(feeds)
            feeds = self.classifier(feeds)
            result.extend(feeds)
        return result
