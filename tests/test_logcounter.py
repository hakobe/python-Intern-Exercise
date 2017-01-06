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

    def test_group_by_user(self):
        parser = Parser(filename = 'sample_data/log.ltsv')
        logs = parser.parse()
        logcounter = LogCounter(logs)

        logs_by_user = logcounter.group_by_user()

        self.assertEqual( len( logs_by_user['john'] ), 1)
        self.assertEqual(
            logs_by_user['john'][0],
            Log(
                host = '127.0.0.1',
                user = 'john',
                epoch = '1372794390',
                req = 'GET /apache_pb.gif HTTP/1.0',
                status = '200',
                size = '1234',
                referer = 'http://b.hatena.ne.jp/hotentry',
            )
        )
        self.assertEqual( len( logs_by_user['frank'] ), 3)
        self.assertEqual(
            logs_by_user['frank'][0],
            Log(
                host = '127.0.0.1',
                user = 'frank',
                epoch = '1372694390',
                req = 'GET /apache_pb.gif HTTP/1.0',
                status = '200',
                size = '2326',
                referer = 'http://www.hatena.ne.jp/',
            )
        )
        self.assertEqual( len( logs_by_user['guest'] ), 1)
        self.assertEqual(
            logs_by_user['guest'][0],
            Log(
                host = '127.0.0.1',
                user = None,
                epoch = '1372894390',
                req = 'GET /apache_pb.gif HTTP/1.0',
                status = '503',
                size = '9999',
                referer = 'http://www.example.com/start.html',
            )
        )
