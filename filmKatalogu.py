filmler={"kara korsanın laneti":{"yapım yılı":1957,"imdb":8.2,"tür":"korku"},"sinegin intikamı":{"yapım yılı":1945,"imdb":9.2,"tür":"korku"}}
#print(filmler)
def filmEkle():
    filmAdı=input("film adı gir")
    global filmler


    if filmAdı:
        yapım_yılı=input("yapım yılı gir")

        imdb=input("imdb")

        tur=input("film türü gir")

        filmler[filmAdı]={"yapım yılı":yapım_yılı,"imdb":imdb,"tur":tur}
        print("film eklendi")
        
    else:
       
         print("film adı yok")


def filmSil():
    filmAdı=input("film adı gir")
    


    if filmAdı:
        filmler.pop(filmAdı)
        print("film silindi")
        
    else:
        print(" film yok")
        input(" devam etmke için herhangi bir tuşa bas")
        
def filmGetir():
    aranan=input("hangi film")
    if aranan in filmler.keys():
        yapım_yılı=(filmler.get(aranan)).get("yapım yılı","yapım yılı yok")
        imdb=(filmler.get(aranan)).get("imdb"," yok")
        tur=(filmler.get(aranan)).get("tür"," yok")
        print("film adı : {}  yapım yılı {}   ımdb: {}  tur:  {}".format(aranan,yapım_yılı,imdb,tur)
            )
        input(" devam etmke için herhangi bir tuşa bas")
    else:
        print("film yok")
        input(" devam etmke için herhangi bir tuşa bas")
        
def filmListesi():
    for film in filmler:
        filmAdı=film
        yapım_yılı=filmler[film].get("yapım yılı","yok")
        imdb=filmler[filmAdı].get("imdb","yok")
        tur=filmler[filmAdı].get("tür","yok")
        print("film adı : {}  yapım yılı {}   ımdb: {}  tur:  {}".format(filmAdı,yapım_yılı,imdb,tur))
        print("===="*80)
       
    
while True:
    print(""""1-tümfilmleri listele
    2-film ara
    3-film ekle
    4-film sil""")
    secenek=int(input("secimini yap"))
    if secenek==1:
        filmListesi()
        
    elif secenek==2:
     
     
        filmGetir()
    elif secenek==3:
         filmEkle()
    elif secenek==4:
          filmSil()
