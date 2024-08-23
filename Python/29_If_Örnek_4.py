sayi=int(input("Lütfen bir sayi giriniz:"))
kontrol=(sayi>0) and (sayi%2==1)

if kontrol==True:
    print("Tek bir sayi girdiniz")
else:
    print("Çift bir sayi girdiniz")