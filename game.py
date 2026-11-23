

import random


possible_colors = [
    "BLU",
    "RED",
    "GRE",
    "WHI",
    "YEL",
    "BRO",
    "BLA"
    "ORA"
]


class Row:

    def __init__(self, colors, result):
        self.colors = colors
        self.result = result


class Game:

    def __init__(self):
        self.solution = self.random_solution()
        self.rows = []

    '''def __init__(self, solution: tuple):
        self.solution = solution

    def __init__(self, solution: tuple, rows):
        self.solution = solution
        self.rows = rows'''

    def copy(self):
        return Game(self.solution, self.rows)

    def add_row(self, row: Row):
        self.rows.append(row)

    def play_colors(self, colors):
        result = self.calculate_result(colors)
        self.add_row(Row(tuple(colors), result))

    def calculate_result(self, colors):

        result = {
            "black": 0,
            "white": 0
        }

        solution_copy = list(self.solution)

        for i in range(len(solution_copy)):
            if solution_copy[i] == colors[i] and colors[i]:
                print(
                    f"Black, {solution_copy[i]}. c: {colors}, s_c: {solution_copy}")
                result["black"] += 1
                colors[i] = None
                solution_copy[i] = None

        for color_guess in colors:
            if color_guess and color_guess in solution_copy:
                result["white"] += 1
                colors[colors.index(color_guess)] = None
                solution_copy.remove(color_guess)
                print(
                    f"White, {color_guess}. c: {colors}, s_c: {solution_copy}")

        return result

    def random_solution(self):
        return (
            random.choice(possible_colors),
            random.choice(possible_colors),
            random.choice(possible_colors),
            random.choice(possible_colors)
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
        while len(next_guess) < 4:
            print("Your current guess:", next_guess)
            color = input("Color? (\"RESTART\" to restart)")
            if color in possible_colors:
                next_guess.append(color)
            elif color == "RESTART":
                next_guess = []
            elif color == "SOL":
                print(game.solution)

        print("Your current guess:", next_guess)
        ready = input("Send it? (enter for yes)")
        if not ready:  # Meaning ready (naturally)
            game.play_colors(next_guess)
        else:
            print("Didn't play.")


def main():
    ui(Game())


if __name__ == "__main__":
    main()
