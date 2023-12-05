total = 0

valid_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

with open("input.txt", "r") as file:
    for line in file:
        firstNum = None
        lastNum = None
        for index, char in enumerate(line):
            if char.isdigit():
                if firstNum is None:
                    firstNum = char
                    lastNum = char
                else:
                    lastNum = char
            else:
                for digit in valid_digits.keys():
                    if line[index:].startswith(digit):
                        if firstNum is None:
                            firstNum = valid_digits[digit]
                            lastNum = valid_digits[digit]
                        else:
                            lastNum = valid_digits[digit]
        total += int(firstNum+lastNum)

print(total)