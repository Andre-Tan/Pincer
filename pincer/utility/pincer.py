from sys import exit
import os
import logging

from pincer.objects.sequence import Sequence
from pincer.objects.primer import PrimerPair
from pincer.objects.alignment import Alignment

from pincer.utility.contig_pcr import Contig_PCR

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

class IncorrectIntegerValueException(Exception):
    pass
    
class Pincer:
    def __init__(self, assembly_filename, primer_filename, min_3_end=10, threshold=10,
                min_score=16, min_product_length=500, max_product_length=3000, output_filename=None):
                
        self.contigs = Sequence(assembly_filename)
        
        primerPair = PrimerPair(primer_filename)
        self.primer1 = primerPair.primer1
        self.primer2 = primerPair.primer2
        
        self.min_3_end = min_3_end
        self.threshold = threshold
        
        self.min_score = self.assert_int_correct(min_score)
        self.min_product_length = self.assert_int_correct(min_product_length)
        self.max_product_length = self.assert_int_correct(max_product_length)
        
        self.output_filename = output_filename
            
    def assert_int_correct(self, unit):
        int_err = "{} is not positive integer."
        
        if type(unit) is int and unit > 0:
            return unit
        else:
            raise IncorrectIntegerValueException(int_err.format(unit))
    
    def filter_contigs_by_length(self):
        return [contig for contig in self.contigs if len(contig) >= self.min_product_length]
    
    def write_where(self, pincer_output):
        output = pincer_output[:-1]
        
        if pincer_output:
            if self.output_filename == "None" or self.output_filename == None:
                print(output)
            else:
                with open(self.output_filename, "w") as handle:
                    handle.write(output)
        else:
            logger.info("There is no output.")
            
        return output
            
    def run_Pincer(self):
        
        contigs_to_run = self.filter_contigs_by_length()
        pincer_output = ""
        
        logger.info("Running Pincer on {} contigs in {}".format(len(contigs_to_run), self.contigs.name))
        
        for idx, contig in enumerate(contigs_to_run):
            
            contig_pcr = Contig_PCR(contig, self.primer1, self.primer2, 
                                    self.min_3_end, self.threshold,
                                    self.min_score, self.min_product_length, self.max_product_length)
            
            pincer_output += contig_pcr.run_PCR_pipeline()
        
        logger.info("Finished Pincer in {}".format(self.contigs.name))
        
        return self.write_where(pincer_output)