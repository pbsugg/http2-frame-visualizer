import os
import main
import unittest
import tempfile

class MainTestCase(unittest.TestCase):

    def setUp(self):
        self.app = flaskr.app.test_client()


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
