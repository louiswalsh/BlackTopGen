import unittest
import sqlite3

class MyTestCase(unittest.TestCase):
    def testTable(self):
        assert sum([1, 2]) == 3

    def testTableConnection (self):
        connectionObject = sqlite3.connect("BLKTP_PLYRS.db")
        #assert (cursorObject = connectionObject.cursor());

if __name__ == '__main__':
    unittest.main()
