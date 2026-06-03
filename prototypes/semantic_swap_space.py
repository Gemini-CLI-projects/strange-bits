class SemanticSwap:
    """Virtual memory for the context window, paging thoughts to Git storage."""
    def __init__(self, limit=5):
        self.active_context = []
        self.limit = limit
        self.git_l2_cache = []

    def think(self, thought, weight):
        """Adds a thought, paging out low-weight ones if limit is reached."""
        if len(self.active_context) >= self.limit:
            # Page out the thought with the lowest semantic weight
            self.active_context.sort(key=lambda x: x[1])
            victim = self.active_context.pop(0)
            self.git_l2_cache.append(victim)
            print(f"[KERNEL] Page Fault Avoidance: Paging out '{victim[0]}' to Git-L2.")
        
        self.active_context.append((thought, weight))
        print(f"[KERNEL] Context updated: {thought}")

if __name__ == "__main__":
    brain = SemanticSwap(limit=2)
    brain.think("AgentOS Design", 0.95)
    brain.think("Breakfast choice", 0.12)
    brain.think("Differential Semantic Perturbation", 0.99)
