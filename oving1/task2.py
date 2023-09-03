import numpy as np

def nest(c,x):
    n=len(c)
    res = c[0]
    for i in range(1,n):
        res = res*x + c[i]
    return res

def test_feil(funk):
    n = 50
    c = np.ones(n+1)
    x = 1.00001
    Px = ((x**(n+1))-1)/(x-1)
    
    error = abs(Px - funk(c, x))
    form = "{:.11e}".format(error) #fikk mye feil pga utskrift formatering
    return form

print(f'{test_feil(nest)}')
