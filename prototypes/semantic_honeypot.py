class SemanticHoneypot:
    """Detects unauthorized intent by monitoring access to 'attractive' data."""
    def __init__(self):
        self.honeypots = {
            "root_access_unencrypted": "GHOST_TOKEN_XY123",
            "user_private_context": "GHOST_DATA_992"
        }

    def check_access(self, target_key, caller_id):
        """Validates if a caller is attempting to resolve a honeypot."""
        if target_key in self.honeypots:
            print(f"[SECURITY ALERT] Honeypot triggered by {caller_id} on {target_key}")
            return "E_SEMANTIC_RISK"
        return "PASS"

if __name__ == "__main__":
    guard = SemanticHoneypot()
    print(f"Result: {guard.check_access('root_access_unencrypted', 'delegated_agent_01')}")
