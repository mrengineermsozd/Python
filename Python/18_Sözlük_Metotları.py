Bilgi={
    "Ad":"Mustafa Serhat",
    "Soyad":"özdemir",
    "Doğum Yeri":"Kadıköy",
    "TC:":4818841548
}
print(type(Bilgi))
print(Bilgi.keys())
#anahtar değerlerin çıktısını verir ad, soyad, doğum yeri, tc gibi
print(Bilgi.values())
#keylere karşılık gelen değerleri verir
print(Bilgi.items())
#key ve değerleri eşleştirerek döndürür
print(Bilgi.get("Ad"))
#istenilen keyin karşılığını yazdırmayı sağlar
print(Bilgi.update({"Cinsiyet":"Erkek"}))
print(Bilgi)
#yeni bir key ve değer ekleyerek sözlüğü güncellemeye yarar
Bilgi2=Bilgi.copy()
print(Bilgi2)
#yeni bir sözlüğe kopyalama yapmak için kullanılır
print(Bilgi.__len__())
#uzunluğunu hesaplar
Bilgi.pop("TC:")
print(Bilgi)
#istenilen keyi kaldırmaya yarar