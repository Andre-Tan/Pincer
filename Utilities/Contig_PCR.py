from Bio import pairwise2

from ObjectClasses.Alignment import Alignment

class Contig_PCR:
    
    """
    Contig_PCR: Run in silico PCR on a single contig.
    
    Note: This class is intended for Pincer.
            You can find Pincer on:
    
    You need to supplement: 
    1. target contig: a Seq object
    2. primer1 and primer2: 2 Seq object, both in 5'-3' direction
    3. penalty_tuple: for Bio.pairwise2, tuple of integes consisting 
        (match, mismatch, gap open, gap extend). Only match is supposed to be positive.
    4. min_score: integer, to filter alignments.
    5. min_product_length: integer, x basepairs of minimum expected product length.
    6. max_product_length: integer, x basepairs of minimum expected product length.
    
    Will output the product sequence.
    """
    
    def __init__(self, target, primer1, primer2, penalty_tuple,
                min_score, min_product_length, max_product_length):
        
        self.target_seq = target.sequence
        self.target_id = target.id
        
        self.primer1 = primer1.sequence
        self.primer2 = primer2.sequence
        
        self.penalty_tuple = penalty_tuple
        
        self.min_score = min_score
        self.min_product_length = min_product_length
        self.max_product_length = max_product_length
        
    ### Local helper functions

    def align_and_filter(self, target_seq, primer):
        """
        Align target and a single primer.
        
        Will output a list of the alignments above threshold min_score.
        Returns None if no alignment is above threshold min_score.
        """
        
        def get_alignment_above_min_score(alignments):
            return [align for align in alignments if Alignment(align).filter_by_score(self.min_score)]
        
        match, mismatch, gap_open, gap_extend = self.penalty_tuple
        
        alignment = pairwise2.align.localms(target_seq, primer, match, mismatch,
                                            gap_open, gap_extend)
        
        return get_alignment_above_min_score(alignment)
        
    def permute_possible(self, positions1, positions2):
        """
        Permute possible products of PCR, filtered by min and max product_length.
        Returns None if nothing is above threshold.
        """
        
        def logical_position(pos1, pos2):
            
            if pos1 > pos2:
                return (pos2, pos1)
            if pos2 > pos1:
                return (pos1, pos2)
        
        def get_shortest_range_and_filter(pos_tuple1, pos_tuple2):
            minimum_diff = float("inf")
            
            for pos1 in pos_tuple1:
                for pos2 in pos_tuple2:
                    diff = abs(pos1-pos2)
                    if diff < minimum_diff:
                        minimum_diff = diff
                        small, big = logical_position(pos1, pos2)
            
            if (big - small >= self.min_product_length) and (big - small <= self.max_product_length):
                return (small, big)
        
        ### permute_possible() starts here
        
        contig_set = []
        
        for tuple1 in positions1:
            for tuple2 in positions2:
                pos_to_extract = get_shortest_range_and_filter(tuple1, tuple2)
                if pos_to_extract != None:
                    contig_set.append(pos_to_extract)
        
        if contig_set != []:
            return contig_set

    def strand_pcr(self, target_seq, forward, reverse):
        """
        Perform the single strand PCR.
        
        Output alignment of forward primer and reverse primer on target,
        None if forward and reverse primers do not both align on target.
        """
        
        reverse = reverse.reverse_complement()
        
        forward_align = self.align_and_filter(target_seq, forward)
        
        if len(forward_align) > 0:
            reverse_align = self.align_and_filter(target_seq, reverse)
            
        if len(forward_align) > 0 and len(reverse_align) > 0:
            forward_positions = [Alignment(align).Positions for align in forward_align]
            reverse_positions = [Alignment(align).Positions for align in reverse_align]
            
            return (forward_positions, reverse_positions)
    
    def show_product_sequence(self, target_seq, primer_align_positions, direction):
        """
        Extract the product sequence if primer_align_positions is not None.
        """
        
        def write_out(target_seq, product_pos):
            string_out = ""
            id = self.target_id
            last_idx = len(product_pos) - 1
            
            for idx, tup in enumerate(product_pos):
                start, end = tup[0], tup[1]
                size = end - start
                product = target_seq[start:end]
                
                string_out += ">{0}:{1}:{2}-{3}:{4}bps\n{5}\n".format(id, direction, start, end, size, product)
            
            return string_out
            
        if primer_align_positions != None:
            primer1_tups, primer2_tups = primer_align_positions
            product_positions = self.permute_possible(primer1_tups, primer2_tups)
            
            if product_positions != None:
                return write_out(target_seq, product_positions)
    
    def run_PCR_pipeline(self):
        """
        Run this and you are good to go. Essentially the main().
        """
        
        template_strand = self.target_seq
        reverse_strand = self.target_seq.reverse_complement()
        
        contig_pcr_output = ""
        
        # Run PCR against template strand
        template_primer_positions = self.strand_pcr(template_strand, self.primer1, self.primer2)
        
        sense_product = self.show_product_sequence(template_strand, template_primer_positions, "Sense")
        
        # Run PCR against reverse strand
        reverse_primer_positions = self.strand_pcr(reverse_strand, self.primer1, self.primer2)
        
        antisense_product = self.show_product_sequence(reverse_strand, reverse_primer_positions, "Antisense")
        
        if sense_product != None:
            contig_pcr_output += sense_product
        if antisense_product != None:
            contig_pcr_output += antisense_product
        
        return contig_pcr_output