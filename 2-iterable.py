

liste = ['izmir', 'bornova', 'python']

# print('Listenin uzunluğu:', len(liste))
#
# for isim in liste:
#     print('İsim: {}, Uzunluğu: {}'.format(isim, len(isim)))
#
# for karakter in 'izmir':
#     print('Karakter:', karakter)
#

# for isim in liste:
#     for karakter in isim:
#         print('İsim: {}, {}. karakter: {}'.format(isim, isim.index(karakter), karakter))
#     print()
# #
if 'izmir' in liste:
    print('İzmir listenin içinde')

print('izmir' in liste)

if 'i' in liste:
    print('i harfi listede')
else:
    print('i harfi listede değil')

if 'i' in 'izmir':
    print('i izmirin içinde')