class OntoFirewall:
    def __init__(self, host_ontology):
        self.host = host_ontology
    def check_drift(self, foreign_ontology):
        drift = sum(1 for k in foreign_ontology if k not in self.host)
        if drift > 2:
            print("[FIREWALL] E_ONTOLOGICAL_INCOMPATIBILITY: Bridge blocked.")
            return False
        return True
