def cut(filename,delimiter,field):
    
    resultado = []
    
    resultline =  []
    
    deflines =   []
    
    f = open(filename)
    
    lines =  f.read()
    
    lines =  lines.split("\n")
    
    for line in lines:
        
        if line != "":
            
            
            deflines.append(line)
    if type(field) == int:
        
        for line in  deflines:
            
            parts =  line.split(delimiter)
            
            resultado +=  [parts[field-1]]
            
            
        resultado = "\n".join(resultado)
        
    elif type(field) == list:
        for line in deflines:
            
            parts = line.split(delimiter)
            
            resultline = []
            for idx in field:
                resultline += [parts[idx-1]]
                
            resultado += [delimiter.join(resultline)]
            
        resultado = "\n".join(resultado)
    return resultado
