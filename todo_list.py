import time

print('Todo List')
print('Választási lehetőségek: \n1. Új tennivaló hozzáadása \n2. Szerkesztés ID alapján \n3. Kilépés, nyomtatás')

lista = []

def hozzaad():
    print('\n--- Új tennivaló hozzáadása ---')
    teendoneve = input('Add meg a teendő nevét: ')
    teendoleirasa = input('Add meg a teendő leírását: ')
    dokumentumok = input('Van dokumentumod? (i/n): ')
    datum = input('Add meg a teljesítés határidejét (yyyy-mm-dd): ')
    
    uj_teendo = {
        'id': len(lista) + 1,
        'nev': teendoneve,
        'leiras': teendoleirasa,
        'dokumentumok': dokumentumok,
        'hatarido': datum
    }
    
    lista.append(uj_teendo)
    print(f'✓ "{teendoneve}" sikeresen hozzáadva!')

def szerkesztes():
    if not lista:
        print('Nincs szerkeszthető tennivaló!')
        return
    
    print('\n--- Meglévő tennivalók ---')
    for teendo in lista:
        print(f"ID: {teendo['id']} - {teendo['nev']}")
    
    try:
        szerkesztendo_id = int(input('\nAdd meg a szerkesztendő tennivaló ID-ját: '))
        
        talalt = False
        for teendo in lista:
            if teendo['id'] == szerkesztendo_id:
                print(f'\nJelenlegi adatok:')
                print(f"Név: {teendo['nev']}")
                print(f"Leírás: {teendo['leiras']}")
                print(f"Dokumentumok: {teendo['dokumentumok']}")
                print(f"Határidő: {teendo['hatarido']}")
                
                uj_nev = input('\nÚj név (Enter = változatlan): ')
                uj_leiras = input('Új leírás (Enter = változatlan): ')
                uj_dokumentumok = input('Dokumentumok (Enter = változatlan): ')
                uj_datum = input('Új határidő (Enter = változatlan): ')
                
                if uj_nev:
                    teendo['nev'] = uj_nev
                if uj_leiras:
                    teendo['leiras'] = uj_leiras
                if uj_dokumentumok:
                    teendo['dokumentumok'] = uj_dokumentumok
                if uj_datum:
                    teendo['hatarido'] = uj_datum
                
                print('✓ Tennivaló sikeresen frissítve!')
                talalt = True
                break
        
        if not talalt:
            print('Nem található tennivaló ezzel az ID-val!')
            
    except ValueError:
        print('Hibás ID formátum!')

def kilepes_nyomtatas():
    if not lista:
        print('\nNincs megjeleníthető tennivaló!')
    else:
        print('\n' + '='*50)
        print('TENNIVALÓK LISTÁJA')
        print('='*50)
        for teendo in lista:
            print(f"\nID: {teendo['id']}")
            print(f"Név: {teendo['nev']}")
            print(f"Leírás: {teendo['leiras']}")
            print(f"Dokumentumok: {teendo['dokumentumok']}")
            print(f"Határidő: {teendo['hatarido']}")
            print('-' * 30)
    
    print('\nViszlát! 👋')

while True:
    print('\n' + '='*40)
    valasztott = input('\nVálasztott opció (1-3): ')
    
    if valasztott == '1':
        hozzaad()
    elif valasztott == '2':
        szerkesztes()
    elif valasztott == '3':
        kilepes_nyomtatas()
        break
    else:
        print('Hibás választás! Válassz 1, 2 vagy 3 közül.')

print('\nProgram befejezve.')