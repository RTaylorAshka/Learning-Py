def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """

    
    occurances = {item:0 for item in lst}
    
    for item in lst:
        occurances[item] = occurances[item] + 1

    if search_term not in occurances:
        return 0
    else:
        return occurances[search_term]