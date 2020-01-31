from selenium.webdriver.firefox.options import Options
from abc import ABCMeta, abstractmethod
from selenium import webdriver
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os


class WebScrappingBase(metaclass=ABCMeta):
    def __init__(self, path, feed):
        self.feed = feed
        self.path = path

    @abstractmethod
    def parse(self, driver):
        pass

    def remove_xml(self, text):
        return BeautifulSoup(text, "lxml").text

    def compile(self, url):
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(
            executable_path=f'{self.path}/drivers/geckodriver', options=options)
        driver.get(url)
        results = self.parse(driver)
        driver.quit()
        return results

    def run(self):
        return self.compile(self.feed.url)
