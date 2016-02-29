import unittest
import filecmp
import os
from trait_assembler import input_spreadsheet

modules_dir = os.path.dirname(os.path.abspath(input_spreadsheet.__file__))
data_dir = os.path.join(modules_dir, 'tests', 'data', 'input_spreadsheet')

class TestInputSpreadsheet(unittest.TestCase):
    
    def test_invalid_spreadsheet_doesnt_exist(self):
        '''test_invalid_spreadsheet_doesnt_exist'''
        i = input_spreadsheet.InputSpreadsheet(os.path.join(data_dir, 'file_which_doesnt_exist'))
        self.assertFalse(i.is_valid_file())
    
    def test_invalid_empty_file(self):
        '''test_invalid_empty_file'''
        i = input_spreadsheet.InputSpreadsheet(os.path.join(data_dir, 'empty_file.csv'))
        self.assertFalse(i.is_valid_file())
    
    def test_invalid_file_doesnt_exist(self):
        '''test_invalid_file_doesnt_exist'''
        i = input_spreadsheet.InputSpreadsheet(os.path.join(data_dir, 'file_doesnt_exist.csv'))
        self.assertFalse(i.is_valid_file())
    
    def test_invalid_missing_cells(self):
        '''test_invalid_missing_cells'''
        i = input_spreadsheet.InputSpreadsheet(os.path.join(data_dir, 'missing_cells.csv'))
        self.assertFalse(i.is_valid_file())
    
    def test_invalid_missing_header(self):
        '''test_invalid_missing_header'''
        i = input_spreadsheet.InputSpreadsheet(os.path.join(data_dir, 'missing_header.csv'))
        self.assertFalse(i.is_valid_file())
    
    def test_invalid_missing_traits(self):
        '''test_invalid_missing_traits'''
        i = input_spreadsheet.InputSpreadsheet(os.path.join(data_dir, 'missing_traits.csv'))
        self.assertFalse(i.is_valid_file())
    
    def test_multiple_mixed_ended(self):
        '''test_multiple_mixed_ended'''
        i = input_spreadsheet.InputSpreadsheet(os.path.join(data_dir, 'multiple_mixed_ended.csv'))
        self.assertTrue(i.is_valid_file())
    
    def test_multiple_paired_ended(self):
        '''test_multiple_paired_ended'''
        i = input_spreadsheet.InputSpreadsheet(os.path.join(data_dir, 'multiple_paired_ended.csv'))
        self.assertTrue(i.is_valid_file())
    
    def test_multiple_single_ended(self):
        '''test_multiple_single_ended'''
        i = input_spreadsheet.InputSpreadsheet(os.path.join(data_dir, 'multiple_single_ended.csv'))
        self.assertTrue(i.is_valid_file())
    
    def test_one_paired_ended(self):
        '''test_one_paired_ended'''
        i = input_spreadsheet.InputSpreadsheet(os.path.join(data_dir, 'one_paired_ended.csv'))
        self.assertTrue(i.is_valid_file())
    
    def test_one_paired_ended_tab(self):
        '''test_one_paired_ended_tab'''
        i = input_spreadsheet.InputSpreadsheet(os.path.join(data_dir, 'one_paired_ended.tsv'), "\t")
        self.assertTrue(i.is_valid_file())
    
    def test_one_paired_ended_unzipped(self):
        '''test_one_paired_ended_unzipped'''
        i = input_spreadsheet.InputSpreadsheet(os.path.join(data_dir, 'one_paired_ended_unzipped.csv'))
        self.assertTrue(i.is_valid_file())
    
    def test_one_single_ended(self):
        '''test_one_single_ended'''
        i = input_spreadsheet.InputSpreadsheet(os.path.join(data_dir, 'one_single_ended.csv'))
        self.assertTrue(i.is_valid_file())
    
    def test_one_single_ended_blank_lines(self):
        '''test_one_single_ended_blank_lines'''
        i = input_spreadsheet.InputSpreadsheet(os.path.join(data_dir, 'one_single_ended_blank_lines.csv'))
        self.assertTrue(i.is_valid_file())
        
        
        