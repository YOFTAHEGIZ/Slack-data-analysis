import unittest
import pandas as pd
from src.loader import SlackDataLoader

class SlackDataLoaderTestCase(unittest.TestCase):

    def setUp(self):
        # Initialize the SlackDataLoader instance
        self.loader = SlackDataLoader(r'..\data\Anonymized_B6SlackExport_25Nov23\anonymized')
        
    def test_load_data_columns(self):
        # Specify the expected columns in the DataFrame
        expected_columns = ['timestamp', 'user', 'channel', 'message']
        
        # Load the data using the desired method from SlackDataLoader
        data = self.loader.get_users()
        
        # Check if the loaded data DataFrame has the expected columns
        self.assertCountEqual(expected_columns, data.columns.tolist())

if __name__ == '__main__':
    unittest.main()