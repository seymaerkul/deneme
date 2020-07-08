def toplama(sayi1,sayi2):
    result=sayi1+sayi2
    print("{} + {} = {}".format(sayi1,sayi2,result))
    print("toplama isleminin sonucu {}".format(result))

def cikarma(sayi1,sayi2):
    result=sayi1-sayi2
    print("{} - {} = {}".format(sayi1,sayi2,result))
    print("cikarma isleminin sonucu {}".format(result))


def usAlma(sayi1,sayi2):
    result=sayi1**sayi2
    print("{} ^ {} = {}".format(sayi1,sayi2,result))
    print("us alma isleminin sonucu {}".format(result))

def bolme(sayi1,sayi2):
    result=sayi1/sayi2
    print("{} / {} = {}".format(sayi1,sayi2,result))
    print("us alma isleminin sonucu {}".format(result))




secenek="""
            [1].toplama
            [2].cikarma
            [3].us alma
            [4].bolme
            """
print(secenek)
secenek=int(input("seciminizi girin"))
sayilar=(input("islem yapılacak sayilari giriniz"))
sayilar_bolunmus=sayilar.split(" ")


sayi1=float(sayilar_bolunmus[0])
sayi2=float(sayilar_bolunmus[1])



if secenek==1:
    toplama(sayi1,sayi2)
elif secenek==2:
    cikarma(sayi1,sayi2)
elif secenek==3:
    usAlma(sayi1,sayi2)
elif secenek==4:
    bolme(sayi1,sayi2)
else :
    print("hatali secim yaptiniz")
   
    
