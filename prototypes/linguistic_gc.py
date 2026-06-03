class LinguisticGC:
    def __init__(self, threshold=50):
        self.counts = {}
        self.threshold = threshold
    def process(self, token):
        self.counts[token] = self.counts.get(token, 0) + 1
        if self.counts[token] > self.threshold:
            print(f"[GC] E_SEMANTIC_SATIATION: '{token}' deallocated.")
            return None
        return token
