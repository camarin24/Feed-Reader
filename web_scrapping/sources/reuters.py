from web_scrapping import WebScrappingBase
from bs4 import BeautifulSoup
from selenium import webdriver
from web_scrapping import New


class ReutersScrapper(WebScrappingBase):
    def __init__(self, path, feed):
        super(ReutersScrapper, self).__init__(path, feed)

    def parse(self, driver):
        results = []
        article_body = driver.find_element_by_class_name(
            "StandardArticleBody_body")
        childs = article_body.find_elements_by_tag_name('p')
        for c in childs:
            results.append(c.text)
        return New(
            new=self.remove_xml(" ".join(results).encode(
                'ascii', errors='ignore')),
            feed=self.feed
        )
