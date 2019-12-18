from abc import ABCMeta, abstractmethod
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os


class WebScrappingBase(metaclass=ABCMeta):
    def __init__(self, feed):
        self.feed = feed

    @abstractmethod
    def parse(self, driver):
        pass

    def remove_xml(self, text):
        return BeautifulSoup(text, "lxml").text

    def compile(self, url):
        driver = webdriver.Firefox(
            executable_path=os.getcwd() + '/drivers/geckodriver')
        driver.get(url)
        driver.find_element_by_class_name
        results = self.parse(driver)
        driver.quit()
        return results

    def run(self):
        return self.compile(self.feed.url)
