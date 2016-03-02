import os
import tempfile

class Error (Exception): pass

class SampleKmers:
    def __init__(self,sampledata,output_directory, minimum_kmer_coverage = 10, kmc_exec = 'kmc', kmer_length = 31, verbose = False):
        self.sampledata = sampledata
        self.output_directory =  os.path.abspath(output_directory)
        self.minimum_kmer_coverage = minimum_kmer_coverage
        self.kmc_exec = kmc_exec
        self.kmer_length = kmer_length
        self.verbose = verbose
        
    def run(self):
        current_directory = os.getcwd()
        os.chdir(self.output_directory)
        
        make a temp directory
        with tempfile.TemporaryDirectory() as tmpdirname:
            with tempfile.NamedTemporaryFile() as fofn:
                
                if self.sampledata.forward:
                    fofn.write(self.sampledata.forward, "\n")
                else:
                    raise Error('Cannot find the forward reads file')
                    
                if self.sampledata.reverse:
                    # paired ended
                    fofn.write(self.sampledata.reverse, "\n")
                
                kmc_command = ''.join(self.kmc_exec, " -k", self.kmer_length, " -ci", self.minimum_kmer_coverage, " @", fofn.name, " ", " kmc_output ", tmpdirname)
                if self.verbose:
                    print('KMC command for creating sample kmers for ',self.sampledata.forward,': ', kmc_command)

        os.chdir(current_directory)
        return 1
