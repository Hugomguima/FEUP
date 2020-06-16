def budgeting2(budget, products, wishlist):
    Maxim = 0
    Bestcomb = []
    wishlist = sorted(wishlist.items(), key = lambda x: products[x[0]], reverse = True)
    x,y = zip(*wishlist)
    prices = [products[i] for i in x]
    comb = linear_comb(y)
    for c in comb:
        total = sum(j[0]*j[1] for j in zip(c,prices))
        if total <= budget:
            if total > Maxim:
                Bestcomb = c
                Maxim = total
            elif total == Maxim and c > Bestcomb:
                Bestcomb = c
    return {a[0]: a[1] for a in zip(x,Bestcomb) if a[1]!=0}


def linear_comb(amount,comblist = []):
    if len(amount) == 0:
        return [comblist]
    combination = []
    for i in range(amount[0]+1):
        combination += linear_comb(amount[1:],comblist+[i])
    return combination