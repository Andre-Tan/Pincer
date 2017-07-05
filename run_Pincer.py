import argparse
from Utilities.Pincer import Pincer

def buildParser():
    parser = argparse.ArgumentParser(description="Pincer - In Silico PCR for Python3")
    
    parser.add_argument("--query", required=True, type=str,
                        help="Path to FASTA of target assembly to PCR against.")               
    parser.add_argument("--primers", required=True, type=str,
                        help="Path to FASTA of primer1 and primer2 of PCR protocol.")
    
    parser.add_argument("-match", default=1, type=int,
                        help=("Integer value of match score in alignment. Default=1."))
    parser.add_argument("-mismatch", default=0, type=int,
                        help=("Integer value of mismatch penalty in alignment. Default=0."))
    parser.add_argument("-gap_open", default=-5, type=int,
                        help=("Integer value of gap open penalty in alignment. Default=-5."))
    parser.add_argument("-gap_extend", default=-2, type=int,
                        help=("Integer value of gap extend penalty in alignment. Default=-2."))
                        
    parser.add_argument("-min_score", default=16, type=int,
                        help="Minimum alignment score to consider as properly aligned. Default=16")
    parser.add_argument("-min_product_length", default=500, type=int,
                        help="Minimum PCR product length. Default=500bps")
    parser.add_argument("-max_product_length", default=3000, type=int,
                        help="Maximum PCR product length. Default=3000bps")
    parser.add_argument("-output_filename", default=None,
                        help="Name of filename to output PCR products.\n" 
                            "Default=None, will print to command line.")
    
    return parser

def generatePincerObj(query, primers, match=1, mismatch=0, 
                        gap_open=-5, gap_extend=-2, min_score=16, 
                        min_product_length=500, max_product_length=3000, 
                        output_filename=None):
    
    """
    Generator of Pincer object within Python. 
    The equivalent of main() in command line. 
    """
    
    args_string = ("--query {} --primers {} -match {} -mismatch {} "
                    "-gap_open {} -gap_extend {} -min_score {} "
                    "-min_product_length {} -max_product_length {} -output_filename {}")
    
    arguments = args_string.format(query, primers, match, mismatch, 
                                    gap_open, gap_extend, min_score,
                                    min_product_length, max_product_length,
                                    output_filename).split()
                                    
    parser = buildParser()
    args = parser.parse_args(arguments)
    
    penalty_tuple = args.match, args.mismatch, args.gap_open, args.gap_extend
    penalty_tuple = tuple(map(int, penalty_tuple))
    
    pincer = Pincer(args.query, args.primers, 
                    penalty_tuple, args.min_score, 
                    args.min_product_length, args.max_product_length, 
                    args.output_filename)
    
    return pincer
    
def main():
    parser = buildParser()
    args = parser.parse_args()
    
    penalty_tuple = (args.match, args.mismatch, args.gap_open, args.gap_extend)
    penalty_tuple = tuple(map(int, penalty_tuple))
    
    pincer = Pincer(args.query, args.primers, 
                    penalty_tuple, args.min_score, 
                    args.min_product_length, args.max_product_length, 
                    args.output_filename)
    
    pincer.run_Pincer()

if __name__ == "__main__":
    main()