#ürünler isminde televizyon,buzdolabı,bilgisayar,fırın
Ürünler=["Televizyon","Buzdolabı","Bilgisayar","Fırın"]
print(Ürünler)
#kaç adet ürün olduğunu çıktı veren kod
print(len(Ürünler))
#ürünlerimizin ilk iki ürünün adı nedir
print(Ürünler[0:2])
#ilk ve sonuncu ürünü getir
print(Ürünler[0],Ürünler[len(Ürünler)-1])
#fırın ürünü ile ütü değişimi olsun
Ürünler[len(Ürünler)-1]="Ütü"
print(Ürünler)
#ürünler listesine çamaşır makinesi ekle
Ürünler=Ürünler+["Çamaşır Makinesi"]
print(Ürünler)
#ürünler listesini tersten yazdıralım
print(Ürünler[::-1])