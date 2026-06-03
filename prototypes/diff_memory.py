class DiffMemory:
    def __init__(self, base_model):
        self.base = base_model
        self.patches = []
    def apply_patch(self, delta):
        self.patches.append(delta)
        print(f"[MEMORY] Applied patch #{len(self.patches)}")
    def reconstruct(self):
        current = self.base
        for p in self.patches:
            current.update(p)
        return current
