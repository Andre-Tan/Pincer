from sys import exit
from Bio import pairwise2

from ObjectClasses.Sequence import Sequence
from ObjectClasses.Primer import PrimerPair
from ObjectClasses.Alignment import Alignment

from Utilities.Contig_PCR import Contig_PCR

class IncorrectLengthException(Exception):
    pass

class IncorrectIntegerValueException(Exception):
    pass
    
class Pincer:
    def __init__(self, assembly_filename, primer_filename, penalty_tuple,
                min_score, min_product_length, max_product_length, output_filename):
                
        self.contigs = Sequence(assembly_filename)
        
        primerPair = PrimerPair(primer_filename)
        self.primer1 = primerPair.primer1
        self.primer2 = primerPair.primer2
        
        self.penalty_tuple = self.assert_tuple_correct(penalty_tuple, 4)
        
        self.min_score = self.assert_int_correct(min_score)
        self.min_product_length = self.assert_int_correct(min_product_length)
        self.max_product_length = self.assert_int_correct(max_product_length)
        
        self.output_filename = output_filename
    
    def assert_tuple_correct(self, unit, correct_length):
        tuple_err = "{} may not be the correct tuple format."
        
        if type(unit) is tuple and len(unit) == correct_length:
            match, mismatch, open, extend = unit
            if match > 0 and mismatch <= 0 and open <= 0 and extend <= 0:
                return unit
        else:
            raise IncorrectTupleException(tuple_err.format(unit))
            
    def assert_int_correct(self, unit):
        int_err = "{} is not positive integer."
        
        if type(unit) is int and unit > 0:
            return unit
        else:
            raise IncorrectIntegerValueException(int_err.format(unit))
    
    def filter_contigs_by_length(self):
        return [contig for contig in self.contigs if len(contig) >= self.min_product_length]
    
    def write_where(self, pincer_output):
        if self.output_filename == "None" or self.output_filename == None:
            print(pincer_output[:-1])
        else:
            with open(self.output_filename, "w") as handle:
                handle.write(pincer_output[:-1])
            
        return pincer_output[:-1]
            
    def run_Pincer(self):
        
        contigs_to_run = self.filter_contigs_by_length()
        pincer_output = ""
        
        for idx, contig in enumerate(contigs_to_run):
        
            contig_pcr = Contig_PCR(contig, self.primer1, self.primer2, self.penalty_tuple,
                                    self.min_score, self.min_product_length, self.max_product_length)
            
            pincer_output += contig_pcr.run_PCR_pipeline()
        
        return self.write_where(pincer_output)