# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 22:22:03 2018

@author: Hugo
"""

def budgeting2(budget,products,wishlist):
    
    products = sorted(products.items(), key = lambda x: x[1],reverse = True)
    products = dict(products)
    cost = 0
    n_wish = {}
    
    for i in products:
        prod_price = products[i]
        if i in wishlist:
            cost += prod_price * wishlist[i]
    
    if cost <= budget:
        return wishlist
    elif cost > budget:
        cost = 0
        
        for i in products:
            prod_price = products[i]
            
            if i in wishlist:
                for j in range(wishlist[i]):
                    if cost + prod_price <= budget:
                        
                        if i in n_wish:
                            n_wish[i] += 1
                        else:
                            n_wish.update({i:1})
                        cost += prod_price
        return n_wish
    