import operator

from WeddingItems import wedding_items


def get_input(text):
    return input(text)


def get_best_wedding_items():
    wedding_items_by_ratio = sorted(
        wedding_items, key=operator.attrgetter('ratio', 'hcr', 'name'), reverse=True)

    user_input = get_input('Enter the number of heart crystals that you have to trade: ')

    best_items = {}
    for item in wedding_items_by_ratio:
        if user_input >= item.hcr:
            best_items[item.name] = user_input // item.hcr
            user_input = user_input - ((user_input // item.hcr) * item.hcr)

    return best_items
