import pyodbc


class Sql:
    def __init__(self):
        self.cnx = pyodbc.connect(r'DRIVER={ODBC Driver 17 for SQL Server};'
                                  r'SERVER=52.14.100.49;DATABASE=Premex_NousProd;'
                                  r'UID=cmarin;PWD=Cambiar.100')
        self.news = None

    def __get_as_dict(self, query):
        cursor = self.cnx.cursor().execute(query)
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        return results

    def __validate_title(self, title):
        if self.news is None:
            self.news = [t['Title']
                         for t in self.__get_as_dict("SELECT Title FROM [Ai].[New]")]
            print(self.news)
        print(title in self.news)
        return title not in self.news

    def __parse_news(self, news):
        results = []
        for n in news:
            if self.__validate_title(str(n.feed.title)):
                feed = n.feed
                results.append((str(feed.title),
                                str(feed.summary),
                                str(n.new),
                                str(feed.date),
                                ','.join(feed.tags).replace("b'", ""),
                                str(','.join(feed.classifier_tags)),
                                str(feed.url),
                                str(feed.source)))

        return results

    def insert(self, news):
        query = "INSERT INTO [Ai].[New] ([Title],[Summary],[Text],[Date],[SourceTags],[Tags],[Url],[Source]) VALUES(?,?,?,?,?,?,?,?)"
        rows = self.__parse_news(news)
        print(f'News inserted {len(rows)}')
        if len(rows) > 0:
            print(rows)
            cursor = self.cnx.cursor()
            cursor.executemany(query, rows)
            cursor.commit()
            self.cnx.close()
