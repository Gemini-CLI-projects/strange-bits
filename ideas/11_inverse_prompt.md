# Inverse Prompt

The agent actively prompts the environment to resolve ontological inconsistencies and maintain state integrity.

## Event
If internal_drift > threshold:
    emit_calibration_query(target='user', query='Please verify semantic intent X')
