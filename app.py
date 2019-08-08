# TODO: Check RSS pages
# NyTimes : https://archive.nytimes.com/www.nytimes.com/services/xml/rss/index.html
# Reuters : https://www.reuters.com/tools/rss
# BBC     : https://www.bbc.com/mundo/institucional/2011/03/000000_rss_gel
# https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f
import json
from rss import RssBase
from web_scrapping.sources import ReutersScrapper,NyTimesScrapper

result = RssBase(['https://rss.nytimes.com/services/xml/rss/nyt/Health.xml']).run()
print(f"Total resultados para el tag healthNews {len(result)}")
for r in result:
    print(f'------------------------{r.url}-----------------------')
    web = NyTimesScrapper(r).run()
    print(web.to_dict())
