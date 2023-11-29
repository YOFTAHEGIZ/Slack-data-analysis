import unittest 
import os
import sys

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from src.loader import SlackDataLoader
from src.loader import SlackDataLoader
import json 

class Test(unittest.TestCase):

    def test_get_channesl(self):
        sl = SlackDataLoader(os.getcwd())
        channels = sl.get_channels()

        expected_columns = ['id', 'name', 'created', 'creator', 'is_archived', 'is_general', 'members', 'topic', 'purpose', 'pins']
        for channel in channels:
            self.assertListEqual(list(channel.keys()), expected_columns)

    
if __name__ == '__main__':
    unittest.main()