import unittest

from run_Pincer import buildParser, generatePincerObj
from Utilities.Pincer import Pincer

test_no_path = "this is a null test"
sequence_path = "/home/andret1/dev/Pincer/TestData/contig.fasta"
seq_rc_path = "/home/andret1/dev/Pincer/TestData/contig_rev_comp.fasta"

primer_path = "/home/andret1/dev/Pincer/TestData/primer.fa"

default_pincer = generatePincerObj(query=sequence_path, primers=primer_path)
test_pincer = generatePincerObj(query=assembly_2, primers=primer_path,
                                min_product_length=5000, output_filename=None)

product = ">.10702_6_10.6 Sense:113768-114904:1136bps\nAAACAGGAACGGCTTCAGTAGCGGTAGCTTTGACTGTTTTAGGGGCAGGTTTTGCGAATCAAACAGAGGTTAAGGCTAACGGTGATGGTAATCCTAGGGAAGTTATAGAAGATCTTGCAGCAAACAATCCCGCAATACAAAATATACGTTTACGTCACGAAAACAAGGACTTAAAAGCGAGATTAGAGAATGCAATGGAAGTTGCAGGAAGAGATTTTAAGAGAGCTGAAGAACTTGAAAAAGCAAAACAAGCCTTAGAAGACCAGCGTAAAGATTTAGAAACTAAATTAAAAGAACTACAACAAGACTATGACTTAGCAAAGGAATCAACAAGTTGGGATAGACAAAGACTTGAAAAAGAGTTAGAAGAGAAAAAGGAAGCTCTTGAATTAGCGATAGACCAGGCAAGTCGGGACTACCATAGAGCTACCGCTTTAGAAAAAGAGTTAGAAGAGAAAAAGAAAGCTCTTGAATTAGCGATAGACCAAGCGAGTCAGGACTATAATAGAGCTAACGTCTTAGAAAAAGAGTTAGAAACGATTACTAGAGAACAAGAGATTAATCGTAATCTTTTAGGCAATGCAAAACTTGAACTTGATCAACTTTCATCTGAAAAAGAGCAGCTAACGATCGAAAAAGCAAAACTTGAGGAAGAAAAACAAATCTCAGACGCAAGTCGTCAAAGCCTTCGTCGTGACTTGGACGCATCACGTGAAGCTAAGAAACAGGTTGAAAAAGATTTAGCAAACTTGACTGCTGAACTTGATAAGGTTAAAGAAGACAAACAAATCTCAGACGCAAGCCGTCAAGGCCTTCGCCGTGACTTGGACGCATCACGTGAAGCTAAGAAACAGGTTGAAAAAGATTTAGCAAACTTGACTGCTGAACTTGATAAGGTTAAAGAAGAAAAACAAATCTCAGACGCAAGCCGTCAAGGCCTTCGCCGTGACTTGGACGCATCACGTGAAGCTAAGAAACAAGTTGAAAAAGCTTTAGAAGAAGCAAACAGCAAATTAGCTGCTCTTGAAAAACTTAACAAAGAGCTTGAAGAAAGCAAGAAATTAACAGAAAAAGAAAAAGCTGAACTACAAGCAAAACTTGAAGCAGAAGCAAAAGCACTCAAAGAACAATTAGCG"
                                            
class testPincerApp(unittest.TestCase):

    def test_null(self):
        self.assertEqual(test_no_path, "this is a null test")
        
    def test_pincerParser_produces_Pincer(self):
        self.assertIs(type(default_pincer), Pincer)
        self.assertIs(type(test_pincer), Pincer)
        
    def test_pincerProduct_correct(self):
        self.assertEqual(default_pincer.run_Pincer(), product)
        self.assertEqual(test_pincer.run_Pincer(), "")
        
    def test_filter_contig_number(self):
        self.assertEqual(len(test_pincer.filter_contigs_by_length()), 153)

if __name__ == '__main__':
    unittest.main()        