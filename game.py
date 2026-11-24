

from copy import copy
import random


POSSIBLE_COLORS = (
    "BLU",
    "RED",
    "GRE",
    "WHI",
    "YEL",
    "BRO",
    "BLA",
    "ORA"
)


class Row:

    def __init__(self, colors, result):
        self.colors = colors
        self.result = result


class Game:

    def __init__(self, solution: tuple | None = None, rows: list | None = None):
        self.solution = solution if solution is not None else self.random_solution()
        self.rows = list(rows) if rows is not None else []
        self.over = False
        self.row_length = 4

    def copy(self):
        return Game(self.solution, self.rows)

    def add_row(self, row: Row):
        self.rows.append(row)

    def play_colors(self, colors):
        result = self.calculate_result(copy(colors))
        if result["black"] == self.row_length:
            self.over = True
        self.add_row(Row(tuple(colors), result))

    def calculate_result(self, colors):

        result = {
            "black": 0,
            "white": 0
        }

        solution_copy = list(self.solution)

        for i in range(len(solution_copy)):
            if solution_copy[i] == colors[i] and colors[i]:
                result["black"] += 1
                colors[i] = None
                solution_copy[i] = None

        for color_guess in colors:
            if color_guess and color_guess in solution_copy:
                result["white"] += 1
                colors[colors.index(color_guess)] = None
                solution_copy[solution_copy.index(color_guess)] = None

        return result

    def random_solution(self):
        return (
            random.choice(POSSIBLE_COLORS),
            random.choice(POSSIBLE_COLORS),
            random.choice(POSSIBLE_COLORS),
            random.choice(POSSIBLE_COLORS)
        )

    def __str__(self):
        s = "GAME\n"
        for row in self.rows:
            s += f"{row.colors}  |  {row.result}\n"
        return s


def ui(game: Game):
    while True:
        print(game)
        next_guess = []
        while len(next_guess) < game.row_length:
            print("Your current guess:", next_guess)
            color = input("Color? (\"RESTART\" to restart)")
            if color in POSSIBLE_COLORS:
                next_guess.append(color)
            elif color == "RESTART":
                next_guess = []
            elif color == "SOL":
                print(game.solution)

        print("Your current guess:", next_guess)
        ready = input("Send it? (enter for yes)")
        if not ready:  # Meaning ready (naturally)
            game.play_colors(next_guess)
            if game.over:
                print("You win!")
                print(game)
                break
        else:
            print("Didn't play.")


def main():
    ui(Game())


if __name__ == "__main__":
    main()
