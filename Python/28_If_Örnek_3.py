İsim=str(input("Lütfen adınızı giriniz:"))
Yas=int(input("Lütfen yaşınızı giriniz:"))
Egitim=str(input("Lütfen eğitim durumunu giriniz:"))
Egitim2=("ilkokul","ortaokul","lise","üniversite")

if Egitim not in Egitim2:
    print("lütfen geçerli bir eğitim durumu giriniz:")
elif (Yas>=18) and (Egitim=="lise" or Egitim=="üniversite"):
    print("Ehliyet şartları geçildi!")
else:
    print("Ehliyet şartları gerçekleşmiyor!")