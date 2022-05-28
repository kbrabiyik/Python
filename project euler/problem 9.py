# a<b<c
# a**2 + b**2 = c**2
# a+b+c =1000
# abc?

for a in range(3,1000): # alt büyüdüğünde üst oto büyüdüğüne göre başlangıcı a dan al
    for b in range(a+1,999):
        cSqrt = a**2 + b**2
        c = cSqrt**0.5

        if(a+b+c==1000):
            product = a*b*c
            print(product)
            break
    
