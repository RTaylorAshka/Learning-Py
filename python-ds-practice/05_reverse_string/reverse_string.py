def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

   
    if type(phrase) is str:
        reverseMe = list(phrase)
        reverseMe.reverse()
        print(''.join(reverseMe))
