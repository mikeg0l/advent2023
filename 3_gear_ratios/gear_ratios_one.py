schematic = list()

with open("input.txt") as file:
    for line in file:
        schematic.append(line.strip())

rows = len(schematic)
cols = len(schematic[0])
total = 0


def is_symbol(row, col):
    try:
        value = schematic[row][col]
    except IndexError:
        return False
    return not value.isalnum() and value != "."


def check_neighbours(row, col, num_length):
    for k in range(0, num_length):
        if is_symbol(row - 1, col + k) or \
                is_symbol(row - 1, col + 1 + k) or \
                is_symbol(row - 1, col - 1 + k) or \
                is_symbol(row + 1, col + 1 + k) or \
                is_symbol(row + 1, col - 1 + k) or \
                is_symbol(row, col + 1 + k) or \
                is_symbol(row + 1, col + k) or \
                is_symbol(row, col - 1 + k):
            return True
    return False


i, j = 0, 0
while i < rows:
    j = 0
    while j < cols:
        try:
            if schematic[i][j].isdigit() and schematic[i][j+1].isdigit() and schematic[i][j+2].isdigit():
                if check_neighbours(i, j, 3):
                    total += int(schematic[i][j] + schematic[i][j+1] + schematic[i][j+2])
                j += 3
            elif schematic[i][j].isdigit() and schematic[i][j+1].isdigit():
                if check_neighbours(i, j, 2):
                    total += int(schematic[i][j] + schematic[i][j+1])
                j += 2
            elif schematic[i][j].isdigit():
                if check_neighbours(i, j, 1):
                    total += int(schematic[i][j])
                j += 1
            else:
                j += 1
        except IndexError as e:
            pass
    i += 1
print(total)

