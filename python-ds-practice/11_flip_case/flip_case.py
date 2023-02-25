def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    phrase = list(phrase)
    phrase = [l.swapcase() if l.upper() == to_swap.upper() else l for l in phrase]

    # for l in phrase:
    #     print(l)
    #     if l.upper() == to_swap.upper():
    #         l.swapcase()

    return ''.join(phrase)