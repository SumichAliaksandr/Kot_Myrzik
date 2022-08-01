from random import randint

from kivy.core.audio import SoundLoader

def cena(i):
    if i == 'Купить шляпку':
        return 100
    elif i == 'Купить бабочку':
        return 200
    elif i == 'Купить шарфик':
        return 300
    else:
        return 0
def moneta(i):

    if i % 10 == 1:
        m = ' монета '
    elif (i % 10 == 2) or (i % 10 == 3) or (i % 10 == 4):
        m = ' монеты '
    else:
        m = ' монет '
    if i % 100 // 10 == 1:
        m = ' монет '
    return m

def rnd_krome(pravilnyi_otvet):
    z = randint(1,40)
    while z == pravilnyi_otvet:
        z = randint(1,40)
    return str(z)

for schetcik in range(1000):
    print (schetcik, moneta(schetcik))



