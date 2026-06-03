# Semantic PID

Process IDs defined by semantic intent rather than sequential integers, enabling context merging for identical goals.

## Deduplication
On process_spawn(intent):
    if exists(PID[intent.hash]):
        merge_context_windows(PID[intent.hash], self)
