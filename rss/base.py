from .feed import Feed
import feedparser


class RssBase(object):
    def __init__(self, source_urls):
        """[summary]

        Arguments:
            source_urls {[array]} -- [Feed urls for the source]
        """
        self.source_urls = source_urls

    def parse(self, item):
        """[summary]

        Arguments:
            item {[object]} -- Feed element from original source

        Return:
            A Feed object
        """
        return Feed(
            title=item['title'],
            summary=item['summary'],
            date=item['published_parsed'],
            url=item['link'],
            tags=[i['term'] for i in item['tags']]
        )

    def get_feeds(self, url):
        """[summary]

        Arguments:
            url {[string]} -- [section or tag feed url]

        Returns:
            [array] -- [list of feedparser objects]
        """

        try:
            return feedparser.parse(url)['items']
        except:
            return []

    def headline_classifier(self, feeds):
        """[summary]

        Arguments:
            feeds {[array]} -- [All the news returned by every feed]
        """
        return [f for f in feeds]

    def run(self):
        result = []
        for url in self.source_urls:
            feeds = [self.parse(f) for f in self.get_feeds(url)]
            result.extend(self.headline_classifier(feeds))

        return result
