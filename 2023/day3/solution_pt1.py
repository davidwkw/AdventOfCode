import sys

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Invalid number of arguments. File path should follow script name. I.e. solution_pt1.py filename", file=sys.stderr)
        exit()

    filename: str = sys.argv[1]
    sum: int = 0
    file = open(filename, 'r')
    content_list: list[str] = file.read().splitlines()
    digit_coordinates: set[tuple[int, int]] = set()

    for row_index, line in enumerate(content_list):
        for column_index, character in enumerate(line):
            if character == '.' or character.isdigit():
                continue
            for cr_index in [row_index - 1, row_index, row_index + 1]:
                for cc_index in [column_index - 1, column_index, column_index + 1]:
                    if cc_index < 0 or cc_index >= len(content_list[cr_index]) or cr_index < 0 or cr_index >= len(content_list) or not content_list[cr_index][cc_index].isdigit():
                        continue
                    while cc_index > 0 and content_list[cr_index][cc_index - 1].isdigit():
                        cc_index -= 1
                    digit_coordinates.add((cr_index, cc_index))

    for row_coord, column_coord in digit_coordinates:
        value: str = ''
        while column_coord < len(content_list[row_coord]) and content_list[row_coord][column_coord].isdigit():
            value += content_list[row_coord][column_coord]
            column_coord += 1
        sum += int(value)

    print(sum)
