import argparse
import sys
import trait_assembler

def run():
    parser = argparse.ArgumentParser(
        description = 'Check the input spreadsheet is valid',
        usage = 'trait_assembler checkspreadsheet [options] <spreadsheet.csv>')
    parser.add_argument('--delimiter', help='Delimiter between cells, defaults to comma', default=',', metavar='STRING')

    parser.add_argument('input_spreadsheet_filename', help='Input spreadsheet filename')
    options = parser.parse_args()

    checkspreadsheet = trait_assembler.checkspreadsheet.CheckSpreadsheet(
        options.input_spreadsheet_filename,
        delimiter=options.delimiter
    )
    if checkspreadsheet.is_valid_file():
        print("Valid file")
    else:
        print("Invalid file")
