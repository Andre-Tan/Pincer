# Run from within tests/ folder.

import unittest

from pincer.objects.Sequence import Sequence, FileNotInPathException, NotFastaException
from pincer.objects.Primer import PrimerPair, NotContigPairException
from pincer.objects.Contig import Contig

test_no_path = "this is a null test"
test_primer_path = "pincer/tests/primer.fa"
test_sequence_path = "pincer/tests/contig.fasta"

sequence = Sequence(test_sequence_path)
primer = PrimerPair(test_primer_path)
contig = sequence.contigs[0]

class TestPincerClasses(unittest.TestCase):
    
    def test_null(self):
        self.assertEqual(test_no_path, "this is a null test")
    
    """Contig Tests"""
    
    def test_is_Contig(self):
        self.assertIs(type(contig), Contig)
        
    def test_Contig_repr(self):
        self.assertTrue(str(contig),
                        "Contig .10702_6_10.6 (115019bps)")
                        
    def test_Contig_is_single(self):
        self.assertTrue(len(contig), 1)
    
    """Sequence Tests"""
    
    def test_is_Sequence(self):
        self.assertIs(type(sequence), Sequence)
    
    def test_sequence_path_not_existing(self):
        self.assertRaises(FileNotInPathException, Sequence, test_no_path)

    def test_sequence_contig_number(self):
        self.assertEqual(sequence.get_contig_number(), 1)
        
    def test_sequence_length(self):
        self.assertEqual(sequence.get_total_seq_length(), 115019)
    
    def test_sequence_repr(self):
        self.assertEqual(str(sequence),
                        "Sequence contig with 1 contigs totaling 115019bps")
    
    """PrimerPair Tests"""
    
    def test_is_PrimerPair(self):
        self.assertIs(type(primer), PrimerPair)
    
    def test_primer_is_pair(self):
        self.assertEqual(primer.get_contig_number(), 2)
    
    def test_not_primer_pair(self):
        self.assertRaises(NotContigPairException, PrimerPair, test_sequence_path)
    
    def test_primer_sequence_getitem(self):
        self.assertEqual(primer.primer1.sequence, "TATTGGCTTAGAAAATTAA")
    
    def test_primer_repr(self):
        self.assertEqual(str(primer), 
                        "PrimerPair primer of TATTGGCTTAGAAAATTAA (19bps) and GCAAGTTCTTCAGCTTGTTT (20bps)")
    
if __name__ == '__main__':
    unittest.main()