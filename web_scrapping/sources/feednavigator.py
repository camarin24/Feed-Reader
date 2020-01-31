from web_scrapping import WebScrappingBase
from bs4 import BeautifulSoup
from selenium import webdriver
from web_scrapping import New


class FeedNavigatorScrapper(WebScrappingBase):
    def __init__(self, path, feed):
        super(FeedNavigatorScrapper, self).__init__(path, feed)

    def parse(self, driver):
        results = []
        article_body = driver.find_element_by_class_name("ezxmltext-field")
        ps = article_body.find_elements_by_tag_name("p")
        for c in ps:
            results.append(c.text)
        return New(
            new=self.remove_xml(" ".join(results).encode(
                'ascii', errors='ignore')),
            feed=self.feed
        )
