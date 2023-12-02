from typing import Generator, Iterable, Iterator, Literal, cast
import re


CubeColor = Literal["blue"] | Literal["red"] | Literal["green"]
Cube = tuple[int, CubeColor]
GameSet = Iterable[Cube]
Game = Iterable[GameSet]

def parse_set(game_set: str) -> GameSet:
    cubes = game_set.split(",")
    for cube in cubes:
        amount, color = cube.strip().split(" ")
        amount = int(amount)
        color = cast(CubeColor, color)
        yield (amount, color)

def parse_game(row: str) -> Game:
    game_regex = re.compile(r"Game (\d+): ")
    row = re.sub(game_regex, "", row)
    return (parse_set(game_set) for game_set in row.split(";"))

MAX_BLUE = 14
MAX_GREEN = 13
MAX_RED = 12

def is_game_possible(game: Game) -> bool:
    for game_set in game:
        reds = greens = blues = 0
        for amount, color in game_set:
            match color:
                case "blue":
                    blues += amount
                case "green":
                    greens += amount
                case "red":
                    reds += amount
            if blues > MAX_BLUE or reds > MAX_RED or greens > MAX_GREEN:
                return False
    return True

def min_cubes_needed(game: Game) -> tuple[int, int, int]:
    min_red = min_green = min_blue = 0
    for game_set in game:
        for amount, color in game_set:
            match color:
                case "blue":
                    min_blue = max(min_blue, amount)
                case "green":
                    min_green = max(min_green, amount)
                case "red":
                    min_red = max(min_red, amount)
    return (min_red, min_green, min_blue)

def solution(input: list[str]) -> int:
    solution = 0
    for id, row in enumerate(input, start=1):
        game = parse_game(row)
        if is_game_possible(game):
            solution += id
    return solution

def solution_part2(input: list[str]):
    solution = 0
    for row in input:
        game = parse_game(row)
        min_red, min_green, min_blue = min_cubes_needed(game)
        power = min_red * min_green * min_blue
        solution += power
    return solution


    

if __name__ == "__main__":
    with open("day2.txt", "r") as f:
        input = f.readlines()
    print(solution(input))
    print(solution_part2(input))
