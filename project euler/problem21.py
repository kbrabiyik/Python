# d(n) = n in bölenlerinin toplamı
# d(a) =b
# d(b) =a
# a nın b ye eşit olmadıgı durumları bul
L=[]
def bolumtoplamlari(n):
    top = 0
    for i in range(1,n):
        if(n%i ==0):
            top +=i
    return top

for j in range(1,10000):
    birinci = bolumtoplamlari(j)
    if(bolumtoplamlari(birinci) == j and birinci!=j):
        L.append(j)
        
top = 0
for k in range(len(L)):
    top = top+ L[k]

print(L)
print(top)
    
    
    
        

    
    
            
