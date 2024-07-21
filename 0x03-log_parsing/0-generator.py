#!/usr/bin/python3
'''A script that generates random HTTP request logs.'''
import random
import sys
import datetime
from time import sleep


for _ in range(10000):
    sleep(random.random())
    ip_address = "{}.{}.{}.{}".format(
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255)
    )
    timestamp = datetime.datetime.now().strftime('%d/%b/%Y:%H:%M:%S %z')
    request_line = "GET /projects/1216 HTTP/1.1"
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    file_size = random.randint(1, 1024)
    
    log_entry = '{} - [{}] "{}" {} {}\n'.format(
        ip_address, timestamp, request_line, status_code, file_size
    )
    sys.stdout.write(log_entry)
    sys.stdout.flush()
