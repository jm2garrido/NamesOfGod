#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
NamesOfGod

Caller para cython
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

import time
import sys
#import nd_naive
#import nd_stage_1
import nd_stage_2

if __name__ == '__main__':
    #las constantes
    CAR = 13
    POS = 9
    MAXBLOCK = 3

    if len(sys.argv) == 4:
        car = int(sys.argv[1])
        pos = int(sys.argv[2])
        maxblock = int(sys.argv[3])
    else:
        car = CAR
        pos = POS
        maxblock = MAXBLOCK

    print("Caracteres:   {}".format(car))
    print("Posiciones:   {}".format(pos))
    print("Repeticiones: {}".format(maxblock))


    # aqui podria ser clock. pero eso mide el processor time en muchos sistemas
    # por coherencia con otras versiones, queremos medir el wall-time
    # ojo, la version en C usa clock
    begin = time.time()

    #sum_, sumOK = nd_naive.nombresDios(car,pos,maxblock)
    sum_, sumOK = nd_stage_2.nombresDios(car,pos,maxblock)

    #acabados los calculos, pongo los resultados

    end = time.time()

    print("Sum   {0}".format(sum_))
    print("SumOK {0}".format(sumOK))
    print("Time: {0}".format((end-begin)*1000))