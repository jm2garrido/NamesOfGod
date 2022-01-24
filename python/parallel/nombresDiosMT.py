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

# Version para python 3
# 2016-5-1

import time
import array
import threading
import logging

def check_and_generate(first_number):
    # internal values of each thread
    global sumMT
    global sumOKMT
    global lock

    #logging.info("Entering {0}".format(threading.current_thread().name))
    sum = 0
    sumOK = 0
    cell = array.array('i')

    for i in range(POS-1):
        cell.append(0)
    cell.append(first_number)

    ended = False

    while not ended:
        sum+=1

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
            sumOK+=1
            # print cell

        cell[0]+=1

        i=0    
        while(cell[i]>=CAR):
            cell[i]=0
            i+=1
            # POS-1, POS is now fixed in thread
            if i<POS-1:
                cell[i]+=1
            else:
                ended= True
                break
    # while ended, adding up the results

    with lock:    
        sumMT += sum
        sumOKMT += sumOK

    #logging.info("exiting {0} {1} {2}".format(threading.current_thread().name,sumMT,sumOKMT))


#las constantes 13, 9, 3
CAR = 13
POS = 7
MAXBLOCK = 3

#estos numeros pueden ser grandes, mas de 32 bits
#compartidos para todos los threads
sumMT = 0
sumOKMT = 0

lock = threading.Lock()

logging.basicConfig(level=logging.INFO)

print("Caracteres:   {}".format(CAR))
print("Posiciones:   {}".format(POS))
print("Repeticiones: {}".format(MAXBLOCK))

# aqui podria ser clock. pero eso mide el processor time en muchos sistemas
# por coherencia con otras versiones, queremos medir el wall-time
# ojo, la version en C usa clock
begin = time.time()

workers = []
for n in range(CAR):
    t = threading.Thread(target=check_and_generate,name=str(n), args= (n,))
    workers.append(t)
    t.start()

for i in workers:
    i.join()

#acabados los calculos, pongo los resultados

end = time.time()

print ("Sum   {0}".format(sumMT))
print ("SumOK {0}".format(sumOKMT))
print ("Time: {0}".format((end-begin)*1000))
        

