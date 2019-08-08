from .feed import Feed
import feedparser
import ssl


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
            title=item['title'].encode("utf8"),
            summary=item['summary'].encode("utf8"),
            date=item['published_parsed'],
            url=item['link'],
            tags=[i['term'].encode("utf8") for i in item['tags']]
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

    def headline_classifier(self, feeds):
        """[summary]

        Arguments:
            feeds {[array]} -- [All the news returned by every feed]
        """
        return [f for f in feeds]

    def run(self):
        result = []
        for url in self.source_urls:
            u_feeds = self.get_feeds(url)
            print(len(u_feeds))
            feeds = [self.parse(f) for f in u_feeds]
            result.extend(self.headline_classifier(feeds))

        return result
