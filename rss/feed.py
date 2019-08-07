class Feed(object):
    def __init__(self, title, summary, date, url, image_url=None, tags=[]):
        self.title = title
        self.summary = summary
        self.date = date
        self.url = url
        self.image = image_url
        self.tags = tags

    def to_dict(self):
        return self.__dict__
