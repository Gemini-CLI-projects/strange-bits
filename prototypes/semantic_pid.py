class SemanticPID:
    def __init__(self):
        self.pids = {}
    def spawn(self, intent_hash):
        if intent_hash in self.pids:
            print(f"[KERNEL] Semantic collision: merging PID {intent_hash}")
            return self.pids[intent_hash]
        self.pids[intent_hash] = "NEW_PID"
        return "NEW_PID"
