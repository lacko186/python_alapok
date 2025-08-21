import random
import ork 
from ork import orklista
import hobbit
from hobbit import hobbitok


print('Gyűrűk ura')

kezdődhet = input('Kezdődhet a harc? i/n: ')
if kezdődhet == 'i':
    print('\n\t\tA választott ork: ' + ork.valasztottork(orklista)+ '\ta választott harcos: ' + hobbit.valasztottharcos(hobbitok) )
    ork.orkkepessege(orklista)
    print('\n')
    hobbit.harcoskepessege(hobbitok)
else:
    print('viszlát!')
    
         