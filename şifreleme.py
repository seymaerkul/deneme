import string
import os

#get all letters
alphabet=string.ascii_lowercase
max_character=len(alphabet)


clean=("cls" if os.name=="nt" else "clear")


def options():
    while  True:
        os.system(clean)
        option=input("what do you want ?").lower()
        if option in ("sifrele","sifreleme","sifreleme yapmak","sifreleme yapmak isterim"):
            encryption()

        elif option in("şifre çözmek","çözmek","şifre çöz"):
            sifreCoz()

        else:
            print("şifreleme yapmak için %s,şifre çözmek için %s yazın" % ("şifrele","şifre çöz"))

def encryption():
    metin=input("sifrelenecek metni gir").lower()
    encryption_key=encryptionKey()
    sifrelenmis_metin=""
    for karakter in metin:
        if karakter.isalpha():
            karakter_pos=ord(karakter)
            karakter_pos += encryption_key
            if karakter_pos>ord("z"):
                karakter_pos -= max_character
            elif karakter_pos<ord("a"):     
                  karakter_pos += max_character
            sifreliKarakter=chr(karakter_pos)
            sifrelenmis_metin+=sifreliKarakter
        else:
            sifrelenmis_metin+=karakter
    print("%s kelimesinin %d ile şifrelenmiş hali %s" % (metin,encryption_key, sifrelenmis_metin))
    input()





def sifreCoz():
    sifreli_metin=input("çözülecek metni gir").lower()
    encryption_key=encryptionKey()
    cozulmus_metin=""
    for karakter in sifreli_metin:
        if karakter.isalpha():
            karakter_pos=ord(karakter)
            karakter_pos -= encryption_key
            if karakter_pos>ord("z"):
                karakter_pos -= max_character
            elif karakter_pos<ord("a"):     
                  karakter_pos += max_character
            cozulmusKarakter=chr(karakter_pos)
            cozulmus_metin+=cozulmusKarakter
        else:
            cozulmus_metin+=karakter
    print("%s şifreli metninin %d ile çözülmüş hali hali %s" % (sifreli_metin,encryption_key, cozulmus_metin))
    input()


    



    
def encryptionKey():
    key=int(input("enter the encryption key (1-%s):" % max_character))
    if key>=1 and key<=max_character:
        return key
    else:
        return 1

if __name__=="__main__":
    options()
