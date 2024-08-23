Kullanıcı_Adı=input("Lütfen Kullanıcı adını giriniz:")
Kullanıcı_Sifre=input("Lütfen şifrenizi giriniz:")

SistemKullanıcıAdı="mrengineermso"
SistemKullanıcıSifre="159258357"

if Kullanıcı_Adı==SistemKullanıcıAdı and Kullanıcı_Sifre==SistemKullanıcıSifre:
    print("Merhaba {}, Hoşgeldin !!!".format(SistemKullanıcıAdı))
elif Kullanıcı_Adı!=SistemKullanıcıAdı and Kullanıcı_Sifre!=SistemKullanıcıSifre:
    print("Merhaba kullanıcı adı ve şifreyi hatalı girdiniz.")
elif Kullanıcı_Adı!=SistemKullanıcıAdı :
    print("Merhaba, Kullanıcı adını hatalı girdiniz.")
elif Kullanıcı_Sifre!=SistemKullanıcıSifre:
    print("Merhaba {}, Hatalı bir şifre girdiniz".format(SistemKullanıcıAdı))