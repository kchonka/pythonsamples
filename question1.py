# Math question #1
# Write a function that takes two integers (x and y) and returns a 
# list of numbers between x and y that are divisible by 5 but not by 7.

import argparse

def get_nums(x, y):
    res = []

    for num in range(x, y):
        if num % 5 == 0:
            if num % 7 != 0:
                res.append(num)
    
    return res
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", help="Lower bound", type=int)
    parser.add_argument("y", help="Upper bound", type=int)
    args = parser.parse_args()
    print(get_nums(args.x, args.y))


if __name__ == "__main__":
    main()    
