from Bio import SeqIO
import os.path

class Assembly:
    def __init__(self, filename):
        assert self.path_exists(filename), "File does not exist!"
            
        self.id = filename[:filename.index(".")]

        self.contigs = []
        self.contigs = self.iterateAndAppend_toAssembly(filename)

        self.type = None

    def __repr__(self):
        string = "Assembly {} of {} contigs totaling {}bps"
        return string.format(self.id, self.get_contig_number(), self.get_assembly_length())

    def __len__(self):
        return self.get_assembly_length()
		
    def __iter__(self):
        return iter(self.contigs)
        
    def __getitem__(self, i):
        return self.contigs[i]

    def get_contig_number(self):
        return len(self.contigs)

    def get_assembly_length(self):
        lengths = map(len, self.contigs)
        return sum(lengths)

    def iterateAndAppend_toAssembly(self, filename):
        with open(filename, "r") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                self.contigs.append(record.seq)
        
        return self.contigs

    def set_type(self, scheme, type):
        self.Type = (scheme, type)

    def path_exists(self, filename):
        return os.path.isfile(filename)