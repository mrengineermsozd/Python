x="mustafa serhat özdemir"
ad="Serhat"
soyad="Özdemir"
görev="Öğrenci"
bilgiler=[ad,soyad,görev]
print("Kişi adı: {},Kişinin Soyadı: {},Kişinin Görevi: {}"
      .format(bilgiler[0],bilgiler[1],bilgiler[2]))

print(x.lower())
#tüm karakterleri küçük harfe çevirir 
print(x.upper())
#tüm karakterleri büyük harfe çevirir
print(x.islower())
#harflerin küçük olup olmadığını sorgular ve true false değer olarak çıktı verir
print(x.isupper())
#harflerin büyük olup olmadığını sorgular ve true false değer olarak çıktı verir
print(x.isnumeric())
#içeriğinin sayısal değer olup olmadığını sorgular
print(x.isalnum())
#içeriğinin sayısal değer olup olmadığını sorgular
print(x.capitalize())
#stringde yer alan sadece ilk karakteri büyük harf yapar
print(x.title())
#stringde yer alan boşluktan sonraki her kelimenin ilk harfini büyük harf yapar
print(x.swapcase())
#büyük harfleri küçük harfe küçük harfleri büyük harfe çevirir
print(x.count("a"))
#karakter dizisi içerisinde kaç tane o karakterden olduğunu bulur
print(x.strip("öz"))
#baştan ve sondan boşluk varsa götürür ama örneğin ir yazarsan sağdan başlar ve iri siler ancak öz yazarsak silmez 
print(x.split(" "))
#karakter dizisi içerisinde eklediğiniz karakterden ayırma işlemi yapar
print(x.find("öz"))
#öz kelimesinin hangi karakterde yer aldığını bulur 
print(x.format())