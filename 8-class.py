class Insan:
    isim = 'Sıradan İnsan'
    yas = 0

    @classmethod
    def konus(kendi):
        print(kendi.isim, 'konuşur...')

    def kare_al(self, sayi):
        karesi = sayi * sayi
        print(self.isim, 'kare alır... Sonuç:', karesi)


# insan1 = Insan()
# insan1.isim = 'Rüzgar Burak'
# insan1.konus()
# insan1.kare_al(5)
#
# insan2 = Insan()
# insan2.konus()
# insan2.kare_al(3)

print(Insan.isim)
Insan.konus()