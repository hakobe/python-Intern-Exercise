import unittest
from log import Log

class LogTest(unittest.TestCase):
    def test_init(self):
        log = Log(
            host    = '127.0.0.1',
            user    = 'frank',
            epoch   = '1372694390',
            req     = 'GET /apache_pb.gif HTTP/1.1',
            status  = '200',
            size    = '2326',
            referer = 'http://www.hatena.ne.jp/',
        )
        self.assertEqual(log.method, 'GET')
        self.assertEqual(log.path, '/apache_pb.gif')
        self.assertEqual(log.protocol, 'HTTP/1.1')
        self.assertEqual(log.uri, 'http://127.0.0.1/apache_pb.gif')

    def test_eq(self):
        log = Log(
            host    = '127.0.0.1',
            user    = 'frank',
            epoch   = '1372694390',
            req     = 'GET /apache_pb.gif HTTP/1.1',
            status  = '200',
            size    = '2326',
            referer = 'http://www.hatena.ne.jp/',
        )
        same_log = Log(
            host    = '127.0.0.1',
            user    = 'frank',
            epoch   = '1372694390',
            req     = 'GET /apache_pb.gif HTTP/1.1',
            status  = '200',
            size    = '2326',
            referer = 'http://www.hatena.ne.jp/',
        )
        other_log = Log(
            host    = '127.0.0.1',
            user    = 'frank',
            epoch   = '1372694390',
            req     = 'GET /apache_pb.gif HTTP/1.1',
            status  = '200',
            size    = '2326',
            referer = 'http://www.hatena.ne.jp/?hoge=1',
        )

        self.assertEqual(log, same_log)
        self.assertNotEqual(log, other_log)
