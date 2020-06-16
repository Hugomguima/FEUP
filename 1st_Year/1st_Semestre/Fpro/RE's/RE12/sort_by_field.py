def sort_by_field(filename,field):
    
    
    defline = []
    
    address = open(filename)
    
    lines = address.read()
    
    lines = lines.split("\n")
    
    for line in lines:
        
        if line != "":
            
            defline.append(line)
            
            
    for i in range(len(defline[0].split(","))):
        if defline[0].split(",")[i] == field:
            index = i
            break
    sortedlines = sorted(defline[1:],key = lambda x: x.split(",")[index])
    
    sortedlines = [defline[0]] + sortedlines
    
    
    sortedstrings = "\n".join(sortedlines)
    
    
    return sortedstrings + "\n"
