import argparse
import sys
import trait_assembler

def run():
    parser = argparse.ArgumentParser(
        description = 'Check the dependancies are installed and the correct versions',
        usage = 'trait_assembler checkdependancies')
        
    options = parser.parse_args()

    checkdependancies = trait_assembler.checkdependancies.CheckDependancies(
        verbose=True
    )
    checkdependancies.check_all_progs_readable()
