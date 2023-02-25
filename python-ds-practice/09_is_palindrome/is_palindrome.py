def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    phrase = list(phrase.upper().replace(' ', ''))

    for l in phrase:
        if phrase[0] != phrase[-1]:

            # print(phrase[-1])
            # print(l)
            return False
        else:
            
            phrase.pop(0)
            phrase.pop(-1)
            # print(phrase)

    return True
