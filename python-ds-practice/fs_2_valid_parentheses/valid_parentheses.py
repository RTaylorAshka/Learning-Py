def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    parens = list(parens)
    
    

    # print(parens)
    

    if len(parens) % 2 != 0:
        return False
    
    for i in range(0, len(parens)):

        if parens[0] != '(':
            return False
        
        
        

        if parens[0] + parens[1] == '()':
            parens.pop(0)
            parens.pop(0)
            print('in')
            if len(parens) == 0:
                return True

        elif parens[0] + parens[-1] == '()':
            parens.pop(0)
            parens.pop(len(parens) - 1)
            print('out')
            if len(parens) == 0:
                return True
        
        

    return True



            