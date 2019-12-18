from web_scrapping import WebScrappingBase
from bs4 import BeautifulSoup
from selenium import webdriver
from web_scrapping import New


class CnnScrapper(WebScrappingBase):
    def __init__(self, feed):
        super(CnnScrapper, self).__init__(feed)

    def parse(self, driver):
        results = []
        article_body = driver.find_elements_by_class_name("zn-body__paragraph")
        for c in article_body:
            results.append(c.text)
        return New(
            new=self.remove_xml(" ".join(results).encode(
                'ascii', errors='ignore')),
            feed=self.feed
        )
