from web_scrapping import WebScrappingBase
from bs4 import BeautifulSoup
from selenium import webdriver
from web_scrapping import New


class NyTimesScrapper(WebScrappingBase):
    def __init__(self, feed):
        super(NyTimesScrapper, self).__init__(feed)

    def parse(self, driver):
        results = []
        story_body = driver.find_elements_by_class_name(
            "StoryBodyCompanionColumn")

        for sb in story_body:
            div = sb.find_elements_by_tag_name('div')
            for d in div:
                ps = d.find_elements_by_tag_name('p')
                for p in ps:
                    results.append(p.text)

        return New(
            new=" ".join(results).encode("utf8"),
            feed=self.feed
        )
