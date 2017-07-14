from sys import exit
from Bio import SeqIO
from objects.Sequence import Sequence

class NotContigPairException(Exception):
    pass

class PrimerPair(Sequence):
    def __init__(self, filename):
        Sequence.__init__(self, filename)
        
        self.assert_primer_is_pair()
           
        self.primer1 = self.contigs[0]
        self.primer2 = self.contigs[1]
        
    def __repr__(self):        
        string = "PrimerPair {0} of {1} ({2}bps) and {3} ({4}bps)"
        return string.format(self.name, self.primer1.sequence, len(self.primer1), self.primer2.sequence, len(self.primer2))
        
    def assert_primer_is_pair(self):
        if self.get_contig_number() != 2:
            raise NotContigPairException("{} does not contain 2 primers!".format(self.file))
            exit(1)
            