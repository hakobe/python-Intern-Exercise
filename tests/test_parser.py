import unittest

from parser import Parser
from log import Log

class ParserTest(unittest.TestCase):
    def test_parse(self):
        parser = Parser(filename = 'sample_data/log.ltsv')
        logs = parser.parse()
        self.assertEqual(logs[0],
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
        self.assertEqual(logs[1],
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
        self.assertEqual(logs[2],
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
