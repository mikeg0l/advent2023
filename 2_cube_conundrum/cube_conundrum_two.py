total = 0

with open("input.txt", "r") as file:
    for line in file:
        max_cubes = {
            "blue": 0,
            "red": 0,
            "green": 0
        }

        game, game_content = line.split(":")
        for game_set in game_content.split(";"):
            for cubes in game_set.split(","):
                cube_amount, cube_color = cubes.strip().split(" ")
                if int(cube_amount) > max_cubes[cube_color]:
                    max_cubes[cube_color] = int(cube_amount)

        total += (max_cubes["red"] * max_cubes["green"] * max_cubes["blue"])

    print(total)

