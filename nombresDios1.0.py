"""
NamesOfGod

Copyright (C) 2016 Jose Miguel Garrido

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import time
import array

#las constantes
CAR = 13
POS = 6
MAXBLOCK = 3

#estos numeros pueden ser grandes, mas de 32 bits
# hay que usar los numeros de precision arbitraria
sum = 0L
sumOK = 0L

# matriz eficiente de enteros
cell = array.array('i')

for i in range(POS):
    cell.append(0)

ended = False

# aqui podria ser clock. pero eso mide el processor time en muchos sistemas
# por coherencia con otras versiones, queremos medir el wall-time
# ojo, la version en C usa clock
begin = time.time()

while not ended:
    sum+=1L

    numOK = True

    #bucle chapucero para emular el for de java
    k=0
    while ((numOK) and (k<POS-MAXBLOCK)):
        numOK=False
        e = k + 1
        while ((not numOK) and (e < k+MAXBLOCK+1)):
            #print "k: {0} e: {e}".format(k,e)
            if (cell[k]!=cell[e]):
                #print "Verdad"
                numOK =True
            e+=1
        k+=1

    if(numOK):
        sumOK+=1L
        # print cell

    cell[0]+=1

    i=0    
    while(cell[i]>=CAR):
        cell[i]=0
        i+=1
        if i<POS:
            cell[i]+=1
        else:
            ended= True
            break

#acabados los calculos, pongo los resultados

end = time.time()

print "Sum   {0}".format(sum)
print "SumOK {0}".format(sumOK)
print "Time: {0}".format((end-begin)*1000)
        

