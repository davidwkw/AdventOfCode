import sys
import re
from collections.abc import Iterable

number_strings: Iterable[str]
pattern: str

number_strings = "one two three four five six seven eight nine".split()
pattern = "(?=(" + "|".join(number_strings) + "|\\d))"
print(pattern)

def f(x: str) -> str:
    if x in number_strings:
        return str(number_strings.index(x) + 1)
    return x

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Invalid number of arguments. File path should follow script name. I.e. solution_pt2.py filename", file=sys.stderr)
        exit()

    sum: int
    filename: str

    filename = sys.argv[1]
    sum = 0
    with open(filename, 'r') as file:
        line: str

        line = file.readline()
        while (line):
            matches: Iterable[str]
            matches = list(map(f, re.findall(pattern, line)))
            if not matches:
                continue
            sum += int(matches[0] + matches[-1])
            line = file.readline()

    print(sum)
