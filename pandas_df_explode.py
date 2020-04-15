# Splitting (Exploding) a column into multiple rows

import pandas as pd

def printobj(obj) :
    print(type(obj))
    print(obj)
    print('-'*45)
    
if 0:
    df = pd.DataFrame(
         {'Menu' : ['Drinks', 'Food', 'At home Coffee'],
          'Item' : [['Coffees', 'Teas', 'Beverages'],
                    ['Bakery', 'Snacks', 'Yogurt'],
                    ['Whole Bean', 'Instant']] } )

    printobj(df)
    df = df.explode('Item')
    printobj(df)
    df.index = pd.RangeIndex(len(df))
    printobj(df)

if 0:
    import numpy as np
    
    midx1 = pd.MultiIndex.from_product([list('AB'), list('ab')])
    midx2 = pd.MultiIndex.from_product([list('MF'), list('cd')])
    df = pd.DataFrame(
            [[1,[1,2,3],3,4], [9,[2,3],10,11],
             [4,[1,3],6,7], [1,[7,8,9],10,15]],
             index = midx1, columns = midx2)  
    printobj(df)
    df = df.explode(('M', 'd'))
    printobj(df)
