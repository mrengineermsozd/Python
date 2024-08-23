Liste=[1,2,3,"Merhaba",4,5]
Liste.append("A")
print(Liste)
#listeye yeni bir karakter veya sayı eklemeye yarar
Liste.insert(3, 5)
print(Liste)
#insert tanımlanan konuma yeni bir karakter veya sayı ekler
Liste.remove(2)
print(Liste)
#soldan başlayarak ilk karşılaştığı değeri siler
Liste.pop(2)
print(Liste)
#istenilen indexi siler içi boş bırakılırsa en soldaki indexi siler
Liste2=Liste.copy()
print(Liste2)
#yeni bir değişkene başka bir diziyi atamak için kullanılır
Liste.extend(Liste2)
print(Liste)
#iki listeyi birbirine eklemek için kullanılır liste 1 üzerine liste 2 eklenir
print(Liste.count(1))
#liste içerisinde o karakterden kaç tane olduğunu bulmaya yarar
liste3=[1,5,7,9,2,4]
liste3.sort()
print(liste3)
#küçükten büyüğe sıralar
liste3.reverse()
print(liste3)
#listeyi ters çevirir
liste3.clear()
print(liste3)
#listenin içini temizler 