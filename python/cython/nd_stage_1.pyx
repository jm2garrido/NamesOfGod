#cython: language_level=3, boundscheck=False
"""
NamesOfGod

Typed cython version, using a memory view
"""

__author__ = "Jose Miguel Garrido"
__copyright__ = "(C) 2022 Jose Miguel Garrido"
"""
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

import array

def nombresDios(int car,int pos,int maxblock):
    #estos numeros pueden ser grandes, mas de 32 bits
    # hay que usar los numeros de precision arbitraria
    cdef long long sum_ = 0
    cdef long long sumOK = 0

    cdef bint ended = False, numOK
    cdef int k, e, i

    # matriz eficiente de enteros
    cell_array = array.array('i',pos * [ 0 ])
    # a memory view
    cdef int[:] cell = cell_array

    while not ended:
        sum_+=1

        numOK = True

        #bucle chapucero para emular el for de java
        k = 0
        while ((numOK) and (k<pos-maxblock)):
            numOK=False
            e = k + 1
            while ((not numOK) and (e < k+maxblock+1)):
                #print("k: {0} e: {1}".format(k,e))
                if (cell[k]!=cell[e]):
                    #print("Verdad")
                    numOK =True
                e+=1
            k+=1

        if(numOK):
            sumOK+=1
            # print(cell)

        cell[0]+=1

        i=0    
        while(cell[i]>=car):
            cell[i]=0
            i+=1
            if i<pos:
                cell[i]+=1
            else:
                ended= True
                break
            
    return sum_,sumOK