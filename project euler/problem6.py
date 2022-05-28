L=[]
for i in range(101):
    L.append(i)

toplam = (L[-1]*L[-2])/2
toplamkare = toplam**2 # toplamlarının karesi

L_2 = []
for i in range(1,101):
    a = i**2
    L_2.append(a)

top =0
for i in range(len(L_2)):
    top = top + L_2[i]
print("The difference is",toplamkare-top)
