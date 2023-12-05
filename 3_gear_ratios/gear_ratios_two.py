schematic = list()

with open("example.txt") as file:
    for line in file:
        schematic.append(line.strip())

rows = len(schematic)
cols = len(schematic[0])
total = 0

def is_g

def check_neighbours(row, col):
        if (row - 1, col + k) or \
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
        if schematic[i][j] == "*":
            print(i, j)
        j += 1
    i += 1

