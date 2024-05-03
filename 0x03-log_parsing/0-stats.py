#!/usr/bin/python3

import sys


def print_msg(my_dict, total_size):
    '''Method to print'''

    print("File size: {}".format(total_size))
    for key, value in sorted(my_dict.items()):
        if value != 0:
            print("{}: {}".format(key, value))


total_size = 0
code = 0
count = 0
my_dict = {'200': 0,
           '301': 0,
           '400': 0,
           '401': 0,
           '403': 0,
           '404': 0,
           '405': 0,
           '500': 0
           }

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            count += 1

            if count <= 10:
                total_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in my_dict.keys()):
                    my_dict[code] += 1

            if (count == 10):
                print_msg(my_dict, total_size)
                count = 0

finally:
    print_msg(my_dict, total_size)
