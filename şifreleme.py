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



def encryption():
    metin=input("sifrelenecek metni gir").lower()
    encryption_key=encryptionKey()

            

def encryptionKey():
    key=input("enter the encryption key (1-%s)" % max_character)
    



options()
