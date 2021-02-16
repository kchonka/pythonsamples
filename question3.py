# Math question #3:
# Write a function that takes two integers (x and b) as inputs and 
# returns a string that represents the number x in base b.
# Example 1: if x=5 and b=2 then the function will return "101"
# Example 2: if x=5 and b=3 then the function will return "12"

# Solutions work up to base-36.

import argparse

def convert(x, b):
    if b > 36:
        print("Cannot convert to base larger than base-36, please try again.")
        exit(1)

    # Alphabetic convertions for reprsentation in larger bases:
    data = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 
            15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J',
            20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 
            25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T',
            30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y',
            35: 'Z'}

    stack = [] # to temporarily store the answer in reverse order

    while x != 0:
        remainder = x % b 
        if remainder >= 10:
            stack.append(data[remainder])
        else:
            stack.append(remainder)
        x = int((x - remainder) / b)
    
    # Reverse the stack:
    result = ''
    while stack:
        result += str(stack.pop())
    
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", help="The number to be converted", type=int)
    parser.add_argument("b", help="The base used for conversion", type=int)
    args = parser.parse_args()

    print(convert(args.x, args.b))


if __name__ == "__main__":
    main()