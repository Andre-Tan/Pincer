class Alignment:
    def __init__(self, align_tup):
        assert len(align_tup) == 5, "Are you sure it is alignment output?"
        subject, aligned, score, start, end = align_tup
        
        self.subject = subject
        self.aligned = aligned
        self.score = score
        self.Positions = (start, end)
        
        
    def filter_by_score(self, score):
        return self.score >= score