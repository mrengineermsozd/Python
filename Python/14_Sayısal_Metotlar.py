x=9.4
print(x.__abs__())
#sayının mutlak değerini alır
print(x.__pow__(3))
#sayının üssünü alır
print(x.__divmod__(1))
#divmod içinde yazan sayıya bölüm ve kalanını verir
print(x.as_integer_ratio())
#kaçın kaça bölümü x i verir onu verir 
print(x.is_integer())
#sayı intiger ise true diğer veri tiplerinde false verir.
print(x.__ceil__())
#sayıyı yukarı yuvarlar
print(x.__floor__())
#sayıyı aşağı yuvarlar
print(x.__mod__(2))
#modülüs bölme yaparak kalanı verir
