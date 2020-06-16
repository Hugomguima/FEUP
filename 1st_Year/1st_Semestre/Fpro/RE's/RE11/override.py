def override(l1,l2):
    
    lista_1 = l2
    
    for i in l1:
        
        
        counter = 0
        for j in l2:
            
            if i[0] != j[0]:
                
                counter += 1
                
            elif j in l1:
                
                counter += 1
                
        if counter == len(l2):
            
            lista_1.append(i)
            
    lista_1 = sorted(lista_1)
    
    
    
    for i in range(len(lista_1)):
        if i >= len(lista_1)-1:
            break
        
        elif lista_1[i] == lista_1[i+1]:
            lista_1.pop(i)
    return lista_1