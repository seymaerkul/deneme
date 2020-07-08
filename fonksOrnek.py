"""def tekmiCiftmi(x):
    if x %2==0:
        print(x,"çifttir")
    else:
        print(x,"tektir")




tekmiCiftmi(5)   """

########
"""
def harfBuyut(liste):
    x=0
    for kelime in liste:
        liste[x]=kelime.upper()
        x+=1

    return liste


kelimeler=["aaaa","bbbb","cccc"]
print(harfBuyut(kelimeler))
"""
"""
def listeDuzenle(liste):
    metin=[]
    tamSayı=[]
    ondalıklıSayı=[]
    for eleman in liste:
        if isinstance(eleman,int):
            tamSayı.append(eleman)
            
        elif isinstance(eleman,float):
            ondalıklıSayı.append(eleman)
          
            
        elif isinstance(eleman,str):
            metin.append(eleman)

            
        else:

            print("veri tipi tanımlanmadı")
    return metin,tamSayı,ondalıklıSayı





liste=["biber","domates","patlıcan",2.3,5.6,8.8,1,2,3,4,5]
print(listeDuzenle(liste))"""
def hello():
    print("hello world")

    
def carpı2(x):
    return x*2


def tamSayıCarp(liste):
    i=0
    for eleman in liste:
        if isinstance (eleman,int) or isinstance(eleman,float):
            liste[i]=carpı2(eleman)
        i+=1
    return liste



liste=[3,6,10,"jgg",12.5]
print(tamSayıCarp(liste))



hello()



























