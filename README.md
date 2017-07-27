# Pincer: In Silico PCR for Python3

## Table of Content

1. [Introduction](##Introduction)
2. [Requirements](##Requirements)
3. [Installation](##Installation)
4. [Usage](##Usage)
5. [Output Header](##Output_Header)
6. [Contact](##Contact)

## Introduction

### Purpose

Pincer is a Python3 tool to do in silico PCR.  

Provide it with a genome assembly FASTA and primers FASTA, and it will produce amplicons where possible.

### Background

Other tools for the same purpose exist (e.g. Seqpoet in Python2 and isPcr in C), but there is none for Python3.

Although we can use both tools from Python3 by communicating with the command line, it adds unnecessary hassle to the whole process, thus Pincer.

### Developer's Opinions

Pincer and Seqpoet is similar in speed, where in the same machine they take ~2 minutes to do in silico PCR to the whole genome. IsPCR is a lot faster (~10s), but may be unfriendly to those familiar to only Python tools (or want to stay within Python environment).

If you want ease of use in Python, use Seqpoet or Pincer (depending on the version of Python you use). If you want speed and is okay with not using Python, use isPcr.

## Requirements

Currently it only needs Biopython, specifically Bio.pairwise2 and Bio.SeqIO. 

Working with Biopython >= v1.7.

## Installation

Pincer uses setup.py for easier installation. Clone the GitHub page for Pincer, and run setup.py over the command line on the directory where setup.py for Pincer is located.
The command is:

```sh
$ python3 setup.py install
``` 

You will then be able to use Pincer by calling `pincer` on the command line.

## Usage
As is, Pincer is ready to be used over the command line after installation.

The required variables are:

| Argument | Variable Type | Description |
| ------ | ------ | ------ |
| --query | FASTA | An assembled genome FASTA. Alignment will be checked within contigs; the longer the contigs, the better chance we have to find possible existing alignments. |
| --primers | FASTA | A FASTA containing primer1 and primer2 as separate records. |

Pincer uses Bio.pairwise2 local alignment function, and you can manually set the score and penalty using:  

| Argument | Variable Type | Default | Description |
| ------ | ------ | ------ | ------ |
| -match | integer | 1 | A positive integer value for when match occurs |
| -mismatch | integer | 0 | A negative integer value (or zero) for when mismatch occurs |
| -gap_open | integer | -5 | A negative integer value (or zero) for when gap open occurs |
| -gap_extend | integer | -2 | A negative integer value (or zero) for when gap extend occurs |

Pincer will filter alignments according to the set scores, and produce amplicons where primer1 and primer2 aligned in a contig within possible product length range. 
Amplicons outside of the minimum and maximum product length will not be produced. 
The variables are:

| Argument | Variable Type | Default | Description |
| ------ | ------ | ------ | ------ |
| -min_score | integer | 16 |Positive integer value for alignment to be considered as properly aligned |
| -min_product_length | integer | 500bps| Positive integer value for minimum product length | 
| -max_product_length | integer | 3000bps | Positive integer value for maximum product length | 
| -output_filename | filename | None (stdout) | A character string for if you want the amplicons sent to a file |

## Output Header

The amplicons will be coupled with a slightly modified FASTA header to show where it is produced.  
```
>contig_found direction:start_pos-end_pos:size
```
| Argument | Description |
| ------ | ------ |  
| contig_found | Record.id of the contig in the genome FASTA. |  
| direction | Sense or Antisense. FASTA sequence is by default Sense, and the reverse complement is Antisense. |
| start_pos-end_pos | Start and end position in the contig sequence. Note that in Antisense, the position produced is in the reverse complement of the contig sequence. |
| size | Size of the product amplicon (in base pairs). |

An example FASTA header produced by Pincer would look like this:
```
>contig1 Sense:113768-114904:1136bps
```

## Contact

Should you want to fill issues or contact me about anything regarding Pincer, 
you can reach me here or on my email: andre.sutanto.91@gmail.com.
