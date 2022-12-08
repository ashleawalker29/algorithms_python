def get_calories(file):
    """ Returns the number of calories for the elf carrying the most calories. """
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

    return max(elf_inventory or [0])
