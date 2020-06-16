def parse(filename):
    resultado = ""
    
    file = open(filename)
    
    lines = file.readlines()
    
    for line in lines:
        
        words = line.split()
        
        
        for word in words:
            
            if word == "(":
                
                resultado += word
                
            else:
                resultado += word + ","
    return eval("(" + resultado + ")")