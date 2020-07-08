"""karesi=lambda sayı:sayı**2
print(karesi(8))
yazdır=lambda metin:print(metin)
yazdır("ello")"""

#istediğimiz paranteze istediğimizi koymak için
"""metin="birinci {1} ikinci {0} üçüncü {1}".format("deger1","deger2","deger3")
print(metin)
metin="benim adım {isim} soyadım {soyad} boyum {boy} ".format(isim="ali",soyad="yılmaz",boy=1.80)
print(metin)"""
#%ile string biçimlendirme
"""isim="vedat"
print("benim adım %s" % isim)"""
"""%d=int
%s=string
%f=float"""
"""ucret=59.94563333
print("aldığım sapkanın ucreti %.2f" % ucret)#noktadan sonra iki sayıyı yaz .2f
urun="sapka".title()
ucret=45.876768
urunFormatlı=urun[0].upper() + urun[1:].lower()
print("ürün türü: %s ücreti %.2f TL"%(urun,ucret))"""
#DEĞİŞKENLERİN KAPSAMLARI
genelDegisken="bana her yerden erişebilirsin"
def fonksiyon1():
    fonk1Degiskeni=123
def fonksiyon2():
  
    print(genelDegisken)


fonksiyon2()    
