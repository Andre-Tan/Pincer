import os
from Bio.Seq import Seq
from Bio import pairwise2

from ObjectClasses.Assembly import Assembly

class NotFileException(Exception):
    pass

class PrimerO:
    def __init__(self, assembly_filename, primer_filename=None):
        assert os.path.isfile(assembly_filename), NotFileException("{} is not a file!".format(assembly_filename))
        #assert os.path.isfile(primer_filename), NotFileException("{} is not a file!".format(assembly_filename))        
        
        self.contigs = Assembly(assembly_filename)
        
        self.primer1 = Seq("TATTCGCTTAGAAAATTAA")
        self.primer2 = Seq("GCAAGTTCTTCAGCTTGTTT").reverse_complement()
        
    def amplicon_positions(self, contig_num, penalty_matrix,
                           min_score, min_product_length, max_product_length):
        
        target = self.contigs[contig_num]
        primer1 = self.primer1
        primer2 = self.primer2
        
        match, mismatch, gap_open, gap_extend = penalty_matrix
        
        def filter_alignment(alignments, min_score):
            return [align for align in alignments if Alignment(align).filter_by_score(min_score)]
        
        def permute_possible(start, end, min_product_length, max_product_length):
            contig_set = []
            
            for id1 in start:
                for id2 in end:
                    if id1 > id2:
                        if (id1 - id2 >= min_product_length) and (id1 - id2 <= max_product_length):
                            contig_set.append((id2, id1))
                    if id2 > id1:
                        if (id2 - id1 >= min_product_length) and (id2 - id1 <= max_product_length):
                            contig_set.append((id1, id2))
            
            return contig_set
        
        # Align with forward primer, and filter by minimum alignment score.
        print("align target with {}".format(primer1))
        primer1_alignment = pairwise2.align.localms(target, primer1, 
                                                    match, mismatch, gap_open, gap_extend)
        filtered_1 = filter_alignment(primer1_alignment, min_score)
        
        # If a primer1 alignment where minimum alignment score is reached exists, find primer2 alignment.
        if len(filtered_1) > 0:
            print("Yes! Align target with {}".format(primer2))
            primer2_alignment = pairwise2.align.localms(target, primer2,
                                                        match, mismatch, gap_open, gap_extend)
            filtered_2 = filter_alignment(primer2_alignment, min_score)
        
        # If both primer1 and primer2 aligned in contig, extract the possible product positions
        if len(filtered_1) > 0 and len(filtered_2) > 0:
        
            primer1_alignments = [Alignment(alignment1).endPosition for alignment1 in filtered_1]
            primer2_alignments = [Alignment(alignment2).startPosition for alignment2 in filtered_2]
            
            return permute_possible(primer1_alignments, primer2_alignments, min_product_length, max_product_length)
            
    def run_primerO(self, penalty_matrix=(1, 0, -2, -2), 
                    min_score=17, min_product_length=500, max_product_length=4000):
        
        for idx, contig in enumerate(self.contigs):
            product_post = self.amplicon_positions(idx, penalty_matrix, min_score, min_product_length, max_product_length)
            
            for tup in product_post:
                print(contig[tup[0]:tup[1]])
            
class Alignment:
    def __init__(self, align_tup):
        assert len(align_tup) == 5, "Are you sure it is alignment output?"
        subject, aligned, score, start, end = align_tup
        
        self.subject = subject
        self.aligned = aligned
        self.score = score
        self.startPosition = start
        self.endPosition = end
        
    def filter_by_score(self, score):
        return self.score >= score