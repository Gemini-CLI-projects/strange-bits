# Heisenberg Debugger

Forces the developer to write robust code by introducing controlled non-determinism upon observation.

## Logic
If observed_by(developer):
    randomize_ptr_offsets()
    inject_jitter(latency=5ms)
