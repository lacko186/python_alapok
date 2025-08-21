import random
import ork
from ork import orklista 

class Harcos:
    def __init__(self,id, nev, feladat, képesség, erő, fegyver, élet,sebzes):
        self.id = id 
        self.nev = nev
        self.feladat = feladat
        self.képesség = képesség
        self.erő = erő
        self.fegyver = fegyver
        self.élet = élet
        self.sebzes = sebzes
hobbitok = []
Frodó =  Harcos(1,'Frodó', 'Eljuttatni a gyűrűt mordorba, elpusztítani', 'Gyorsan tud futni', 400, ['kard', 'kő', 'testi erő'], 300, 200)
Samu =  Harcos(2,'Samu', 'Segíteni frodónak eljuttatni a gyűrűt mordorba, elpusztítani', 'Gyorsan tud futni', 400, ['kard', 'kő', 'testi erő'],300, 200)
Gandalf = Harcos(3,'Gandalf', "Megállítani Szauron seregeit", "Aa mágia mestere", 800, ['Varázsbot', 'Kard'], 500, 750)
Legolasz = Harcos(4,'Legolasz', "Megállítani mordor seregeit","Az íj és a nyíl mestere tündeként tökéletesen kezeli", 670, ['íj', 'Nyíl', 'Kard'],600, 480)
Vándor =Harcos(5,'Aragorn', 'Megállítani mordor seregeit', 'Tündék által kovácsolt kardot mesterien forgatja', 810, ['kard'],650, 600)
Galadrielurno = (6, 'Galadriel', 'A tündék legerősebbike', 'A mágia legmagasabb szintjén van Szauronnál erősebb', 1300, ['varászlat', 'tündemágia', 'ősi erők'],1300, 800)

hobbitok.append(Frodó)
hobbitok.append(Samu)
hobbitok.append(Gandalf)
hobbitok.append(Legolasz)
hobbitok.append(Vándor)


randomharcos = random.randint(1,5)
def valasztottharcos(hobbitok):
    harcosneve = ''
    for harcos in hobbitok:
            if harcos.id == randomharcos:
                harcosneve = harcos.nev
                break
    return harcosneve

def harcoskepessege(hobbitok):
     for harcos in hobbitok:
          if harcos.id == randomharcos:
               print(f'Védd meg középföldét \n harcos feladata: {harcos.feladat}\n képességek:\n Életerő: {harcos.élet}\n Ereje: {harcos.erő}\n Fegyverei/képességei: {harcos.fegyver}')


               
               