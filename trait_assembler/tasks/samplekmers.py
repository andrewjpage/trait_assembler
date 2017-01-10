import argparse
import sys
import trait_assembler

def run():
    parser = argparse.ArgumentParser(
        description = 'Create a KMC database for each sample in a spreadsheet',
        usage = 'trait_assembler samplekmers [options] <spreadsheet.csv> <output_directory>')
    parser.add_argument('--delimiter', help='Delimiter between cells, defaults to comma', default=',', metavar='STRING')
    parser.add_argument('--min_kmer_coverage', type=int, help='Minimum kmer coverage [%(default)s]', metavar='INT', default=10)
    parser.add_argument('--kmer_length', type=int, help='Kmer length [%(default)s]', metavar='INT', default=31)
    parser.add_argument('--verbose', action='store_true', help='Be verbose')
    parser.add_argument('--kmc_exec', help='KMC executable', default='kmc', metavar='STRING')
    
    parser.add_argument('input_spreadsheet_filename', help='Input spreadsheet filename')
    parser.add_argument('output_directory', help='Output directory')
    options = parser.parse_args()

    samplekmers = trait_assembler.samplekmers.SampleKmers(
        options.input_spreadsheet_filename,
        options.output_directory,
        delimiter=options.delimiter,
        verbose=options.verbose,
        minimum_kmer_coverage=options.min_kmer_coverage,
        kmer_length=options.kmer_length,
        kmc_exec=options.kmc_exec,
    )
    samplekmers.run()
