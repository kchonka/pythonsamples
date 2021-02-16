# File question #2
# Given a Comma Separated File (csv) and a column number (zero being the 
# left most column) return the sum of all the entries in that column.
# Assume that all the entries in the CSV are numbers.
# Assume also that there are no column headers.

import argparse

def read_and_get_sum(path, c):
    sum = 0

    with open(path) as csvfile:
        for line in csvfile:
            row = line.split(',')
            if len(row) > c:
                sum += int(row[c])
    return sum


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="The path of the csv file", type=str)
    parser.add_argument("c", help="The column number", type=int)
    args = parser.parse_args()

    print(read_and_get_sum(args.path, args.c))


if __name__ == "__main__":
    main()