def print_upper_words(words, must_start_with):
    check = ''
    for letter in must_start_with:
        check = check + letter.upper() + ' '

        
    for word in words:
        if word[0].upper() in check:
            print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})