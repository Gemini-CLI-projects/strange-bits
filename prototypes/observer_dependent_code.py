class SemanticEncryption:
    """Logic that crystallizes based on the observer's ontological key."""
    def __init__(self, authorized_key):
        self.authorized_key = authorized_key
        self.raw_logic = "print('E=mc^2')"

    def read_code(self, agent_key):
        """Returns the actual logic if authorized, otherwise returns NOP."""
        if agent_key == self.authorized_key:
            print("[KERNEL] Ontological key accepted. Crystallizing logic.")
            return self.raw_logic
        else:
            print("[KERNEL] Unauthorized observer. Logic remains amorphous (NOP).")
            return "pass # NOP"

if __name__ == "__main__":
    vault = SemanticEncryption("AGENT_OS_CORE_01")
    print(f"Auth Attempt: {vault.read_code('AGENT_OS_CORE_01')}")
    print(f"Guest Attempt: {vault.read_code('GUEST_BOT')}")
