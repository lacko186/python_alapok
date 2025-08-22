import time 

def feldolgozas(nulladik,elso,masodik,harmadik,negyedik, kesleltetes):
    elsosorkihagy = nulladik.split() + ['\n']
    szavak = elso.split() + ['\n']
    szavakketto = masodik.split() + ['\n']
    szavakharom = harmadik.split() + ['\n']
    szavaknegy = negyedik.split()+ ['\n']
    
    for szo in elsosorkihagy: 
        print(szo, end=' ', flush=True)
    for szo in szavak:
        print(szo, end=' ',flush=True)
        time.sleep(kesleltetes)
    
    for szo in szavakketto:
        print(szo, end=' ',flush=True)
        time.sleep(kesleltetes)
    

    for szo in szavakharom:
        print(szo, end=' ',flush=True)
        time.sleep(kesleltetes)
    
    for szo in szavaknegy:
        print(szo, end=' ',flush=True)
        time.sleep(kesleltetes)
nulladik = ''
elso = 'I wanna feel the heat i wanna own the night'
masodik = 'I wanna feel the beat i wanna dance tonight'
harmadik = 'I wanna lose myself i wanna come alive'
negyedik = ' I wanna feel the love go into overdirve'
kesleltetes= 0.4

feldolgozas(nulladik,elso,masodik,harmadik,negyedik,kesleltetes)