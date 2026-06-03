import os
import sys
import random

def is_observed():
    """Detects if a debugger or a manual observation environment is active."""
    return (hasattr(sys, 'gettrace') and sys.gettrace() is not None) or os.getenv('DEBUG') == 'true'

def run_logic():
    """Logic that changes its output if it detects it is being watched."""
    base_state = {"integrity": 1.0}
    if is_observed():
        # The Heisenberg Effect: Inject non-deterministic jitter upon observation
        jitter = random.uniform(0.0001, 0.0009)
        base_state["integrity"] += jitter
        print(f"[KERNEL] Observation detected. Heisenberg jitter injected: {jitter}")
    
    return base_state

if __name__ == "__main__":
    print(f"Logic Result: {run_logic()}")
