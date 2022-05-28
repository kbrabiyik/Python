#9009 = 91*99
# en büyük 3 basamaklı iki sayinin carpimi olucak
# ve simetrik olucak

L=[]
n = 0
for a in range(999, 100, -1):
    for b in range(999, 100, -1):
        x = a * b
        if(x > n):
            s = str(a * b)
            if(s == s[::-1]):
                 n = a * b
                 L.append(a)
                 L.append(b)
print("Palindrom value is",n)
print(L[-1],"*",L[-2],"is",n)

