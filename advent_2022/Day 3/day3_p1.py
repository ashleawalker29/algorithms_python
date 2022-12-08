def get_duplicate_item(file):
    f = open(file, 'r')

    dupes = []

    for line in f:
        # Santize line
        line = line.strip('\n')

        # Divide the line into two equal parts
        first_half = line[:len(line) // 2]
        second_half = line[len(line) // 2:]

        for char in line:
            if char in first_half and char in second_half:
                dupes.append(char)
                break

    f.close()

    return dupes

def get_priority(dupes):
    priorities = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                  'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
                  't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
                  'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35,
                  'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44,
                  'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

    total = 0
    for dupe in dupes:
        total += priorities[dupe]

    return total

def get_triples(file):
    f = open(file, 'r')
    lines = [line for line in f]
    f.close()

    groups = [[x,y,z] for x,y,z in zip(lines[0::3], lines[1::3], lines[2::3])]

    dupes = []
    for group in groups:
        for elf in group:
            for char in elf:
                if char in group[0] and char in group[1] and char in group[2]:
                    dupes.extend(char)
                    break
            break

    return dupes
