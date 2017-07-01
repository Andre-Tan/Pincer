from Bio import SeqIO
import os.path

class Sequence(Object):
    def __init__(self, filename):
        assert self.path_exists(filename), "No file!"
        self.id = filename[:filename.index(".")]
        
    def path_exists(self, filename):
        return os.path.isfile(filename)