# Kata: https://www.codewars.com/kata/55b3425df71c1201a800009c

from statistics import mean, median

def str_to_sec(time_str):
    """
    Converts a time string in the format 'hh|mm|ss' to total seconds.
    """
    h, m, s = map(int, time_str.split("|"))
    return h * 3600 + m * 60 + s

def sec_to_hms(seconds):
    """
    Converts total seconds back to 'hh|mm|ss' format.
    """
    h, remainder = divmod(seconds, 3600)
    m, s = divmod(remainder, 60)
    return f"{h:02}|{m:02}|{s:02}"

def stat(time_str):
    """
    Computes and returns the Range, Average, and Median of a given list of times.
    The input is a string of times separated by commas in 'hh|mm|ss' format.
    """
    if not time_str:
        return ""
    
    # Convert time strings to seconds
    times = [str_to_sec(i) for i in time_str.replace(",", "").split()]
    
    # Calculate statistics
    range_t = max(times) - min(times)
    average_t = int(mean(times))
    median_t = int(median(times))
    
    # Format output
    return (f"Range: {sec_to_hms(range_t)} "
            f"Average: {sec_to_hms(average_t)} "
            f"Median: {sec_to_hms(median_t)}")
