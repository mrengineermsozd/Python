x="mrengineer mso"
for i in x:
    if i==" ":
        continue
    print(i)

import random

# 0 ile 20 arasında rastgele bir sayı seç
dogru_sayi = random.randint(0, 20)

# Kullanıcıya 5 tahmin hakkı ver
tahmin_hakki = 5

print("0 ile 20 arasında bir sayı tuttum. Bunu tahmin etmek için 5 hakkınız var.")

while tahmin_hakki > 0:
    tahmin = int(input("Tahmininizi girin: "))
    
    if tahmin == dogru_sayi:
        print("Tebrikler! Doğru sayıyı tahmin ettiniz.")
        break  # Doğru sayı tahmin edildiğinde döngüyü sonlandırır
    else:
        tahmin_hakki -= 1
        if tahmin < dogru_sayi:
            print("Daha büyük bir sayı tahmin edin.")
        else:
            print("Daha küçük bir sayı tahmin edin.")
        
        if tahmin_hakki > 0:
            print(f"Kalan tahmin hakkınız: {tahmin_hakki}")
        else:
            print(f"Tahmin hakkınız bitti. Doğru sayı {dogru_sayi} idi.")