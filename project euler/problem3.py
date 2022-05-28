
# en büyük ortak bölen



L=[]
def faktor(sayi):  # Fonksiyon Oluşturuldu
    bolundu = False  # Boolean ile asal olup olmadığını kontrol edeceğiz
    sayi2 =sayi
    for i in range(2, sayi):  # Sayıyı 2 den başlatarak saydırma işlemini başlattım
        if (sayi % i == 0):  # i değeri sayi değerini tam bölüyor mu kontrol ettik.
            for k in range(2,i):  # Sonra i sayısına kadar saydırarak asal olup olmadığına gerekli kontrolleri yaparak karar vereceğiz.
                if (i % k == 0):  # Eğer i'nin k'ya modu 0 ise bolundu değeri True olur
                    bolundu = True
            if (bolundu == False):#Eğer bolunmez ise sayımız asal çarpanıdır
                # print(i)#Ekrana bastık sayımızı
                L.append(i)
                sayi2 =sayi2/i #Burada bunu yapmamızın sebebi eğer bir sayı asal çarpanlarına bölünüyor ise sonuç 1 olacaktır. Bundan dolayı sayi2'yi her asal olan ve tam bölen değer ile bölüyoruz.
                if(sayi2==1):#Eğer sonuç 1 çıkarsa algoritma duracaktır.
                    break
            bolundu = False
 
faktor(600851475143)
print(L)
 
print("600851475143 sayısının en büyük asal böleni",L[-1])
    
    
    



    


