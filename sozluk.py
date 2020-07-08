import os
kelimeler={"get":["almak","edinmek","olmak","elde etmek"],
           "break":["mola","ara","kırılmak","fren"],
           "winner":["kazanan","galip","birinci"]}
def kelimeListele():
    for no,kelime in (list(enumerate(kelimeler,1))) :
        print("{}.{}".format(no,kelime))
    input("devam etmek için tuşa bas")      
  



def kelimeCevir(kelime,kelimeler):
    if kontrol(kelime,kelimeler):
        print("{} kelimesinin anlamları ".format(kelime),end=": ")
        print(*kelimeler[kelime])

    else:
        print("{} kelimesi mevcut değil".format(kelime))

    input("devam etmek için tuşa bas")


    
def kontrol(kelime,kelimeler):
    if kelime in kelimeler:
        return True
    else:
        return False

    input("devam etmek için tuşa bas")

def kelimeEkle(kelime,kelimeler):
    if kontrol(kelime,kelimeler):
        mevcut=set(kelimeler[kelime])
        yeniGiris=input("kelime zaten mevcut.girilen  kelimenin kayıtlı anlamları:{}\n yeni anlam girmek ister misin (E/H)".format(mevcut))
        if yeniGiris.lower()=="e":
            yeniAnlam=input("girmek istediğiniz anlamları yazın")
            yeniAnlamBolunmus=set(yeniAnlam.split(","))
            kelimeler[kelime]=list(mevcut|yeniAnlamBolunmus)
            print("anlamlar kaydedildi",kelimeler[kelime])
        elif yeniGiris.lower()=="h":
            pass
            
    else:
        yenikelime=input("girmek istediğiniz kelime yazın")
        yenikelimeBolunmus=set(yenikelime.split(","))
        kelimeler[kelime]=list(yenikelimeBolunmus)
        print("anlamlar kaydedildi",kelimeler[kelime])
    input("devam etmek için tuşa bas")                        
secenekler="""
[1].kelime ekle
[2].kelime çevir
[3].kelime listele

"""
while(True):
    temizle=("cls" if os.name=="nt" else "clear")
    os.system(temizle)
    print(secenekler)
    secenekler=int(input("secimini yap"))
    if secenekler==1:
        kelime=input("eklenecek kelimeyi yaz")
        kelimeEkle(kelime,kelimeler)    
    elif secenekler==2:
        kelime=input("cevirilecek kelimeyi yaz")  
        kelimeCevir(kelime,kelimeler)     
    elif  secenekler==3:
         kelimeListele()
        
