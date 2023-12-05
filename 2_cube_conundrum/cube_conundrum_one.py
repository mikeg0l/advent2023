cube_limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total = 0

with open("input.txt", "r") as file:
    for line in file:
        possible = True
        game, game_content = line.split(":")
        for game_set in game_content.split(";"):
            for cubes in game_set.split(","):
                cube_amount, cube_color = cubes.strip().split(" ")
                if int(cube_amount) > cube_limits[cube_color]:
                    possible = False

        if possible:
            total += int(game.split(" ")[1])

    print(total)

