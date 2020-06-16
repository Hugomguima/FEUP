def flatten(alist):   
    value = []  
    for element in alist:
        if type(element) == list:
            value += flatten(element)
        else:
            value.append(element)
    return value
#print(flatten(['Hello', [2, [[], False]], [True]]))
#print(flatten([[]]))