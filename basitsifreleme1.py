harfler="abcdefghijklmopqrstuwxyz"

kelime="Hey"

kelime=kelime.lower()
print(kelime[0]+"------"+harfler[harfler.index("h")])
sifreliKelime=harfler[harfler.index(kelime[0])+1]+harfler[harfler.index(kelime[1])+1]+harfler[harfler.index(kelime[2])+1]

print(kelime,"kelimesinin sifreli hali",sifreliKelime)
sifresiKırılmıs=harfler[harfler.index(kelime[0])]+harfler[harfler.index(kelime[1])]+harfler[harfler.index(kelime[2])]
print(sifreliKelime,"kelimesinin cozulmus hali",sifresiKırılmıs)                                                                                          
