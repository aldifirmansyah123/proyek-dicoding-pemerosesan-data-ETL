import sys
import os

# Menambahkan folder utama ke dalam sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from utils.load import save_to_csv, save_to_google_sheets, load_to_postgresql

class TestLoad(unittest.TestCase):

    @patch('utils.load.pd.DataFrame.to_csv')
    def test_save_to_csv(self, mock_to_csv):
        """Test untuk fungsi save_to_csv"""
        df = pd.DataFrame({
            'title': ['Product 1', 'Product 2'],
            'price': [10000, 20000],
            'rating': [4.5, 5.0]
        })
        save_to_csv(df, 'test.csv')
        mock_to_csv.assert_called_once_with('test.csv', index=False)

    @patch('utils.load.build')
    @patch('utils.load.Credentials.from_service_account_file')
    def test_save_to_google_sheets(self, mock_creds, mock_build):
        """Test untuk fungsi save_to_google_sheets"""
        df = pd.DataFrame({
            'title': ['Product 1', 'Product 2'],
            'price': [10000, 20000],
            'rating': [4.5, 5.0]
        })
        mock_creds.return_value = MagicMock()
        mock_service = MagicMock()
        mock_build.return_value = mock_service
        save_to_google_sheets(df, 'spreadsheet_id', 'Sheet1!A2')
        mock_service.spreadsheets.return_value.values.return_value.update.assert_called_once()

    @patch('utils.load.create_engine')
    def test_load_to_postgresql(self, mock_create_engine):
        """Test untuk fungsi load_to_postgresql"""
        df = pd.DataFrame({
            'title': ['Product 1'],
            'price': [10000],
            'rating': [4.5],
            'colors': [2],
            'size': ['M'],
            'gender': ['Unisex'],
            'timestamp': ['2025-05-26 20:00:00']
        })
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine
        df.to_sql = MagicMock()
        load_to_postgresql(df, table_name='test_products')
        df.to_sql.assert_called_once_with('test_products', mock_engine, if_exists='replace', index=False)

if __name__ == '__main__':
    unittest.main()
