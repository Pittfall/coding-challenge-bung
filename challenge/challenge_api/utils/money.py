def num_from_currency(value: str) -> int:
    '''
    Converts a currency string with a suffix (e.g., 'M' for million, 'K' for thousand)
    into an integer.
    '''

    multipliers = {'M': 1000000, 'K': 1000}
    suffix = value[-1]
    multiplier = multipliers.get(suffix)

    if multiplier is None:
        raise ValueError('Invalid currency format')

    number_output = float(value[1:-1])
    return int(number_output * multiplier)
    