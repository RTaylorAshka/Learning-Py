def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    phrase = phrase.lower()
    vowels = 'aeiou'
    vowel_dic = {l:0 for l in phrase if l in 'aeiou'}

    for l in phrase:
        if l in vowels:
            vowel_dic[l] = vowel_dic[l] + 1

    return vowel_dic