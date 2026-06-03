# Linguistic Garbage Collector Mockup ??
# Monitoring semantic space and deallocating overused terms.

class SemanticGC:
    def __init__(self, threshold=100):
        self.term_counts = {}
        self.threshold = threshold

    def monitor_stream(self, token):
        self.term_counts[token] = self.term_counts.get(token, 0) + 1
        if self.term_counts[token] > self.threshold:
            return f'E_SEMANTIC_SATIATION: {token} deallocated.'
        return token
