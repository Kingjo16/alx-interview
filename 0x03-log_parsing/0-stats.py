#!/usr/bin/python3
'''Module analizing HTTP request logs.'''
import re


def parse_log_entry(log_entry):
    '''Extracts components from a line of an HTTP request log.
    '''
    patterns = (
        r'\s*(?P<ip_address>\S+)\s*',
        r'\s*\[(?P<timestamp>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<http_request>[^"]*)"\s*',
        r'\s*(?P<status>\S+)',
        r'\s*(?P<bytes_sent>\d+)'
    )
    data = {
        'status': 0,
        'bytes_sent': 0,
    }
    log_format = '{}\\-{}{}{}{}\\s*'.format(patterns[0], patterns[1],
                                            patterns[2],
                                            patterns[3], patterns[4])
    match = re.fullmatch(log_format, log_entry)
    if match is not None:
        status = match.group('status')
        bytes_sent = int(match.group('bytes_sent'))
        data['status'] = status
        data['bytes_sent'] = bytes_sent
    return data


def display_summary(total_bytes, status_counts):
    '''Displays the aggregated statistics of the HTTP request log.
    '''
    print('File size: {:d}'.format(total_bytes), flush=True)
    for status in sorted(status_counts.keys()):
        count = status_counts.get(status, 0)
        if count > 0:
            print('{:s}: {:d}'.format(status, count), flush=True)


def accumulate_metrics(log_entry, total_bytes, status_counts):
    '''Accumulates the metrics from a given HTTP request log.

    Args:
        log_entry (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The updated total file size.
    '''
    entry_data = parse_log_entry(log_entry)
    status = entry_data.get('status', '0')
    if status in status_counts.keys():
        status_counts[status] += 1
    return total_bytes + entry_data['bytes_sent']


def main():
    '''Executes the log analyzer.
    '''
    line_count = 0
    total_bytes = 0
    status_counts = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            log_entry = input()
            total_bytes = accumulate_metrics(
                log_entry,
                total_bytes,
                status_counts,
            )
            line_count += 1
            if line_count % 10 == 0:
                display_summary(total_bytes, status_counts)
    except (KeyboardInterrupt, EOFError):
        display_summary(total_bytes, status_counts)


if __name__ == '__main__':
    main()
