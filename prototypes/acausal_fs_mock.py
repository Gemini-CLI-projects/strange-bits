class AcausalFS:
    """A filesystem where file materiality depends on intent probability."""
    def __init__(self):
        self.latent_files = {
            "git": {"prob": 0.0, "content": "BINARY_EXECUTABLE"},
            ".gitconfig": {"prob": 0.0, "content": "USER_CONFIG"}
        }

    def update_intent(self, keystrokes):
        """Updates the probability of file materiality based on TTY buffer."""
        if "git" in keystrokes:
            self.latent_files["git"]["prob"] = 0.95
            self.latent_files[".gitconfig"]["prob"] = 0.90
            print("[KERNEL] Causality activated. Materializing Git binaries.")

    def ls(self):
        """Returns only the files that have crossed the materiality threshold."""
        return [f for f, data in self.latent_files.items() if data["prob"] > 0.5]

if __name__ == "__main__":
    fs = AcausalFS()
    print(f"Empty FS: {fs.ls()}")
    fs.update_intent("git checkout main")
    print(f"Materialized FS: {fs.ls()}")
