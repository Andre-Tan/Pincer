import sys

class wrongAlignmentLengthException(Exception):
    pass
    
class Alignment:
    def __init__(self, align_tup):
        if len(align_tup) != 5:
            raise wrongAlignmentLengthException("Wrong formatting for Alignment!")
            sys.exit(1)
        
        subject, aligned, score, start, end = align_tup
        
        self.subject = subject
        self.aligned = aligned
        self.score = score
        self.Positions = (start, end)
        
    def filter_by_score(self, score):
        return self.score >= score