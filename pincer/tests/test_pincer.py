import unittest

from pincer.utility.pincer import Pincer
from pincer.tests.test_data import *

default_pincer = Pincer(test_sequence_path, test_primer_path, min_3_end=10, threshold=20)
test_pincer = Pincer(test_seq_rc_path, test_primer_path,
                    min_product_length=500, output_filename=None)
test_pincer5000 = Pincer(test_seq_rc_path, test_primer_path,
                        min_product_length=5000, output_filename=None)                                

class testPincerApp(unittest.TestCase):

    def test_null(self):
        self.assertEqual(test_no_path, "this is a null test")
        
    def test_pincerParser_produces_Pincer(self):
        self.assertIs(type(default_pincer), Pincer)
        self.assertIs(type(test_pincer), Pincer)
        
    def test_pincerProduct_correct_default(self):
        self.assertEqual(default_pincer.run_Pincer(), def_product)
    
    def test_pincerProduct_correct_rc(self):
        self.assertEqual(test_pincer.run_Pincer(), test_product)
        
    def test_pincerProduct_correct_rc5000(self):
        self.assertEqual(test_pincer5000.run_Pincer(), test_product_min5000)
        
    def test_filter_contig_number(self):
        self.assertEqual(len(test_pincer.filter_contigs_by_length()), 1)

if __name__ == '__main__':
    unittest.main()        