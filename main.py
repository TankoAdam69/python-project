import os, random
from helyek import videki, galaxy, aluljaro, vasutallomas, allomasiDohi, allomasiDohi2, plaza, belvaros

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
        input('\nENTER')
        os.system('cls')
        energia = 100
        veszely = 0
        penz = 2500
        ora = 9
        perc = 0
        ido = f'{ora}:{perc}0'
        xp = 0
        eloadas = 0
        nap = 1
        rablas = random.randint(1,2)
        elvettPenz = random.randint(100, 1500)
        bukottEnergia = random.randint(0,35)
        def main():
            while win == False and lose == False:
                os.system('cls')
                global energia
                global veszely
                global penz
                global ora
                global perc
                global ido
                global xp
                global rablas
                global elvettPenz
                global bukottEnergia
                global nap
                global hely
                if perc > 60:
                    ora += 1
                    perc = perc % 60
                if perc == 60:
                    ora += 1
                    perc = 0
                    ido = f'{ora}:{perc}0'
                if perc >= 0 and perc < 10:
                     ido = f'{ora}:0{perc}'
                print(f'Energia: {energia}%', end='\t\t')
                print(f'Veszély: {veszely}%', end='\t\t')
                print(f'Egyenleg: {penz}Ft', end='\t\t')
                print(f'{ido}', end='\t\t')
                print(f'XP: {xp}')
                hely = videki()
                v = input('Hova szeretnél menni? ')
                match v:
                    case '1':
                        while v == '1':
                            os.system('cls')
                            energia -= 2
                            perc += 10
                            ido = f'{ora}:{perc}'
                            if perc > 60:
                                ora += 1
                                perc = perc % 60
                            if perc == 60:
                                ora += 1
                                perc = 0
                                ido = f'{ora}:{perc}0'
                            if perc >= 1 and perc < 10:
                                ido = f'{ora}:0{perc}'
                            print(f'Energia: {energia}%', end='\t\t')
                            print(f'Veszély: {veszely}%', end='\t\t')
                            print(f'Egyenleg: {penz}Ft', end='\t\t')
                            print(f'{ido}', end='\t\t')
                            print(f'XP: {xp}')
                            hely = galaxy()
                            v = input('\nSzeretnél edzeni? ')
                            if v == '1' and penz >= 1300 and veszely >= 1:
                                os.system('cls')
                                ora += 3
                                ido = f'{ora}:{perc}'
                                if perc > 60:
                                    ora += 1
                                    perc = perc % 60
                                if perc == 60:
                                    ora += 1
                                    perc = 0
                                    ido = f'{ora}:{perc}0'
                                if perc >= 1 and perc < 10:
                                    ido = f'{ora}:0{perc}'
                                energia -= 60
                                penz -= 1300
                                veszely -= 30
                                if veszely < 0:
                                    veszely = 0
                                print(f'Energia: {energia}%', end='\t\t')
                                print(f'Veszély: {veszely}%', end='\t\t')
                                print(f'Egyenleg: {penz}Ft', end='\t\t')
                                print(f'{ido}', end='\t\t')
                                print(f'XP: {xp}')
                                print('\n3 órát edzettél.')
                                v = '1'
                                energia += 2
                                perc -= 10
                                input('\nENTER')
                                # os.system('cls')
                                # perc += 10
                                # ido = f'{ora}:{perc}'
                                # if perc > 60:
                                #     ora += 1
                                #     perc = perc % 60
                                # if perc == 60:
                                #     ora += 1
                                #     perc = 0
                                #     ido = f'{ora}:{perc}0'
                                # if perc >= 1 and perc < 10:
                                #     ido = f'{ora}:0{perc}'
                                # energia -= 2
                                #hely = galaxy()
                            elif v == '1' and penz < 1300:
                                os.system('cls')
                                print(f'Energia: {energia}%', end='\t\t')
                                print(f'Veszély: {veszely}%', end='\t\t')
                                print(f'Egyenleg: {penz}Ft', end='\t\t')
                                print(f'{ido}', end='\t\t')
                                print(f'XP: {xp}')
                                print('\nNincs elég pénzed edzeni.')
                                v = '1'
                                energia += 2
                                perc -= 10
                                input('\nENTER')
                                # os.system('cls')
                                # perc += 10
                                # ido = f'{ora}:{perc}'
                                # if perc > 60:
                                #     ora += 1
                                #     perc = perc % 60
                                # if perc == 60:
                                #     ora += 1
                                #     perc = 0
                                #     ido = f'{ora}:{perc}0'
                                # if perc >= 1 and perc < 10:
                                #     ido = f'{ora}:0{perc}'
                                # energia -= 2
                                #hely = galaxy()
                            elif v == '1' and veszely < 1:
                                os.system('cls')
                                print(f'Energia: {energia}%', end='\t\t')
                                print(f'Veszély: {veszely}%', end='\t\t')
                                print(f'Egyenleg: {penz}Ft', end='\t\t')
                                print(f'{ido}', end='\t\t')
                                print(f'XP: {xp}')
                                print('\nNem vagy eléggé veszélyben az edzéshez.')
                                v = '1'
                                energia += 2
                                perc -= 10
                                input('\nENTER')
                                # os.system('cls')
                                # perc += 10
                                # ido = f'{ora}:{perc}'
                                # if perc > 60:
                                #     ora += 1
                                #     perc = perc % 60
                                # if perc == 60:
                                #     ora += 1
                                #     perc = 0
                                #     ido = f'{ora}:{perc}0'
                                # if perc >= 1 and perc < 10:
                                #     ido = f'{ora}:0{perc}'
                                # energia -= 2
                                #hely = galaxy()
                            elif v == '2':
                                os.system('cls')
                                print(f'Energia: {energia}%', end='\t\t')
                                print(f'Veszély: {veszely}%', end='\t\t')
                                print(f'Egyenleg: {penz}Ft', end='\t\t')
                                print(f'{ido}', end='\t\t')
                                print(f'XP: {xp}')
                                os.system('cls')
                                perc += 10
                                ido = f'{ora}:{perc}'
                                if perc > 60:
                                    ora += 1
                                    perc = perc % 60
                                if perc == 60:
                                    ora += 1
                                    perc = 0
                                    ido = f'{ora}:{perc}0'
                                if perc >= 1 and perc < 10:
                                    ido = f'{ora}:0{perc}'
                                energia -= 2
                                #hely = videki()
                            else:
                                os.system('cls')
                                print(f'Energia: {energia}%', end='\t\t')
                                print(f'Veszély: {veszely}%', end='\t\t')
                                print(f'Egyenleg: {penz}Ft', end='\t\t')
                                print(f'{ido}', end='\t\t')
                                print(f'XP: {xp}')
                                ('\nSemmilyen követelménnyel nem rendelkezel az edzéshez')
                                v = '1'
                                energia += 2
                                perc -= 10
                                input('\nENTER')
                                # os.system('cls')
                                # perc += 10
                                # ido = f'{ora}:{perc}'
                                # if perc > 60:
                                #     ora += 1
                                #     perc = perc % 60
                                # if perc == 60:
                                #     ora += 1
                                #     perc = 0
                                #     ido = f'{ora}:{perc}0'
                                # if perc >= 1 and perc < 10:
                                #     ido = f'{ora}:0{perc}'
                                # energia -= 2
                                #hely = galaxy()
                    case '2':
                        os.system('cls')
                        energia -= 2
                        perc += 5
                        ido = f'{ora}:{perc}'
                        if perc > 60:
                            ora += 1
                            perc = perc % 60
                        if perc == 60:
                            ora += 1
                            perc = 0
                            ido = f'{ora}:{perc}0'
                        if perc >= 1 and perc < 10:
                            ido = f'{ora}:0{perc}'
                        print(f'Energia: {energia}%', end='\t\t')
                        print(f'Veszély: {veszely}%', end='\t\t')
                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                        print(f'{ido}', end='\t\t')
                        print(f'XP: {xp}')
                        hely = aluljaro()
                        v = input('Hova szeretnél menni? ')
                        if v == '1':
                            os.system('cls')
                            perc += 5
                            ido = f'{ora}:{perc}'
                            if perc > 60:
                                ora += 1
                                perc = perc % 60
                            if perc == 60:
                                ora += 1
                                perc = 0
                                ido = f'{ora}:{perc}0'
                            if perc >= 1 and perc < 10:
                                ido = f'{ora}:0{perc}'
                            energia -= 2
                            print(f'Energia: {energia}%', end='\t\t')
                            print(f'Veszély: {veszely}%', end='\t\t')
                            print(f'Egyenleg: {penz}Ft', end='\t\t')
                            print(f'{ido}', end='\t\t')
                            print(f'XP: {xp}')
                            hely = vasutallomas()
                            v = input('Megveszed a jegyet? ')
                            if v == '1':
                                pass
                            elif v == '2':
                                energia -= 2
                                perc += 5
                                ido = f'{ora}:{perc}'
                                if perc > 60:
                                    ora += 1
                                    perc = perc % 60
                                if perc == 60:
                                    ora += 1
                                    perc = 0
                                    ido = f'{ora}:{perc}0'
                                if perc >= 1 and perc < 10:
                                    ido = f'{ora}:0{perc}'
                        elif v == '2':
                            os.system('cls')
                            perc += 5
                            ido = f'{ora}:{perc}'
                            if perc > 60:
                                ora += 1
                                perc = perc % 60
                            if perc == 60:
                                ora += 1
                                perc = 0
                                ido = f'{ora}:{perc}0'
                            if perc >= 1 and perc < 10:
                                ido = f'{ora}:0{perc}'
                            energia -= 2
                            print(f'Energia: {energia}%', end='\t\t')
                            print(f'Veszély: {veszely}%', end='\t\t')
                            print(f'Egyenleg: {penz}Ft', end='\t\t')
                            print(f'{ido}', end='\t\t')
                            print(f'XP: {xp}')
                            hely = allomasiDohi()
                            if rablas == 1:
                                os.system('cls')
                                penz -= elvettPenz
                                energia -= bukottEnergia
                                ora += 1
                                perc += 30
                                ido = f'{ora}:{perc}'
                                if perc > 60:
                                    ora += 1
                                    perc = perc % 60
                                if perc == 60:
                                    ora += 1
                                    perc = 0
                                    ido = f'{ora}:{perc}0'
                                if perc >= 1 and perc < 10:
                                    ido = f'{ora}:0{perc}'
                                print(f'Energia: {energia}%', end='\t\t')
                                print(f'Veszély: {veszely}%', end='\t\t')
                                print(f'Egyenleg: {penz}Ft', end='\t\t')
                                print(f'{ido}', end='\t\t')
                                print(f'XP: {xp}')
                                print(f'\nAhogy kiértél az aluljáróból megtámadt egy c-típusú usb és kirabolt. (-{elvettPenz} Ft, -{bukottEnergia}% energia)')
                                input('\nENTER')
                                os.system('cls')
                            else:
                                os.system('cls')
                            print(f'Energia: {energia}%', end='\t\t')
                            print(f'Veszély: {veszely}%', end='\t\t')
                            print(f'Egyenleg: {penz}Ft', end='\t\t')
                            print(f'{ido}', end='\t\t')
                            print(f'XP: {xp}')
                            v = '6'
                            while v == '6':
                                os.system('cls')
                                print(f'Energia: {energia}%', end='\t\t')
                                print(f'Veszély: {veszely}%', end='\t\t')
                                print(f'Egyenleg: {penz}Ft', end='\t\t')
                                print(f'{ido}', end='\t\t')
                                print(f'XP: {xp}')
                                hely = allomasiDohi()
                                esemeny = allomasiDohi2()
                                v = input('Hova szeretnél menni? ')
                                match v:
                                    case '1':
                                        os.system('cls')
                                        energia -= 2
                                        perc += 10
                                        ido = f'{ora}:{perc}'
                                        if perc > 60:
                                            ora += 1
                                            perc = perc % 60
                                        if perc == 60:
                                            ora += 1
                                            perc = 0
                                            ido = f'{ora}:{perc}0'
                                        if perc >= 1 and perc < 10:
                                            ido = f'{ora}:0{perc}'
                                        print(f'Energia: {energia}%', end='\t\t')
                                        print(f'Veszély: {veszely}%', end='\t\t')
                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                        print(f'{ido}', end='\t\t')
                                        print(f'XP: {xp}')
                                        while v == '1':
                                            os.system('cls')
                                            perc += 5
                                            ido = f'{ora}:{perc}'
                                            if perc > 60:
                                                ora += 1
                                                perc = perc % 60
                                            if perc == 60:
                                                ora += 1
                                                perc = 0
                                                ido = f'{ora}:{perc}0'
                                            if perc >= 1 and perc < 10:
                                                ido = f'{ora}:0{perc}'
                                            energia -= 2
                                            if energia > 100:
                                                energia = 100
                                            print(f'Energia: {energia}%', end='\t\t')
                                            print(f'Veszély: {veszely}%', end='\t\t')
                                            print(f'Egyenleg: {penz}Ft', end='\t\t')
                                            print(f'{ido}', end='\t\t')
                                            print(f'XP: {xp}')
                                            hely = belvaros()
                                            v = input('Hova szeretnél menni? ')
                                            match v:
                                                case '1':
                                                    if penz < 700:
                                                        os.system('cls')
                                                        print(f'Energia: {energia}%', end='\t\t')
                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                        print(f'{ido}', end='\t\t')
                                                        print(f'XP: {xp}')
                                                        print('Nincs elég pénzed kaját venni!')
                                                        v = '1'
                                                        input('\nENTER')
                                                    else:
                                                        os.system('cls')
                                                        penz -= 700
                                                        energia += 15
                                                        if energia > 100:
                                                            energia = 100
                                                        perc += 5
                                                        if perc > 60:
                                                            ora += 1
                                                            perc = perc % 60
                                                        if perc == 60:
                                                            ora += 1
                                                            perc = 0
                                                            ido = f'{ora}:{perc}0'
                                                        if perc >= 1 and perc < 10:
                                                            ido = f'{ora}:0{perc}'
                                                        print(f'Energia: {energia}%', end='\t\t')
                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                        print(f'{ido}', end='\t\t')
                                                        print(f'XP: {xp}')
                                                        print('Vettél kaját. (-700 Ft, +15% energia)')
                                                        v = '1'
                                                        input('\nENTER')
                                    case '2':
                                        energia -= 2
                                        perc += 10
                                        ido = f'{ora}:{perc}'
                                        if perc > 60:
                                            ora += 1
                                            perc = perc % 60
                                        if perc == 60:
                                            ora += 1
                                            perc = 0
                                            ido = f'{ora}:{perc}0'
                                        if perc >= 1 and perc < 10:
                                            ido = f'{ora}:0{perc}'
                                        os.system('cls')
                                        hely = main()
                        elif v == '3':
                            perc += 5
                            ido = f'{ora}:{perc}'
                            if perc > 60:
                                ora += 1
                                perc = perc % 60
                            if perc == 60:
                                ora += 1
                                perc = 0
                                ido = f'{ora}:{perc}0'
                            if perc >= 1 and perc < 10:
                                ido = f'{ora}:0{perc}'
                            energia -= 2
                            hely = main()
                    case '3':
                        os.system('cls')
                        energia -= 2
                        perc += 15
                        ido = f'{ora}:{perc}'
                        if perc > 60:
                            ora += 1
                            perc = perc % 60
                        if perc == 60:
                            ora += 1
                            perc = 0
                            ido = f'{ora}:{perc}0'
                        if perc >= 1 and perc < 10:
                            ido = f'{ora}:0{perc}'
                        print(f'Energia: {energia}%', end='\t\t')
                        print(f'Veszély: {veszely}%', end='\t\t')
                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                        print(f'{ido}', end='\t\t')
                        print(f'XP: {xp}')
                        hely = plaza()
                        v = input('Hova szeretnél menni? ')
                        if v == '1':
                            pass
        main()
    case '2':
        os.system('cls')
        print('Köszönjük hogy benéztél.')

def lose():
    if energia > 100:
        energia = 100
    elif energia < 0 or energia == 0:
        energia = 0
        lose = True
        print('Vesztettél!')
        v = input('Szeretnéd újrakezdeni? ')
        match v:
            case '1':
                pass
    if penz < 0 or penz == 0:
        penz = 0
        lose = True
        print('Vesztettél!')
        v = input('Szeretnéd újrakezdeni? ')
        match v:
            case '1':
                pass
def win():
    pass
