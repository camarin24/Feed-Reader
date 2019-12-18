# TODO: Check RSS pages
# NyTimes : https://archive.nytimes.com/www.nytimes.com/services/xml/rss/index.html
# Reuters : https://www.reuters.com/tools/rss
# BBC     : https://www.bbc.com/mundo/institucional/2011/03/000000_rss_gel
# https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f
from web_scrapping.sources import ReutersScrapper,NyTimesScrapper
from orchestrator import Orchestrator

orc = Orchestrator()
orc.run()
