import time

def music(nulladik,elso,masodik,harmadik,negyedik,kesleltetes):
    nulladiksor = nulladik.split() + ['\n']
    elsosor = elso.split() + ['\n']
    masodiksor = masodik.split() + ['\n']
    harmadiksor = harmadik.split() + ['\n']
    negyediksor = negyedik.split() + ['\n']

    for szo in nulladiksor:
        print(szo, end=' ', flush=True)
        time.sleep(kesleltetes)
    for szo in elsosor:
        print(szo, end=' ', flush=True)
        time.sleep(kesleltetes)
    for szo in masodiksor:
        print(szo, end=' ', flush=True)
        time.sleep(kesleltetes)
    for szo in harmadiksor:
        print(szo, end=' ', flush=True)
        time.sleep(kesleltetes)
    for szo in negyediksor:
        print(szo, end=' ', flush=True)
        time.sleep(kesleltetes)

nulladik = ' '
elso = 'I wanna feel the heat, i wanna own the night'
masodik = 'I wanna feel the beat, i wanna dance tonight'
harmadik = 'I wanna lose myself, i wanna come alive'
negyedik = 'I wanna feel the love into overdrive'
kesleltetes = 0.5

music(nulladik,elso,masodik,harmadik,negyedik,kesleltetes)