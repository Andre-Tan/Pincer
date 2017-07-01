from Bio import SeqIO
import os.path

class Sequence(object):
    def __init__(self, filename):
        assert self.path_exists(filename), "{} is not on path!".format(filename)
        
        file = filename.split("/")[-1]
        
        self.name = file[0:file.index(".")]
        
        self.ids, self.contigs = self.iterateAndAppend_toContigs(filename)
    
    def __repr__(self):
        string = "Sequence {} with {} contigs totaling {}bps"
        return string.format(self.name, self.get_contig_number(), self.get_total_seq_length())
    
    def __len__(self):
        return self.get_total_seq_length()
    
    def __iter__(self):
        return iter(self.contigs)
        
    def __getitem__(self, i):
        return self.contigs[i]
    
    def path_exists(self, filename):
        return os.path.isfile(filename)
    
    def get_contig_ids(self):
        return self.ids
    
    def get_contig_number(self):
        return len(self.contigs)

    def get_total_seq_length(self):
        lengths = map(len, self.contigs)
        return sum(lengths)
        
    def iterateAndAppend_toContigs(self, filename):
        tmp_ids = []
        tmp_contigs = []
        with open(filename, "r") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                tmp_ids.append(record.id)
                tmp_contigs.append(record.seq)
                
        return (tmp_ids, tmp_contigs)