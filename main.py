import os, random
from helyek import videki, galaxy, aluljaro, vasutallomas, allomasiDohi, allomasiDohi2, plaza, belvaros, baross_ut, baross_ut2, meki, kfc, dunaKapuTer

winValue = False
loseValue = False

def lose():
    global energia
    global penz
    global perc
    global ora
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

print('Győr szimulátor') 
print('1: Start')
print('2: Kilépés')
v = input('Választás: ')

def main():
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
    global eneklosCsavo
    global munkaido
    global maxMunkaido
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
            rablas = random.randint(1,10)
            elvettPenz = random.randint(100, 1500)
            bukottEnergia = random.randint(0,35)
            eneklosCsavo = random.randint(1, 10)
            munkaido = 0
            maxMunkaido = 6
            def jatek():
                while winValue == False and loseValue == False:
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
                    global eneklosCsavo
                    global munkaido
                    global maxMunkaido
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
                                if rablas > 0 and rablas < 6:
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
                                            b = ''
                                            while b == '':
                                                os.system('cls')
                                                perc += 10
                                                energia -= 2
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
                                                            b = '2'
                                                            input('\nENTER')
                                                    case '2':
                                                        bs = ''
                                                        while bs == '':
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
                                                            hely = baross_ut()
                                                            if eneklosCsavo > 0 and eneklosCsavo < 4:
                                                                print('\nTalálkoztál az éneklős Csávóval.')
                                                                input('\nENTER')
                                                                os.system('cls')
                                                                print(f'Energia: {energia}%', end='\t\t')
                                                                print(f'Veszély: {veszely}%', end='\t\t')
                                                                print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                print(f'{ido}', end='\t\t')
                                                                print(f'XP: {xp}')
                                                                print('\n1: Igen (200 Ft)')
                                                                print('2: Nem')
                                                                v = input('Adsz neki pénzt? ')
                                                                match v:
                                                                    case '1':
                                                                        os.system('cls')
                                                                        penz -= 200
                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                        print(f'{ido}', end='\t\t')
                                                                        print(f'XP: {xp}')
                                                                        print('\nNagyon örült neki, megköszönte és elment. (-200 Ft)')
                                                                        br = '1'
                                                                        input('\nENTER')
                                                                    case '2':
                                                                        os.system('cls')
                                                                        veszely += 5
                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                        print(f'{ido}', end='\t\t')
                                                                        print(f'XP: {xp}')
                                                                        print(f'\nNem tetted boldoggá, a veszélyszinted értéke ennyire emelkedett: {veszely}%')
                                                                        br = '1'
                                                                        input('\nENTER')
                                                                    case '17.10.43.35.31':
                                                                        os.system('cls')
                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                        print(f'{ido}', end='\t\t')
                                                                        print(f'XP: {xp}')
                                                                        nev = input('Írd be a neved: ')
                                                                        input('\nENTER')
                                                                        os.system('cls')
                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                        print(f'{ido}', end='\t\t')
                                                                        print(f'XP: {xp}')
                                                                        print('\nTe: Szerintem a Dézsit megkéne ölni.')
                                                                        print('\nÉneklős Csávó: Hogy hívnak?')
                                                                        print(f'\nTe: {nev}')
                                                                        print(f'\nÉneklős Csávó: {nev}, tetszik a neved.')
                                                                        input('\nENTER')
                                                                        os.system('cls')
                                                                        xp += 5
                                                                        maxMunkaido = 9
                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                        print(f'{ido}', end='\t\t')
                                                                        print(f'XP: {xp}')
                                                                        print(f'\nAz éneklős Csávó megáldott téged. A tapasztalati szinted {xp}-re növekedett. A napi max munkaidő 9 órára emelkedett.')
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
                                                                        br = '1'
                                                                        input('\nENTER')
                                                            br = '1'
                                                            while br == '1':
                                                                os.system('cls')
                                                                print(f'Energia: {energia}%', end='\t\t')
                                                                print(f'Veszély: {veszely}%', end='\t\t')
                                                                print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                print(f'{ido}', end='\t\t')
                                                                print(f'XP: {xp}')
                                                                hely = baross_ut()
                                                                esemeny = baross_ut2()
                                                                v = input('Hova szeretnél menni? ')
                                                                match v:
                                                                    case '1':
                                                                        k = ''
                                                                        while k == '':
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
                                                                            hely = kfc()
                                                                            v = input('Mit fogsz csinálni? ')
                                                                            match v:
                                                                                case '1':
                                                                                    os.system('cls')
                                                                                    if penz < 2000:
                                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                                        print(f'{ido}', end='\t\t')
                                                                                        print(f'XP: {xp}')
                                                                                        print('\nNincs elég pénzed kajára.')
                                                                                        k = ''
                                                                                        perc -= 5
                                                                                        energia += 2
                                                                                        input('\nENTER')
                                                                                    else:
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
                                                                                        energia += 30
                                                                                        if energia > 100:
                                                                                            energia = 100
                                                                                        penz -= 2000
                                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                                        print(f'{ido}', end='\t\t')
                                                                                        print(f'XP: {xp}')
                                                                                        print('\nEttél a KFC-ben. (-2000Ft, +30% energia)')
                                                                                        k = ''
                                                                                        energia += 2
                                                                                        input('\nENTER')
                                                                                        os.system('cls')
                                                                                case '2':
                                                                                    os.system('cls')
                                                                                    if munkaido == maxMunkaido:
                                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                                        print(f'{ido}', end='\t\t')
                                                                                        print(f'XP: {xp}')
                                                                                        print('\nMa már elérted a max munkaidődet. (6 óra)')
                                                                                        perc -= 5
                                                                                        energia += 2
                                                                                        k = ''
                                                                                        input('\nENTER')
                                                                                    elif energia < 35:
                                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                                        print(f'{ido}', end='\t\t')
                                                                                        print(f'XP: {xp}')
                                                                                        print('\nNincs elég energiád a munkához. (min. 35%)')
                                                                                        perc -= 5
                                                                                        energia += 2
                                                                                        k = ''
                                                                                        input('\nENTER')
                                                                                    else:
                                                                                        ora += 1
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
                                                                                        energia -= 20
                                                                                        munkaido += 1
                                                                                        penz += 1000
                                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                                        print(f'{ido}', end='\t\t')
                                                                                        print(f'XP: {xp}')
                                                                                        print('\nDolgoztál egy órát a KFC-ben. (+1000Ft, -20% energia)')
                                                                                        k = ''
                                                                                        perc -= 5
                                                                                        energia += 2
                                                                                        input('\nENTER')
                                                                                case '3':
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
                                                                                    k = '1'
                                                                                    br = '1'
                                                                                case default:
                                                                                    os.system('cls')
                                                                                    print(f'Energia: {energia}%', end='\t\t')
                                                                                    print(f'Veszély: {veszely}%', end='\t\t')
                                                                                    print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                                    print(f'{ido}', end='\t\t')
                                                                                    print(f'XP: {xp}')
                                                                                    print('\nNincs ilyen választás.')
                                                                                    input('\nENTER')
                                                                                    perc -= 5
                                                                                    energia += 2
                                                                                    k = ''
                                                                    case '2':
                                                                        m = ''
                                                                        while m == '':
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
                                                                            hely = meki()
                                                                            v = input('Mit fogsz csinálni? ')
                                                                            match v:
                                                                                case '1':
                                                                                    os.system('cls')
                                                                                    if penz < 2500:
                                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                                        print(f'{ido}', end='\t\t')
                                                                                        print(f'XP: {xp}')
                                                                                        print('\nNincs elég pénzed kajára.')
                                                                                        m = ''
                                                                                        perc -= 5
                                                                                        energia += 2
                                                                                        input('\nENTER')
                                                                                    else:
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
                                                                                        energia += 35
                                                                                        if energia > 100:
                                                                                            energia = 100
                                                                                        penz -= 2500
                                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                                        print(f'{ido}', end='\t\t')
                                                                                        print(f'XP: {xp}')
                                                                                        print('\nEttél a Mekiben. (-2500Ft, +35% energia)')
                                                                                        m = ''
                                                                                        energia += 2
                                                                                        input('\nENTER')
                                                                                        os.system('cls')
                                                                                case '2':
                                                                                    os.system('cls')
                                                                                    if munkaido == maxMunkaido:
                                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                                        print(f'{ido}', end='\t\t')
                                                                                        print(f'XP: {xp}')
                                                                                        print('\nMa már elérted a max munkaidődet. (6 óra)')
                                                                                        perc -= 5
                                                                                        energia += 2
                                                                                        m = ''
                                                                                        input('\nENTER')
                                                                                    elif energia < 35:
                                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                                        print(f'{ido}', end='\t\t')
                                                                                        print(f'XP: {xp}')
                                                                                        print('\nNincs elég energiád a munkához. (min. 35%)')
                                                                                        perc -= 5
                                                                                        energia += 2
                                                                                        m = ''
                                                                                        input('\nENTER')
                                                                                    else:
                                                                                        ora += 1
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
                                                                                        energia -= 20
                                                                                        munkaido += 1
                                                                                        penz += 1250
                                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                                        print(f'{ido}', end='\t\t')
                                                                                        print(f'XP: {xp}')
                                                                                        print('\nDolgoztál egy órát Mekiben. (+1250Ft, -20% energia)')
                                                                                        m = ''
                                                                                        perc -= 5
                                                                                        energia += 2
                                                                                        input('\nENTER')
                                                                                case '3':
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
                                                                                    m = '1'
                                                                                    br = '1'
                                                                                case default:
                                                                                    os.system('cls')
                                                                                    print(f'Energia: {energia}%', end='\t\t')
                                                                                    print(f'Veszély: {veszely}%', end='\t\t')
                                                                                    print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                                    print(f'{ido}', end='\t\t')
                                                                                    print(f'XP: {xp}')
                                                                                    print('\nNincs ilyen választás.')
                                                                                    input('\nENTER')
                                                                                    perc -= 5
                                                                                    energia += 2
                                                                                    m = ''
                                                                    case '3':
                                                                        br = '2'
                                                                        bs = '2'
                                                                        b = ''
                                                                    case default:
                                                                        os.system('cls')
                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                        print(f'{ido}', end='\t\t')
                                                                        print(f'XP: {xp}')
                                                                        print('\nNincs ilyen választás.')
                                                                        input('\nENTER')
                                                                        br = '1'
                                                    case '3':
                                                        d = ''
                                                        while d == '':
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
                                                            hely = dunaKapuTer()
                                                            v = input('Eszel fagyit? ')
                                                            match v:
                                                                case '1':
                                                                    os.system('cls')
                                                                    print(f'Energia: {energia}%', end='\t\t')
                                                                    print(f'Veszély: {veszely}%', end='\t\t')
                                                                    print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                    print(f'{ido}', end='\t\t')
                                                                    print(f'XP: {xp}')
                                                                    gomboc = 0
                                                                    v = int(input('Hány gombócot eszel? '))
                                                                    gomboc = v
                                                                    if penz < gomboc * 650:
                                                                        os.system('cls')
                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                        print(f'{ido}', end='\t\t')
                                                                        print(f'XP: {xp}')
                                                                        print(f'\nNincs elég pénzed ennyi gombócra. ({gomboc * 650}Ft)')
                                                                        d = ''
                                                                        perc -= 5
                                                                        energia += 2
                                                                        input('\nENTER')
                                                                    elif penz < 650:
                                                                        os.system('cls')
                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                        print(f'{ido}', end='\t\t')
                                                                        print(f'XP: {xp}')
                                                                        print('\nNincs elég pénzed fagyira. (650Ft)')
                                                                        d = ''
                                                                        perc -= 5
                                                                        energia += 2
                                                                        input('\nENTER')
                                                                    else:
                                                                        os.system('cls')
                                                                        penz -= gomboc * 650
                                                                        perc += gomboc * 5
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
                                                                        energia += gomboc * 10
                                                                        if energia > 100:
                                                                            energia = 100
                                                                        print(f'Energia: {energia}%', end='\t\t')
                                                                        print(f'Veszély: {veszely}%', end='\t\t')
                                                                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                                                                        print(f'{ido}', end='\t\t')
                                                                        print(f'XP: {xp}')
                                                                        print(f'\nEttél {gomboc} gombóc fagyit. (-{gomboc * 650}Ft, +{gomboc * 10}% energia)')
                                                                        d = ''
                                                                        perc -= 5
                                                                        energia += 2
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
                                            hely = jatek()
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
                                hely = jatek()
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
            jatek()
        case '2':
            os.system('cls')
            print('Köszönjük hogy benéztél.')
main()


def win():
    pass
