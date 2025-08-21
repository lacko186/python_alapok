import random

class Orkok:
    def __init__(self,id, nev, feladat, képesség, erő, fegyver, élet):
        self.id = id 
        self.nev = nev
        self.feladat = feladat
        self.képesség = képesség
        self.erő = erő
        self.fegyver = fegyver
        self.élet = élet

orklista = []

szimplaork = Orkok(6,'Szimpla ork', 'Megszerezni a gyűrűt, elpusztítani mindenkit', 'Megállíthatatlan ameddig él harcol', 100,['kés', 'kard'], 140)
góliátork = Orkok(7,'5 méter magas ork', 'Megszerezni a gyűrűt, elpusztítani mindenkit', 'Megállíthatatlan ameddig él harcol', 300,['erő', 'magasság'], 300)
Szaruman = Orkok(8,'Szaruman Sötét mágus', 'Megszerezni a gyűrűt, elpusztítani mindenkit', 'Hatalmas mágiákat ismer', 600,['Varázsbot', 'kard'], 500)
Szauron = Orkok(9,'Szauron az orkok vezére', 'Megszerezni a gyűrűt, uralkodni középfölde felett', 'Rendkívül erős', 800,['irányítás', 'lát mindent'], 1000)

orklista.append(szimplaork)
orklista.append(góliátork)
orklista.append(Szaruman)
orklista.append(Szauron)

randomharcos = random.randint(6,9)
def valasztottork(orklista):
    orkneve = ''
    for orkok in orklista:
            if orkok.id == randomharcos:
                orkneve = orkok.nev
                break
    return orkneve

def orkkepessege(orklista):
     for orkok in orklista:
          if orkok.id == randomharcos:
               print(f'Középfölde egy rusnya teremtésével van dolgod \n ork feladata: {orkok.feladat}\n képességek:\n Életerő: {orkok.élet}\n Ereje: {orkok.erő}\n Fegyverei/képességei: {orkok.fegyver}')

        
          