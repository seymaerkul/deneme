#kullanıcı kayıt uygulaması
import os,time
cevrimici_kullanıcı=False
def kayıtOl():
    kullanıcıAdı=input("kullanıcı adı gir")
    mail=input("mail adresini gir")
    if  not kontrol(kullanıcıAdı):
        print("kullanıcı zaten mevcut")
        time.sleep(1)
        os.system(temizle)

        return kayıtOl()
    sifre=input("şifrenizi girin")
    sifreOnay=input("şifrenizi tekra girin")
    if sifre!=sifreOnay:
        print("şifreler eşleşmedi")
        return kayıtOl()
    dosya=open("kullanıcı.txt","a")
    dosya.write(kullanıcıAdı)
    dosya.write(" ")
    dosya.write(sifre)
    dosya.write(" ")
    dosya.write(mail)
    dosya.write("\n")
    dosya.close()
    print("kullanıcı eklendi")
    input()
def kontrol(kullanıcıAdı):
    try:
        if kullanıcıAdı  not in open("kullanıcı.txt","r").read():
            return True
        else:
            return False
    except FileNotFoundError:
        return True
def girisYap():
    global cevrimici_kullanıcı
    kullanıcıAdı=input("kullanıcı adını gir")
    sifre=input("sifreni gir")
    dosya=open("kullanıcı.txt","r")
    satirlar=dosya.readlines()
    cevrimici_kullanıcı=False
    for kullanıcı in satirlar:
        bolunmus=kullanıcı.split()
        bolunmusKullanıcı=bolunmus[0]
        bolunmusSifre=bolunmus[1]
        if kullanıcıAdı==bolunmusKullanıcı and sifre==bolunmusSifre:
            cevrimici_kullanıcı=kullanıcıAdı
        
    if cevrimici_kullanıcı:
        print("hosgeldiniz",kullanıcıAdı)
    else:
        print("kullanıcı adı veya şifre hatalı ")
    input()
temizle=("cls" if os.name=="nt" else "clear")
if __name__=="__main__":
    while(True):
        print("""

            1-kayıt ol
            2-giriş yap


    """)
        secim=int(input("seçimini yap"))
        if secim==1:
            kayıtOl()
            
        elif secim==2:
            girisYap()
        





    



