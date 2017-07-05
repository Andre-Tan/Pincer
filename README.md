# Pincer: In Silico PCR for Python3

Pincer is a Python3 tool to do in silico PCR.  

Provide it with a genome assembly FASTA and primers FASTA, and it will produce amplicons where possible.

## Requirements

Currently it only needs Bio.pairwise2 and Bio.SeqIO. Version will be updated.

## Usage
As is, Pincer is ready to be used over the command line, but you may need to do 
`python3 run_Pincer.py --query <your assembly FASTA> --primers <your primers FASTA>`
(setup.py will be made).

The required variables are:  
`--query <FASTA>`: an assembled genome FASTA. Alignment will be checked within contigs; the longer the contigs, the better chance we have to find possible existing alignments.  
`--primers <FASTA>`: a FASTA containing primer1 and primer2 as separate records.  

Pincer uses Bio.pairwise2 local alignment function, and you can manually set the score and penalty using:  
`-match <int>`: a positive integer value for when match occurs. Default: 1  
`-mismatch <int>`: a negative integer value (or zero) for when mismatch occurs. Default: 0  
`-gap_open <int>`: a negative integer value (or zero) for when gap open occurs. Default: -5  
`-gap_extend <int>`: a negative integer value (or zero) for when gap extend occurs. Default: -2  

Pincer will filter alignments according to the set scores, and produce amplicons where primer1 and primer2 aligned in a contig within possible product length range. 
Amplicons outside of the minimum and maximum product length will not be produced. 
The variables are:  
`-min_score <int>`: a positive integer value for alignment to be considered as properly aligned. Default: 16.  
`-min_product_length <int>`: a positive integer value for minimum product length. Default: 500bps.  
`-max_product_length <int>`: a positive integer value for maximum product length. Default: 3000bps.  

`-output_filename <filename>`: a character string for if you want the amplicons sent to a file. Default: None, will print to command line.  

## Output Header

The amplicons will be coupled with a slightly modified FASTA header to show where it is produced.  
`>contig_found direction:start_pos-end_pos:size`
  
`contig_found`: Record.id of the contig in the genome FASTA.  
`direction`: Sense or Antisense. FASTA sequence is by default Sense, and the reverse complement is Antisense.  
`start_pos-end_pos`: Start and end position in the contig sequence. Note that in Antisense, the position produced is in the reverse complement of the contig sequence.  
`size`: Size of the product amplicon (in base pairs).  

## To Be Updated

1. Need more unittest.
2. Need an easy setup.py.

## Contact

Should you want to fill issues or contact me about anything regarding Pincer, 
you can reach me here or on my email: andre.sutanto.91@gmail.com.
