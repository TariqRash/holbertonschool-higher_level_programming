#!/usr/bin/python3
"""Log parsing script that computes metrics from stdin.

This script reads log lines from stdin and computes statistics
about file sizes and HTTP status codes every 10 lines and on
keyboard interruption (CTRL+C).
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


def parse_line(line):
    """Parse a log line and extract file size and status code.

    Args:
        line (str): Log line to parse.

    Returns:
        tuple: (file_size, status_code) or (0, None) if parsing fails.
    """
    try:
        parts = line.split()
        if len(parts) < 7:
            return 0, None

        file_size = int(parts[-1])
        status_code = int(parts[-2])

        return file_size, status_code
    except (ValueError, IndexError):
        return 0, None


if __name__ == "__main__":
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                     403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            file_size, status_code = parse_line(line)

            total_size += file_size

            if status_code in status_counts:
                status_counts[status_code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_counts)
