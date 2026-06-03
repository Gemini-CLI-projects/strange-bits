class InversePrompter:
    def check_integrity(self, state):
        if not state.get("consistent"):
            print("[KERNEL] Calibration required. Emitting inverse prompt...")
            return "QUERY: Please verify your last semantic intent."
        return "OK"
