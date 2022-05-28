
L=[]
L.append(2)
a =1
for deger in range(2,2000000):
    for i in range(2,deger):
        if(deger%i != 0):
            a = 2
            continue
            
        elif(deger%i ==0):
            a = 4
            break
    if(a ==2):
        L.append(deger)
    if(len(L)==10000):
        break
        print(L[-1])



            
