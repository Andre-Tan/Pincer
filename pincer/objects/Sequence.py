from Bio import SeqIO
from os import path
from sys import exit

from pincer.objects.Contig import Contig

class FileNotInPathException(Exception):
    pass

class NotFastaException(Exception):
    pass
    
class Sequence(object):
    def __init__(self, filename):
        self.file, self.name = self.get_file_and_name(filename)
        
        self.contigs = self.iterateAndAppend_toContigs(filename)
    
    def __repr__(self):
        string = "Sequence {} with {} contigs totaling {}bps"
        return string.format(self.name, self.get_contig_number(), self.get_total_seq_length())
    
    def __len__(self):
        return self.get_total_seq_length()
    
    def __iter__(self):
        return iter(self.contigs)
        
    def __getitem__(self, i):
        return self.contigs[i]

    def get_contig_number(self):
        return len(self.contigs)

    def get_total_seq_length(self):
        lengths = map(len, self.contigs)
        return sum(lengths)
    
    def get_file_and_name(self, filename):
        if not path.isfile(filename):
            raise FileNotInPathException("{} is not a file!".format(filename))
            exit(1)
        
        file = filename.split("/")[-1]
        type = file[file.index(".")+1:]
        name = file[0:file.index(".")]
        
        if type not in ["fasta", "fa"]:
            raise NotFastaException("{} is not a fasta file!".format(filename))
            exit(1)
        
        return file, name
        
    def iterateAndAppend_toContigs(self, filename):
        tmp_contigs = []
        
        with open(filename, "r") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                tmp_contigs.append(Contig(record.id, record.seq))
        
        return tmp_contigs