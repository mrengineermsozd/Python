Bilgi=["Ahmet","Yıldız",35,"Evli"]
print(Bilgi)
#içerisinde farklı veri tiplerini barındıran veri tipidir
print(Bilgi[2])
#indisleri yine 0 dan başlar
x="Ahmet"
#x[2]=n hata verir fakat listelerde bu değişiklikler yapılabilir
Bilgi[0]="Mehmet"
print(Bilgi)
Bilgi2=["Murat","Özden",25,"Evli"]
Bilgi3=[Bilgi,Bilgi2]
print(Bilgi3)
print(len(Bilgi3))