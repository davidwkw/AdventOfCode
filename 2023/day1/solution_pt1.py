import sys
import re

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Invalid number of arguments. File path should follow script name. I.e. solution_pt1.py filename", file=sys.stderr)
        exit()

    filename: str = sys.argv[1]
    sum: int = 0
    with open(filename, 'r') as file:
        for line in file:
            sum_string: str = ''
            match = re.search(r"\d", line)
            if match == None:
                continue
            sum_string += match.group()
            line = line[::-1]
            match = re.search(r"\d", line)
            if match == None:
                continue
            sum_string += match.group()
            sum += int(sum_string)

    print(sum)
