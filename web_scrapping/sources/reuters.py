from web_scrapping import WebScrappingBase
from bs4 import BeautifulSoup
from selenium import webdriver
from web_scrapping import New


class ReutersScrapper(WebScrappingBase):
    def __init__(self, feed):
        super(ReutersScrapper, self).__init__(feed)

    def parse(self, driver):
        results = []
        article_body = driver.find_element_by_class_name(
            "StandardArticleBody_body")
        childs = article_body.find_elements_by_tag_name('p')
        for c in childs:
            results.append(c.text)
        return New(
            new=" ".join(results),
            feed=self.feed
        )
