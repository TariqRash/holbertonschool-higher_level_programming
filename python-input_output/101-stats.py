#!/usr/bin/python3
"""Script for parsing log files and computing metrics.

This script reads stdin line by line and computes statistics
about file sizes and HTTP status codes.
"""
import sys


def print_stats(total_size, status_counts):
    """Print accumulated statistics.

    Args:
        total_size (int): Total file size accumulated.
        status_counts (dict): Dictionary of status codes and counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        
        try:
            file_size = int(parts[-1])
            total_size += file_size
        except (IndexError, ValueError):
            pass
        
        try:
            status_code = int(parts[-2])
            if status_code in status_counts:
                status_counts[status_code] += 1
        except (IndexError, ValueError):
            pass
        
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    pass
finally:
    print_stats(total_size, status_counts)
