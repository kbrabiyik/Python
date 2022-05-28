# bilmemkaca kadar olan asal sayıların toplamını veren kod
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if (n%i ==0):
            return False
    return True

summ = 0
for i in range(2,100):
    if(isPrime(i)):
        summ+=i
print(summ)
            
