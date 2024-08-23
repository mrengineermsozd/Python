print("Merhaba Vucüt Kitle Endeksi Hesaplama Uygulamasına Hoşgeldiniz!")

boy=int(input("Lütfen boyunuzu cm cinsinden giriniz:"))
kilo=int(input("Lütfen kilonuzu kg cinsinden giriniz: "))

endeks=round(((kilo)/(boy/100)**2),2)

if endeks<=18.4:
    print("Vücut kitle endeksiniz {} ve sonucunuz zayıf çıktı.".format(endeks))
elif endeks>18.4 and endeks<=24.9:
    print("Vucüt kitle endeksiniz {} sonucunuz normal çıktı.".format(endeks))
elif endeks>25 and endeks<=29.9:
    print("Vucüt kitle endeksiniz {} sonucunuz kilolu çıktı.".format(endeks))
elif endeks>30 and endeks<=34.9:
    print("Vucüt kitle endeksiniz {} sonucunuz obez çıktı.".format(endeks))
elif endeks>35:
    print("Vucüt kitle endeksiniz {} sonucunuz mobric obez çıktı.".format(endeks))