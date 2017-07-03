import os
from Bio import pairwise2

from ObjectClasses.Sequence import Sequence
from ObjectClasses.Primer import PrimerPair
from ObjectClasses.Alignment import Alignment

from Utilities.Contig_PCR import Contig_PCR

class Pincer:
    def __init__(self, assembly_filename, primer_filename):
        self.contigs = Sequence(assembly_filename)
        
        primerPair = PrimerPair(primer_filename)
        self.primer1 = primerPair[0]
        self.primer2 = primerPair[1]
    
    def filter_contigs_by_length(self, min_product_length):
        return [contig for contig in self.contigs if len(contig) >= min_product_length]
    
    def run_Pincer(self, penalty_matrix=(1, 0, -5, -2), 
                    min_score=16, min_product_length=500, max_product_length=4000):
        
        contigs_to_run = self.filter_contigs_by_length(min_product_length)
        
        for idx, contig in enumerate(contigs_to_run):
        
            contig_pcr = Contig_PCR(contig, self.primer1, self.primer2, penalty_matrix,
                                    min_score, min_product_length, max_product_length)
            
            contig_pcr.run_PCR_pipeline()