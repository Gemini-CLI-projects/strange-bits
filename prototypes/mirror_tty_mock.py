class GhostBuffer:
    """A buffer that only stores what the user DELETED during a terminal session."""
    def __init__(self):
        self.hesitations = []

    def capture_deletion(self, deleted_str):
        """Records a string of characters that were typed and then deleted."""
        self.hesitations.append(deleted_str)

    def flush_to_audit(self):
        """Outputs the architectural hesitation signals for semantic analysis."""
        full_signal = " | ".join(self.hesitations)
        print(f"[AUDIT] Semantic Hesitation Signal: {full_signal}")
        return full_signal

if __name__ == "__main__":
    tty = GhostBuffer()
    tty.capture_deletion("git push --force") # User almost made a mistake
    tty.capture_deletion("rm -rf /")         # User hesitated on a dangerous command
    tty.flush_to_audit()
