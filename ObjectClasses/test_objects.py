import unittest
import subprocess

from Sequence import Sequence
from Primer import PrimerPair
from Assembly import Assembly

test_no_path = "this is a null test"
test_primer_path = "/home/andret1/dev/Virtue/Data/primer.fa"
test_assembly_path = "/home/andret1/dev/Virtue/Data/LD_10702_6_10.fa"
test_sequence_path = "/home/andret1/dev/Virtue/Data/contig.fasta"

sequence = Sequence(test_sequence_path)
primer = PrimerPair(test_primer_path)
assembly = Assembly(test_assembly_path)

class TestVirtueObjects(unittest.TestCase):
    
    def test_null(self):
        self.assertEqual(test_no_path, "this is a null test")
    
    """Sequence Tests"""
    
    def test_is_Sequence(self):
        self.assertIs(type(sequence), Sequence)
    
    def test_sequence_path_not_existing(self):
        self.assertRaises(AssertionError, Sequence, test_no_path)
    
    def test_sequence_ids_type(self):
        self.assertIs(type(sequence.get_contig_ids()), list)
    
    def test_sequence_ids(self):
        self.assertEqual(sequence.get_contig_ids()[0], ".10702_6_10.6")
        
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
    
    def test_primer_sequence_getitem(self):
        self.assertEqual(primer[0], "TATTGGCTTAGAAAATTAA")
    
    def test_primer_repr(self):
        self.assertEqual(str(primer), 
                        "PrimerPair primer of TATTGGCTTAGAAAATTAA (19bps) and GCAAGTTCTTCAGCTTGTTT (20bps)")
    
    """Assembly Tests"""
    
    def test_is_Assembly(self):
        self.assertIs(type(assembly), Assembly)
    
    def test_assembly_repr(self):
        self.assertEqual(str(assembly), 
                        "Assembly LD_10702_6_10 with 33 contigs totaling 1869817bps")
    
if __name__ == '__main__':
    unittest.main()