print("""
    secenegin nedir?
    [1].filtre kahve
    [2].sicak cikolata
    [3].espresso
    [4].mocha



    """)


    
secim=int(input("seciminiz nedir? :"))
if secim==1 :
    seker=input("seker ister misniz?")
    if seker=="evet":
       print("seker ekleniyor")
    elif seker=="hayır":
       print("seker eklenmedi") 
    print("filtre kahve hazirlaniyor")
    
elif secim==2:
    seker=input("seker ister misniz?")
    if seker=="evet".lower():
       print("seker ekleniyor")
    elif seker=="hayır".lower():
       print("seker eklenmedi")
    print("sicak cikolata hazirlaniyor")
elif secim==3:
    seker=input("seker ister misniz?")
    if seker=="evet".lower():
       print("seker ekleniyor")
    elif seker=="hayır".lower():
       print("seker eklenmedi")
    print("espresso hazirlaniyor")
elif secim==4:
    seker=input("seker ister misniz?")
    if seker=="evet".lower():
       print("seker ekleniyor")
    elif seker=="hayır".lower():
       print("seker eklenmedi")
    print("mocha hazirlaniyor")
else:
    print("gecersiz secim")
