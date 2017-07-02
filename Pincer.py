import os
from Bio.Seq import Seq
from Bio import pairwise2

from ObjectClasses.Sequence import Sequence
from ObjectClasses.Primer import PrimerPair
from ObjectClasses.Alignment import Alignment

class Pincer:
    def __init__(self, assembly_filename, primer_filename):
        self.contigs = Sequence(assembly_filename)
        
        primerPair = PrimerPair(primer_filename)
        self.primer1 = primerPair[0]
        self.primer2 = primerPair[1]
        
    def amplicon_positions(self, target, penalty_matrix,
                           min_score, min_product_length, max_product_length):
        
        ### Local helper functions
        
        def get_alignment_above_min_score(alignments):
            return [align for align in alignments if Alignment(align).filter_by_score(min_score)]
        
        def align_and_filter(target, primer):
            alignment = pairwise2.align.localms(target, primer, 
                                                match, mismatch, gap_open, gap_extend)
            
            return get_alignment_above_min_score(alignment)
            
        def permute_possible(positions1, positions2):
            
            def logical_position(pos1, pos2):
                if pos1 > pos2:
                    return (pos2, pos1)
                if pos2 > pos1:
                    return (pos1, pos2)
            
            def get_shortest_range_and_filter(pos_tuple1, pos_tuple2):
                minimum_diff = float("inf")
                shortest_range = None
                
                for pos1 in pos_tuple1:
                    for pos2 in pos_tuple2:
                        diff = abs(pos1-pos2)
                        if diff < minimum_diff:
                            minimum_diff = diff
                            small, big = logical_position(pos1, pos2)
                
                if (big - small >= min_product_length) and (big - small <= max_product_length):
                    return (small, big)
            
            contig_set = []
            
            for tuple1 in positions1:
                for tuple2 in positions2:
                    pos_to_extract = get_shortest_range_and_filter(tuple1, tuple2)
                    if pos_to_extract != None:
                        contig_set.append(pos_to_extract)
                        
            return contig_set
        
        def one_full_pcr(target, forward, reverse):
            reverse = reverse.reverse_complement()
            
            forward_align = align_and_filter(target, forward)
            
            if len(forward_align) > 0:
                reverse_align = align_and_filter(target, reverse)
                
            if len(forward_align) > 0 and len(reverse_align) > 0:
                forward_positions = [Alignment(align).Positions for align in forward_align]
                reverse_positions = [Alignment(align).Positions for align in reverse_align]
                
                return (forward_positions, reverse_positions)
            
        ### Start here
        match, mismatch, gap_open, gap_extend = penalty_matrix
        
        all_tups = one_full_pcr(target, self.primer1, self.primer2)
        
        if all_tups != None:
            primer1_tups, primer2_tups = all_tups
            
            return permute_possible(primer1_tups, primer2_tups)
            
    def run_Pincer(self, penalty_matrix=(1, 0, -2, -2), 
                    min_score=17, min_product_length=500, max_product_length=4000):
        
        for idx, contig in enumerate(self.contigs):
            target = contig
            product_post = self.amplicon_positions(contig, penalty_matrix, min_score, min_product_length, max_product_length)
            
            if product_post != None:
                for tup in product_post:
                    print(contig[tup[0]:tup[1]])