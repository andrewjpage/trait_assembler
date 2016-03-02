import unittest
import filecmp
import os
from trait_assembler import samplekmers

modules_dir = os.path.dirname(os.path.abspath(checkspreadsheet.__file__))
data_dir = os.path.join(modules_dir, 'tests', 'data', 'samplekmers')

class TestCheckSpreadsheet(unittest.TestCase):
    
    def test_invalid_spreadsheet_doesnt_exist(self):
        '''test_invalid_spreadsheet_doesnt_exist'''
        i = checkspreadsheet.CheckSpreadsheet(os.path.join(data_dir, 'file_which_doesnt_exist'))
        self.assertFalse(i.is_valid_file())
        self.assertEqual(i.parse_sample_data(),[])