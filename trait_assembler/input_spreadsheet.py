import os
import csv
from trait_assembler import common

class SampleData:
    def __init__(self,row):
        
        if row[0]:
            self.forward = os.path.abspath(row[0])
        else:
            self.forward = row[0]
        
        if row[1]:
            self.reverse = os.path.abspath(row[1])
        else:
            self.reverse = row[1]
        
        if not row[2] == '':
            self.trait = int(row[2])
        else:
            self.trait = row[2]
    

class InputSpreadsheet:
    def __init__(self,filename, delimiter = ','):
        self.filename = os.path.abspath(filename)
        self.delimiter = delimiter
    
    def is_valid_file(self):
        # does the file exist?
        if not os.path.exists(self.filename):
            return False
        
        dataseen = 0
        # read in the spreadsheet
        with open(self.filename) as csvfile:
            spreadsheetreader = csv.reader(csvfile, delimiter = self.delimiter)
            for row in spreadsheetreader:
                # there needs to be 3 columns
                if len(row) != 3 or not row[0]:
                    continue
                sd = SampleData(row)
                
                # does the forward reads file exist?
                if not os.path.exists(sd.forward):
                    return False
                    
                # if the reverse read filename is filled in, it must exist
                if sd.reverse and not os.path.exists(sd.reverse):
                    return False
                
                # does each row have a trait and is it zero or one?
                if sd.trait not in [0,1]:
                    return False
                dataseen = 1
        
        if dataseen:
            return True
        else:
            return False
