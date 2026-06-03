# Mirror-Only TTY

Surfaces architectural hesitation by only displaying deleted characters from the TTY buffer.

## Implementation
# Capture VK_BACK events and echo to ghost_buffer
# On ENTER: flush ghost_buffer to audit_log
