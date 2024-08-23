sayi1=int(input("Birinci sayıyı giriniz:"))
sayi2=int(input("ikinci sayıyı giriniz:"))
hesaplar=("+","-","*","/","%","**")
islem=str(input("Lütfen yapmak istediğiniz işlemi giriniz:"))

if islem not in hesaplar:
    print("LÜTFEN GEÇERLİ BİR İŞLEM GİRİNİZ!")
elif islem=="+":
    print("Toplama işlemi seçtiniz sayı1={} ve sayı2={} Toplamın sonucu={}".format(sayi1,sayi2,sayi1+sayi2))
elif islem=="-":
     print("Çıkarma işlemi seçtiniz sayı1={} ve sayı2={} Çıkarma sonucu={}".format(sayi1,sayi2,sayi1-sayi2))
elif islem=="*":
     print("Çarpma işlemi seçtiniz sayı1={} ve sayı2={} Çarpma sonucu={}".format(sayi1,sayi2,sayi1*sayi2))
elif islem=="/":
     print("Bölme işlemi seçtiniz sayı1={} ve sayı2={} Bölme sonucu={}".format(sayi1,sayi2,sayi1/sayi2))
elif islem=="%":
     print("Modülüs Bölme işlemi seçtiniz sayı1={} ve sayı2={} Modülüs Bölme sonucu={}".format(sayi1,sayi2,sayi1%sayi2))
elif islem=="**":
     print("Üs alma işlemi seçtiniz sayı1(taban)={} ve sayı2(Üs)={} Üs Alma sonucu={}".format(sayi1,sayi2,sayi1**sayi2))