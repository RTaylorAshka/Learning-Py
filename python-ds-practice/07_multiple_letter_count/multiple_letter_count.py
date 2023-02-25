def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    
    letter_dict = {l:0 for l in phrase}
    
    for l in phrase:
        letter_dict[l] = letter_dict[l] + 1;

    return letter_dict
