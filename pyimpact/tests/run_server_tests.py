import time
import unittest
import urllib2
import multiprocessing
from pyimpact import server
from os.path import dirname, join, abspath


CWD = join(dirname(__file__), 'data')


class RunServerTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        server.BASE_DIR = CWD
        cls.process = multiprocessing.Process(target=server.run_server)
        cls.process.daemon = True
        cls.process.start()
        time.sleep(2)

    def test_root_url_returns_index(self):
        response = urllib2.urlopen('http://localhost:8080/')
        self.assertEqual(200, response.code)
        self.assertEqual("INDEX", response.read().strip())

    def test_editor_url_returns_weltmeister(self):
        response = urllib2.urlopen('http://localhost:8080/editor')
        self.assertEqual(200, response.code)
        self.assertEqual("EDITOR", response.read().strip())
