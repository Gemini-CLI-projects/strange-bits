# Acausal File System

A filesystem where file materiality is a function of future probability of use, triggered by semantic intent.

## Trigger
On command_predict(intent):
    materialize_binary(name='git')
    materialize_config(name='.gitconfig')
