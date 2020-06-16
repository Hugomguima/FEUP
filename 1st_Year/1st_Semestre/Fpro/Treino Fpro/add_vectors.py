def add_vectors(vector1,vector2):
    
    vector3 = []
    for i in range(len(vector1)):
        
        total = vector1[i] + vector2[i]
        vector3.append(total)
    
    return vector3

print(add_vectors([1, 2, 1], [1, 4, 3]))