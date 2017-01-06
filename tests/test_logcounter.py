import unittest

from parser import Parser
from log import Log
from logcounter import LogCounter

class LogCounterTest(unittest.TestCase):
    def test_count_error(self):
        parser = Parser(filename = 'sample_data/log.ltsv')
        logs = parser.parse()
        logcounter = LogCounter(logs)

        self.assertEqual(logcounter.count_error(), 2)
