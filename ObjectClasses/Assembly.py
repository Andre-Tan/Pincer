from Bio import SeqIO
import os.path
from Sequence import Sequence

class Assembly(Sequence):
    def __init__(self, filename):
        Sequence.__init__(self, filename)

    def __repr__(self):        
        string = "Assembly {} with {} contigs totaling {}bps"
        return string.format(self.name, self.get_contig_number(), self.get_total_seq_length())