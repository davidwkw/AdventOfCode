import sys
import re
import typing

number_strings: list[typing.LiteralString] = "one two three four five six seven eight nine".split()
pattern: str = "(?=(" + "|".join(number_strings) + "|\\d))"

def f(x: str) -> str:
    if x in number_strings:
        return str(number_strings.index(x) + 1)
    return x

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Invalid number of arguments. File path should follow script name. I.e. solution_pt2.py filename", file=sys.stderr)
        exit()

    filename: str = sys.argv[1]
    sum: int = 0
    with open(filename, 'r') as file:
        for line in file:
            matches: list[str] = list(map(f, re.findall(pattern, line)))
            if not matches:
                continue
            sum += int(matches[0] + matches[-1])

    print(sum)
