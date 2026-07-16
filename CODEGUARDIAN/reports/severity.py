def get_severity(
    value,
    warning_threshold,
    critical_threshold
):

    if value >= critical_threshold:

        return "🔴 CRITICAL"

    elif value >= warning_threshold:

        return "🟡 WARNING"

    return "🟢 OK"