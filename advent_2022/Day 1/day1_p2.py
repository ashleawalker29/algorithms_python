def get_top3_calories(file):
    """ Returns the total number of calories for the top 3 elves carrying the most calories. """
    elf_inventory = []
    calorie_count = 0

    # Find length of file
    f = open(file, 'r')
    file_length = 0
    for line in f:
        file_length += 1
    f.close()


    # Evaluate file contents
    f = open(file, 'r')

    current_line = 1
    for line in f:
        # Santize line
        line = line.strip('\n')

        if line:
            calorie_count += int(line)
        if not line or current_line == file_length:
            elf_inventory.append(calorie_count)
            calorie_count = 0

        current_line += 1

    f.close()

    total_calories = 0
    # Add the top 3 calorie counts together
    for i in range(3):
        if sum(elf_inventory) == 0:
            break
        if elf_inventory:
            total_calories += max(elf_inventory)
            elf_inventory.pop(elf_inventory.index(max(elf_inventory)))

    return total_calories
