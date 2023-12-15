import sys
import re

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Invalid number of arguments. File path should follow script name. I.e. solution_pt1.py filename", file=sys.stderr)
        exit()

    sum: int
    filename: str

    filename = sys.argv[1]
    sum = 0
    with open(filename, 'r') as file:
        line: str

        line = file.readline()
        while (line):
            sum_string: str
            sum_string = ''
            match = re.search(r"\d", line)
            if match == None:
                continue
            sum_string += match.group()
            line = line[::-1]
            match = re.search(r"\d", line)
            sum_string += match.group()
            sum += int(sum_string)
            line = file.readline()

    print(sum)
