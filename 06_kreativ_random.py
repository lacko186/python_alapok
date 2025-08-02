import random

jelszó = int(input('Kérem adjon meg egy jelszót: '))

tipp = 0
print('A számítógép nem látja a jelszavad')
print('kitalálom a jelszavad...')

while tipp != jelszó:
    print(tipp)
    tipp = random.randint(0,99999999)
    if tipp == jelszó:
        print(tipp)
    else:
        tipp = random.randint(0,99999999)

print(f'A jelszavad {tipp} volt')