# 2**15 = 32768 2+3+7+6+8 =26
L=[]
def ikiuzeri(n):
    deger = str(2**n)
    L = list(deger)
    print(L)
    toplam =0
    for i in range(len(L)):
        toplam = int(L[i]) + toplam
    print(toplam)
    
    

ikiuzeri(1000)






