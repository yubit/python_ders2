

sayi1 = 5
sayi2 = 3

sonuc = (sayi1 ** sayi2) // (sayi2 + sayi1)

# if sonuc is 15:
#     print('Sonuç is 15')
#
# if sonuc == 15:
#     print('Sonuç == 15')

# dogru_mu = sonuc is 15
# print('Doğru mu ?', dogru_mu)
#
# print('Sonuç is 15', sonuc is 15)
# print('Sonuç == 15', sonuc == 15)
#
# print('Sonuç id: {}, 15 id: {}'.format(id(sonuc), id(15)))
# print('Sonuç id == 15 id:', id(sonuc) == id(15))
# print('Sonuç id is 15 id:', id(sonuc) is id(15))
#

if sonuc is not 16:
    print('Sonuç is not 16')

if not sonuc is 16:
    print('NOT Sonuç is 16')

if sonuc != 16:
    print('Sonuç != 16')

if not sonuc <= 1:
    print('Sonuç not <= 1')
