import re


def is_anagram(phrase, anagram):
    if not phrase or not anagram:
        return 'Cannot find an anagram from an empty string.'

    normalized_phrase = sorted(re.sub(r'[^\w\s]', '', phrase.lower().replace(' ', '')))
    normalized_anagram = sorted(re.sub(r'[^\w\s]', '', anagram.lower().replace(' ', '')))

    compared_characters = set(normalized_phrase) - set(normalized_anagram)
    if compared_characters:
        return 'Partial anagram.'
    return 'Full anagram.'
