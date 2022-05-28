
L=[]
def birbolu(n):
    for i in range(1,n):
        cevap = 1/i
        L.append(str(cevap))
        #print(str(1)+"/"+str(i),"    ",cevap)

birbolu(1000)
M=[]
K=[]
for i in range(1,len(L)):
    if(len(L[i-1])<len(L[i])):
        M.append(L[i])
        K.append(i)
    else:
        continue

print(M[-1])
print(K[-1])
           
        
    
