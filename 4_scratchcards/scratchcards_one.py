total = 0

with open("input.txt", "r") as file:
    for card in file:
        points = 0
        first_match = True
        card_info, content = card.split(":")
        winning_numbers, my_numbers = content.split("|")

        winning_numbers = list(filter(None, winning_numbers.strip().split(" ")))
        my_numbers = list(filter(None, my_numbers.strip().split(" ")))

        for my_number in my_numbers:
            for winning_number in winning_numbers:
                if my_number == winning_number:
                    if first_match:
                        points += 1
                        first_match = False
                    else:
                        points *= 2
        total += points

print(total)

