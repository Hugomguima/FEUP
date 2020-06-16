def triplet(atuple):
    
    result = ()
    c1 = -1
    c2 = -1
    c3 = -1

    for n1 in atuple:
        c1 += 1
        c2 = -1
        c3 = -1
        for n2 in atuple:
            c2 += 1
            c3 = -1
            for n3 in atuple:
                c3 +=1
                if (n1 + n2 + n3) == 0:
                    if atuple[c1] != atuple[c2] and  atuple[c1] != atuple[c3] and atuple[c2] != atuple[c3]:    
                        result = (n1, n2, n3)
                        return result
    
    return result
    
                
        