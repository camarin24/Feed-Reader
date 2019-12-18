class Feed(object):
    def __init__(self, title, summary, date, url, source,image_url=None, tags=[]):
        self.title = title
        self.summary = summary
        self.date = date
        self.url = url
        self.image = image_url
        self.tags = tags
        self.classifier_tags = []
        self.source = source

    def to_dict(self):
        return self.__dict__

    def set_summary(self, summary):
        self.summary = summary
