from web_scrapping.sources import NyTimesScrapper, ReutersScrapper, CnnScrapper
from rss import RssBase
from sql import Sql
import json


class Orchestrator:
    def __init__(self):
        pass

    def __load_sources(self):
        response = None
        with open('sources.json') as file:
            response = json.load(file)
        return response

    def __get_web_driver(self, key, feed):
        if key == "RTS":
            return ReutersScrapper(feed)
        elif key == "NYT":
            return NyTimesScrapper(feed)
        elif key == "CNN":
            return CnnScrapper(feed)

    def __run(self, resource):
        print(f"Getting results for {resource['source']}")
        results = []
        feeds = RssBase(resource['urls'], resource['name']).run()
        for f in feeds:
            driver = self.__get_web_driver(resource['source'], f)
            try:
                results.append(driver.run())
            except NameError:
                print("Error on load the web content")
                print(NameError)

        return results

    def run(self):
        news = []
        resources = self.__load_sources()
        for r in resources:
            news.extend(self.__run(r))
        Sql().insert(news)
