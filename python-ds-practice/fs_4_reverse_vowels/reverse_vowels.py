def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    s = list(s)
    vowels = 'aeiouAEIOU'

    revs = [l for l in s if l in vowels]
    revs.reverse()
    v = 0

    for i in range(0, len(s)):
        
        if s[i] in vowels:
            
            
            s[i] = revs[v]

            v = v + 1
            

    print(''.join(s))
