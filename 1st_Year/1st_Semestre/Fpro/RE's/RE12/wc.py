def wc(filename):
    word = []
    
    characterss = 0
    
    f = open(filename, "r")
    
    l = f.readlines()
    
    
    for line in l:
        word += line.split()
        
        for character in line:
            
            characterss += 1
            
    return (len(l), len(word), characterss)