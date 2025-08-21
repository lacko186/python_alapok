import random
from ork import orklista, Orkok
from hobbit import hobbitok, Harcos

def randomkarakter(karakterek):
    return random.choice(karakterek)

def harc(ork, harcos):
    print(f"\nA harc elkezdődött {ork.nev} és {harcos.nev} között!")
    
    kezdes = random.choice([ork, harcos])
    if kezdes == ork:
        print("Az ork kezd!")
    else:
        print("A harcos kezd!")

    while ork.élet > 0 and harcos.élet > 0:
        if kezdes == harcos:
            harc_sebzes = harcos.sebzes
            ork.élet -= harc_sebzes
            print(f"{harcos.nev} megtámadta {ork.nev} karaktert. {harc_sebzes} sebzést okozott!")
            print(f"{ork.nev} élete: {ork.élet}")
            kezdes = ork
        else:
            harc_sebzes = ork.erő
            harcos.élet -= harc_sebzes
            print(f"{ork.nev} megtámadta {harcos.nev} karaktert. {harc_sebzes} sebzést okozott!")
            print(f"{harcos.nev} élete: {harcos.élet}")
            kezdes = harcos
        

    if ork.élet <= 0:
        print(f"Gratulálok! {harcos.nev} győzött!")
    else:
        print(f"Sajnálom, {ork.nev} győzött. Középfölde veszélyben van.")

print('Gyűrűk ura')
kezdődhet = input('Kezdődhet a harc? i/n: ')

if kezdődhet.lower() == 'i':
    valasztottork = randomkarakter(orklista)
    valasztottharcos = randomkarakter(hobbitok)

    print(f'\nA választott ork: {valasztottork.nev}\nA választott harcos: {valasztottharcos.nev}')

    print('\nAz ork képességei:')
    print(f'Név: {valasztottork.nev}\nFeladat: {valasztottork.feladat}\nÉleterő: {valasztottork.élet}\nErő: {valasztottork.erő}\nFegyverei/képességei: {valasztottork.fegyver}')
    
    print('\nA harcos képességei:')
    print(f'Név: {valasztottharcos.nev}\nFeladat: {valasztottharcos.feladat}\nÉleterő: {valasztottharcos.élet}\nErő: {valasztottharcos.erő}\nFegyverei/képességei: {valasztottharcos.fegyver}')

    harc(valasztottork, valasztottharcos)

else:
    print('viszlát!')