import time

print('időzítő')

ora = int(input('Add meg az órák számát: '))
perc = int(input('Add meg a percek számát: '))
mp = int(input('Add meg a másodpercek számát: '))

while True:
    for h in range(ora, -1, -1):
        for m in range(perc, -1, -1):
            for s in range(mp, -1, -1):
                print(f'{h:02}:{m:02}:{s:02}')
                time.sleep(1)
            mp = 59
        perc = 59
    ora = 0
    print('Idő lejárt!')
    break


