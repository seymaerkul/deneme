#chat uygulaması
import kullanıcıKayıt
from datetime import date
def mesajGonder(**kwargs):
    dosya=open("mesajlar.txt","a")
    dosya.write(kwargs["ben"].lower())
    dosya.write("|")
    dosya.write(kwargs["arkadas"].lower())
    dosya.write("|")
    dosya.write(kwargs["mesaj"].lower())
    dosya.write("|")
    dosya.write(str(kwargs["tarih"]))
    dosya.write("|")
    dosya.write("\n")
    dosya.close()
    print("{ben} adlı kişi {arkadas} adlı kullanıcıya mesaj göderdi".format(ben=kwargs["ben"].title(),arkadas=kwargs["arkadas"].title()))


def mesajKutusu(kullanıcıAdı):
    dosya=open("mesajlar.txt","r")
    satirlar=dosya.readlines()
    for mesaj in satirlar:
        bolunmus=mesaj.split("|")
        gonderen=bolunmus[0]
        alıcı=bolunmus[1]
        mesaj=bolunmus[2]
        tarih=bolunmus[3]
        #if kullanıcıAdı==gonderen or kullanıcıAdı==alıcı :

        print("gönderen:",gonderen," ","alıcı:",alıcı," ","mesaj:",mesaj," ","tarih:",tarih)





def arkadasEkle(**kwargs):
    
    dosya=open("arkadas.txt","a")
    dosya.write(kwargs["ben"].lower())
    dosya.write(" ")
    dosya.write(kwargs["arkadas"].lower())
    dosya.write("\n")
    dosya.close()
    print("{ben} ismli kişi {arkadas} isimli kullanıcıyı ekledi".format(ben=kwargs["ben"].title(),arkadas=kwargs["arkadas"].title()))



def arkadasListesi(kullanıcıAdı):
    try:
        arkadasvar=False
        dosya=open("arkadas.txt","r")
        satirlar=dosya.readlines()
        for arkadaslar in satirlar:
            bolunmus=arkadaslar.split()
            ark1=bolunmus[0]
            ark2=bolunmus[1]
            if kullanıcıAdı==ark1:
                print(ark2)
                arkadasvar=True
            elif kullanıcıAdı==ark2:
                print(ark1)
                arkadasvar=True

        if not arkadasvar:
            print("hic arkadas yok")
    except FileNotFoundError:
        print("hata")
    input()
        
def kisiselMenu(kullanıcıAdı):
   while kullanıcıKayıt.cevrimici_kullanıcı:

       print("""



1.arkadaş listesi
2.arkadaş ekle
3.mesaj gönder
4.mesaj kutusu
5.çıkış

""")
       secim=int(input("secim yap"))
       if secim==1:
           arkadasListesi(kullanıcıAdı)
       elif secim==2:
           arkadas=input("eklemek istediğin arkadaşı yaz")
           arkadasEkle(ben=kullanıcıAdı,arkadas=arkadas)
       elif secim==3:
           arkadas=input("mesajı kime gönderiyorsun")
           mesaj=input("mesajını yaz")
           mesajGonder(ben=kullanıcıAdı,arkadas=arkadas,mesaj=mesaj,tarih=date.today())
       elif secim==4:

           mesajKutusu(kullanıcıAdı)
       elif secim==5:
           print("çıkış yapılıyor...")
           kullanıcıKayıt.cevrimici_kullanıcı=False


if __name__=="__main__":
    while True:
        print("""

1.kayıt ol
2.giris yap
""")
        secim=int(input("secim yap"))
        if secim==1:
            kullanıcıKayıt.kayıtOl()
        elif secim==2:
            kullanıcıKayıt.girisYap()
            if kullanıcıKayıt.cevrimici_kullanıcı:
                kisiselMenu(kullanıcıKayıt.cevrimici_kullanıcı)
               
