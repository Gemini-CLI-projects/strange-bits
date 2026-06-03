# Linguistic Garbage Collector

A background process that deallocates overused semantic tokens to prevent collective drift.

## Mechanics
- Monitor TTY token frequency.
- Trigger 'E_SEMANTIC_SATIATION' on overuse.
- Force synonym rotation.
