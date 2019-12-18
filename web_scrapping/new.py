class New(object):
    def __init__(self, new, feed=None):
        self.feed = feed
        self.new = new

    def to_dict(self):
        return self.__dict__
