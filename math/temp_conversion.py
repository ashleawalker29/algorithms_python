def celsius_to_fahrenheit(n):
    if isinstance(n, float):
        return round_traditional(n * 9.0 / 5.0 + 32, 2)
    return 'Not a valid temperature.'


def fahrenheit_to_celsius(n):
    if isinstance(n, float):
        return round_traditional((n - 32.0) * 5.0 / 9.0, 2)
    return 'Not a valid temperature.'


def round_traditional(val, digits):
    return round(val + 10**(-len(str(val)) - 1), digits)
