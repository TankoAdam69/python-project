from statok import energia, veszely, egyenleg, ido, XP, eloadas
import os

win = False
lose = False
print('Győr szimulátor')
print('1: Start')
print('2: Kilépés')
v = input('Választás: ')
match v:
    case '1':
        os.system('cls')
        print('Köszöntünk a Győr Szimulátorban, ahol legfőbb célod a Bécsi vonatra jegyet venni lesz, illetve fel is szállni erre a vonatra. Emellet különböző lehetőségeid lesznek munkára, evésre, illetve edzőterembe járásra. Utad a vidéki buszmegálóban fog kezdődni, sok szerencsét kívánunk.')
        while win == False and lose == False:
            def main():
                pass
            main()
    case '2':
        os.system('cls')
        print('Köszönjük hogy benéztél.')