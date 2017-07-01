from Bio import SeqIO
import os.path
from Sequence import Sequence

class PrimerPair(Sequence):
    def __init__(self, filename):
        Sequence.__init__(self, filename)
        
        assert self.get_contig_number() == 2, "May not be primer pair!"
        
        self.primer1 = self.contigs[0]
        self.primer2 = self.contigs[1]
        
    def __repr__(self):        
        string = "PrimerPair {0} of {1} ({2}bps) and {3} ({4}bps)"
        return string.format(self.name, self.primer1, len(self.primer1), self.primer2, len(self.primer2))