total = 0
with open("input.txt", "r") as file:
    for line in file:
        firstNum = None
        lastNum = None
        for char in line:
            if char.isdigit():
                if firstNum is None:
                    firstNum = char
                    lastNum = char
                else:
                    lastNum = char
        total += int(firstNum+lastNum)

print(total)
