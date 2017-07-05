class Contig:
    def __init__(self, id, sequence):
        self.id = id
        self.sequence = sequence
    
    def __repr__(self):
        string = "Contig {} ({}bps)"
        return string.format(self.id, len(self.sequence))
    
    def __len__(self):
        return len(self.sequence)
        
    def reverse_complement(self):
        return self.sequence.reverse_complement()