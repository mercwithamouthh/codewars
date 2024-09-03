def past(h, m, s):
    # Convert hours, minutes, and seconds to milliseconds
    hours_in_ms = h * 60 * 60 * 1000
    minutes_in_ms = m * 60 * 1000
    seconds_in_ms = s * 1000

    # Calculate total time in milliseconds since midnight
    total_ms = hours_in_ms + minutes_in_ms + seconds_in_ms

    return total_ms
