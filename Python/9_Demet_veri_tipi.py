#listelere göre çok daha hızlıdır
#içindeki veriler değiştirilmez
#iç içe demet yapısı kurulabilir
liste=["Ahmet",23]
print(type(liste))
demet1=("Ahmet")
print(type(demet1))
demet2=("Ahmet",24)
print(type(demet2))
#içerisine birden fazla değişken gelirse otomatik tuple olarak tanımlanır
liste[0]="Mehmet"
print(liste)
#demet2[0]="Mehmet" bu şekilde değişiklik yapamayız