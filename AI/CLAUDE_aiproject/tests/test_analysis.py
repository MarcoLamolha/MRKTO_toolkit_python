import unittest
from src.analysis.data_analysis import load_data, clean_data, perform_analysis

class TestDataAnalysis(unittest.TestCase):

    def test_load_data(self):
        # Test loading data from a CSV file
        data = load_data('test_data.csv')
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

    def test_clean_data(self):
        # Test cleaning data
        raw_data = {'column1': [1, 2, None], 'column2': ['a', 'b', 'c']}
        cleaned_data = clean_data(raw_data)
        self.assertNotIn(None, cleaned_data['column1'])
        self.assertEqual(len(cleaned_data), 2)

    def test_perform_analysis(self):
        # Test performing analysis
        data = {'column1': [1, 2, 3], 'column2': [4, 5, 6]}
        result = perform_analysis(data)
        self.assertEqual(result['mean_column1'], 2)
        self.assertEqual(result['sum_column2'], 15)

if __name__ == '__main__':
    unittest.main()