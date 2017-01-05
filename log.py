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

    @property
    def uri(self):
        return "http://{}{}".format(self.host, self.path)
