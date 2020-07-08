filmler=[("kara korsanın laneti",1957,8,"korku"),("sinegin intikamı",2957,1.2,"belgesel"),("yılan rüzgarı",1997,9.2,"romantik"),("calm down",1997,9.2,"romantik")]






def filmleriListele(filtre=None,değer=None):
    for film in filmler:
        if not filtre and not değer:
            print("filmin adı: {}({})   imdb: {}    tür:  {}".format(film[0],film[1],film[2],film[3]))

        elif filtre=="film adı":
            
            if değer.lower()==film[0].lower():
                 print("filmin adı: {}({})   imdb: {}    tür:  {}".format(film[0],film[1],film[2],film[3]))

                
        elif filtre=="yapım yılı":
            
            if değer==film[1]:
                 print("filmin adı: {}({})   imdb: {}    tür:  {}".format(film[0],film[1],film[2],film[3]))

        elif filtre=="imdb":
            
            if değer==film[2]:
                 print("filmin adı: {}({})   imdb: {}    tür:  {}".format(film[0],film[1],film[2],film[3]))

        elif filtre=="tür":
            
            if değer.lower()==film[3].lower():
                 print("filmin adı: {}({})   imdb: {}    tür:  {}".format(film[0],film[1],film[2],film[3]))

              
                

filmleriListele("film adı", "kara korsanın laneti")
menu="""
filmi hangi kıstasa göre aramak istersin?
    1-film adı
    2-yapım yılı
    3-imbd puanı
    4-tür
    5-hepsi
    0-çıkış"""
print(menu)
secim=int(input("seciminiz nedir?"))
if secim==1:   
    filtre="film adı"
    değer=input("film adını gir")
    filmleriListele(filtre,değer)
   
elif secim==2:    
    filtre="yapım yılı"
    değer=int(input("yapım yılını gir"))
    filmleriListele(filtre,değer)
elif secim==3:   
    filtre="imdb"
    değer=float(input("imdb puanını gir"))
    filmleriListele(filtre,değer)
elif secim==4:
    mesaj="tür girin"
    filtre="tür"
    değer=input("tür adını gir")
    filmleriListele(filtre,değer)

