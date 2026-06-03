class EntropyScheduler:
    def schedule(self, entropy):
        if entropy > 0.8:
            print("[SCHEDULER] High entropy detected. Throttling process.")
            return "DEFERRED"
        return "CRITICAL"
