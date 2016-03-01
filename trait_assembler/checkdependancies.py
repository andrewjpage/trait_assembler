import re
from trait_assembler import program
# From circlator v0.14.2 by Martin Hunt

class Error (Exception): pass

class CheckDependancies:
    def __init__(self, verbose=False):
        self.verbose = verbose
        
        self.prog_to_version_cmd = {
            'kmc': ('', re.compile('^K-Mer Counter (KMC) ver. ([0-9\.]+)')),
            'samtools': ('', re.compile('^Version: ([0-9\.]+)')),
            'spades': ('', re.compile('^SPAdes genome assembler v.([0-9\.]+)')),
        }

        self.min_versions = {
            'kmc': '2.3.0',
            'samtools': '0.1.9',
            'spades': '3.5.0',
        }

        self.prog_name_to_default = {
            'kmc': 'kmc',
            'spades': 'spades.py',
            'samtools': 'samtools',
        }
    
    def make_and_check_prog(self, name):
        p = program.Program(
            self.prog_name_to_default[name],
            self.prog_to_version_cmd[name][0],
            self.prog_to_version_cmd[name][1]
        )
    
        if not p.in_path():
            raise Error('Error cannot find ' + name + ' in the PATH')
    
        if not p.version_at_least(self.min_versions[name]):
            raise Error('Error version of ' + name + ' too low. I found ' + p.version() + ', but must be at least ' + self.min_versions[name])
    
        if self.verbose:
            print('Found ', name, 'version', p.version())
    
        return p
    
    def check_all_progs_readable(self):
        for prog in self.prog_name_to_default:
            try:
                self.make_and_check_prog(prog)
            except Error as e:
                print(e)
    
    def check_all_progs(self):
        for prog in self.prog_name_to_default:
            self.make_and_check_prog(prog)
    