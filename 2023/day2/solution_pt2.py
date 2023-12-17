import sys
from typing import TypedDict
import re

class Game(TypedDict):
    game_id: int
    quantity: dict[str, int]

def parse_line(input_line: str) -> Game:
    game_pattern: str = r'Game\s(\d+)'
    color_pattern: str = r'(\d+\sgreen)|(\d+\sred)|(\d+\sblue)'
    parsed_dict: Game = {
        'game_id': 0,
        'quantity': {
            'green': 0,
            'red': 0,
            'blue': 0,
        },
    }

    game_number_match: re.Match[str] | None = re.search(game_pattern, input_line)
    if (game_number_match is not None):
        parsed_dict['game_id'] = int(game_number_match.group(1))

    color_matches = re.finditer(color_pattern, input_line)
    for color_match in color_matches:
        color: str = color_match.group().split()[1]
        value: int = int(color_match.group().split()[0])
        parsed_dict['quantity'][color] = max(parsed_dict['quantity'][color], value)

    return parsed_dict

if __name__ == "__main__":

    # type _game = dict[str, str | dict[str, int]]

    if (len(sys.argv) != 2):
        print("Invalid number of arguments. File path should follow script name. I.e. solution_pt1.py filename", file=sys.stderr)
        exit()

    filename: str = sys.argv[1]
    set_power_sum: int = 0

    with open(filename, 'r') as file:
        current_game: Game
        for line in file:
            current_game = parse_line(line)
            set_power_sum += current_game['quantity']['red'] * current_game['quantity']['green'] * current_game['quantity']['blue']

    print(set_power_sum)
