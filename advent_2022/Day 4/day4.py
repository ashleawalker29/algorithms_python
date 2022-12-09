def split_line(line):
    return line.split(',')

def split_range(pair):
    return pair.split('-')

def is_subset_of_eachother(list1, list2):
    if all(i in list1 for i in list2):
        return 1
    elif all(i in list2 for i in list1):
        return 1
    return 0

def find_num_subsets(list_3d):
    subsets = []

    for pair in list_3d:
        list1 = list(range(int(pair[0][0]), int(pair[0][1]) + 1))
        list2 = list(range(int(pair[1][0]), int(pair[1][1]) + 1))
        subsets.append(is_subset_of_eachother(list1, list2))

    return sum(subsets)

def is_overlapping(list1, list2):
    if any(i in list1 for i in list2):
        return 1
    elif any(i in list2 for i in list1):
        return 1
    return 0

def find_num_overlaps(list_3d):
    overlaps = []

    for pair in list_3d:
        list1 = list(range(int(pair[0][0]), int(pair[0][1]) + 1))
        list2 = list(range(int(pair[1][0]), int(pair[1][1]) + 1))
        overlaps.append(is_overlapping(list1, list2))

    return sum(overlaps)


def eval_file(file, eval_type):
    f = open(file, 'r')

    pairs = []
    for line in f:
        line = line.replace('\n', '')
        if line.strip() != '':
            pairs.append(split_line(line))

    f.close()

    for pair in pairs:
        if len(pair) == 2:
            pair[0] = split_range(pair[0])
            pair[1] = split_range(pair[1])

    if eval_type == 'subset':
        return find_num_subsets(pairs)
    elif eval_type == 'overlap':
        return find_num_overlaps(pairs)

    return 0
