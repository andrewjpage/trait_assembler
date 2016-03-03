import os
import csv

class SampleData:
    def __init__(self,row):
        
        if row[0]:
            self.forward = os.path.abspath(row[0].strip())
        else:
            self.forward = row[0].strip()
        
        if row[1]:
            self.reverse = os.path.abspath(row[1].strip())
        else:
            self.reverse = row[1].strip()
        
        if not row[2] == '':
            self.trait = int(row[2].strip())
        else:
            self.trait = row[2].strip()
    

class CheckSpreadsheet:
    def __init__(self,filename, delimiter = ','):
        self.filename = os.path.abspath(filename)
        self.delimiter = delimiter
        self.metadata_for_samples =[]
        
    def parse_sample_data(self):
        
        if  self.is_valid_file() == False:
            return self.metadata_for_samples
            
        with open(self.filename) as csvfile:
            spreadsheetreader = csv.reader(csvfile, delimiter = self.delimiter)
            for row in spreadsheetreader:
                sd = SampleData(row)
                self.metadata_for_samples.append(sd)
                
        return self.metadata_for_samples
        
    
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
