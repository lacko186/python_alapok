print('Automata')

def osszes_csoki(lista):
    for csoki in lista:
        print(f'{csoki["id"]} - {csoki["nev"]} - {csoki["ar"]} Ft')

def csoki_vasarlas(lista):
    while True:
        valasztott_id = int(input('Add meg a választott csokoládé azonosítóját (1-6): '))
            
        if 1 <= valasztott_id <= len(lista):
            valasztott_csoki = lista[valasztott_id - 1] 
                
            print(f'A választott termék: {valasztott_csoki["nev"]}. Ára: {valasztott_csoki["ar"]} Ft.')
                
            cimletek = [500, 1000, 2000, 5000, 10000, 20000]
            kp = int(input(f'Add meg a címletet amivel szeretnél fizetni. Elfogadott címletek: {cimletek}: '))
                
            if kp < valasztott_csoki['ar']:
                print('A megadott címlet nem elég a vásárláshoz. Kérlek adj meg egy nagyobb címletet.')
                 
            visszajaro = kp - valasztott_csoki['ar']
            print(f'Sikeres vásárlás! A visszajáró: {visszajaro} Ft.')
            return 
            
        else:
            print('Hibás azonosító! Kérlek válassz az 1 és 6 közötti számok közül.')

def kilepes():
    print('Kilépés az automatából. Viszlát!')
    return False

vasarlas = True
lista = [
    {'id': 1, 'nev': 'Kinderbueno', 'ar': 400},
    {'id': 2, 'nev': 'Bounty', 'ar': 400},
    {'id': 3, 'nev': 'Brownie', 'ar': 1000},
    {'id': 4, 'nev': 'Milka', 'ar': 900},
    {'id': 5, 'nev': 'Kitkat', 'ar': 500},
    {'id': 6, 'nev': 'Raffaello', 'ar': 1600}
]

while vasarlas:
    print('\nAutomata')
    print('1. Csokoládé vásárlás')
    print('2. Összes csokoládé megjelenítése')
    print('3. Kilépés')
    
    opcio = int(input('Választott: '))
        
    if opcio == 1:
        csoki_vasarlas(lista)
    elif opcio == 2:
        osszes_csoki(lista)
    elif opcio == 3:
        vasarlas = kilepes()
    else:
        print('Hibás választás!')
            
    