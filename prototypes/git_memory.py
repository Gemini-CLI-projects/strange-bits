class GitMemory:
    def __init__(self):
        self.commits = []
    def commit(self, thought):
        self.commits.append(thought)
        print(f"[GIT] New commit: {thought[:20]}...")
    def rebase(self):
        print("[GIT] rebasing --force: identity recalculated.")
