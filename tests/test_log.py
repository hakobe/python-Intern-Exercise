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

    def test_is_error(self):
        success_log = Log(
            host    = '127.0.0.1',
            user    = 'frank',
            epoch   = '1372694390',
            req     = 'GET /apache_pb.gif HTTP/1.1',
            status  = '200',
            size    = '2326',
            referer = 'http://www.hatena.ne.jp/',
        )
        error_log_404 = Log(
            host    = '127.0.0.1',
            user    = 'frank',
            epoch   = '1372694390',
            req     = 'GET /apache_pb.gif HTTP/1.1',
            status  = '404',
            size    = '2326',
            referer = 'http://www.hatena.ne.jp/?hoge=1',
        )
        error_log_503 = Log(
            host    = '127.0.0.1',
            user    = 'frank',
            epoch   = '1372694390',
            req     = 'GET /apache_pb.gif HTTP/1.1',
            status  = '503',
            size    = '2326',
            referer = 'http://www.hatena.ne.jp/?hoge=1',
        )

        self.assertFalse( success_log.is_error() )
        self.assertFalse( error_log_404.is_error() )
        self.assertTrue( error_log_503.is_error() )
