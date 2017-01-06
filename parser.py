from log import Log

class Parser:
    def __init__(self, filename):
        self.filename = filename

    @classmethod
    def _make_pair(cls, label_value):
        label, value = label_value.split(':', 1)
        if value == '-':
            value = None
        return (label, value)

    @classmethod
    def _parse_line(cls, line):
        parsed = dict([ cls._make_pair(label_value) for label_value in line.split("\t") ])
        return Log(**parsed)

    def parse(self):
        with open(self.filename) as logfile:
            return [ Parser._parse_line(line) for line in logfile.read().splitlines() ]
