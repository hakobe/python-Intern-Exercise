import re

class Log:
    def __init__(self, host, user, epoch, req, status, size, referer):
        self.host = host
        self.user = user
        self.epoch = epoch
        self.req = req
        self.status = status
        self.size = size
        self.referer = referer

        (self.method, self.path, self.protocol, *_) = self.req.split()

    def __eq__(self, other):
        return (
            self.host == other.host and
            self.user == other.user and
            self.epoch == other.epoch and
            self.req == other.req and
            self.status == other.status and
            self.size == other.size and
            self.referer == other.referer
        )

    @property
    def uri(self):
        return "http://{}{}".format(self.host, self.path)

    def is_error(self):
        return bool(re.match(r'^5\d\d', self.status))
