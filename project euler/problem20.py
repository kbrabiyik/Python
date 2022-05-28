L=[]
def faktoriyel(n):
    if (n <=1):
        return(1)
    elif(n>1):
        return(n*faktoriyel(n-1))

sayi= faktoriyel(100)
L= list(str(sayi))

top =0
for i in range(len(L)):
    top = top + int(L[i])

print(top)
    


        
