from collections import defaultdict
from pincer.objects.aligned import Aligned

class Aligner:
    
    def __init__(self, sequence, primer, k, threshold=4):
        self.sequence = sequence
        self.primer = primer
        
        self.primer_length = len(primer)
        
        self.k = k
        self.threshold = threshold
        
    def hash_primer_end(self):
        pos_dict = defaultdict(int)
        
        start = self.primer_length-self.k
        end = self.primer_length
        
        pos_dict[str(self.primer)[start:end]]
        return pos_dict

    def find_in_sequence(self, dictionary):
        to_run = len(self.sequence)-self.k+1
        to_align = []
        
        for i in range(to_run):
            if self.sequence[i:i+self.k] in dictionary:
                start, end = i+self.k-self.primer_length, i+self.k
                to_align.append(Aligned(self.sequence[start:end], start, end))
        
        
        print("HEREHERE", to_align) 
        
        return to_align
    
    def align(self, aligned, threshold=10):
        assert len(aligned.seq) == len(self.primer), "Length does not match between aligned and primer"
        score = 0
        threshold = threshold
        
        for i in range(len(aligned.seq)):
            if aligned.seq[i] == self.primer[i]:
                score += 1
            else:
                threshold -= 1 
            
            if threshold <= -1:
                break
        
        return (aligned.seq, self.primer, score, aligned.start, aligned.end)
    
    def main(self):
        dictionary = self.hash_primer_end()
        matches = self.find_in_sequence(dictionary)
        
        return [self.align(match) for match in matches]