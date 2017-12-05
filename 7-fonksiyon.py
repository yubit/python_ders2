# def merhaba():
#     print('Merhaba')
#
#
# merhaba()

# def topla(sayi1, sayi2):
#     print(sayi1 + sayi2)
#
#
# topla(3, 5)
# topla(sayi2=3, sayi1=5)
# topla(3, sayi2=5)
# # yanlış kullanım
# # topla(sayi1=3, 5)


# def kare(sayi):
#     sonuc = sayi * sayi
#     return sonuc
#
#
# uc = 3
# karesi = kare(uc)
# print(karesi)
#
# kare(5)

# def usd_to_tl(miktar, kur=3.87):
#     return miktar * kur
#
#
# para = usd_to_tl(25)
# print(para)


liste = ['Yaşar', 'Üniversitesinde', 'Okuyorum']


def bastir(isim, *kelimeler):
    print(isim,".", *kelimeler)


bastir(*liste)
bastir(liste)

