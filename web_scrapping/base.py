from abc import ABCMeta, abstractmethod
from selenium import webdriver
import requests


class WebScrappingBase(metaclass=ABCMeta):
    def __init__(self, feed):
        self.feed = feed

    @abstractmethod
    def parse(self, driver):
        pass

    def compile(self, url):
        driver = webdriver.Firefox(executable_path='C:/geckodriver.exe')
        driver.get(url)
        driver.find_element_by_class_name
        results = self.parse(driver)
        driver.quit()
        return results

    def run(self):
        return self.compile(self.feed.url)