/*
 *      nombresDios1_0.c
 *
 *      Copyright 2009 josemi <josemi@darksun>
 *
 *      This program is free software; you can redistribute it and/or modify
 *      it under the terms of the GNU General Public License as published by
 *      the Free Software Foundation; either version 2 of the License, or
 *      (at your option) any later version.
 *
 *      This program is distributed in the hope that it will be useful,
 *      but WITHOUT ANY WARRANTY; without even the implied warranty of
 *      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *      GNU General Public License for more details.
 *
 *      You should have received a copy of the GNU General Public License
 *      along with this program; if not, write to the Free Software
 *      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 *      MA 02110-1301, USA.
 */
package main

import (
	"fmt"
	"reflect"
	"time"
)

func main() {
	const CAR = 13
	const POS = 9
	const MAXBLOCK = 3

	// This numbers can be really big, we need a 64 bits integer
	// automatically initialized to 0
	var sum int64
	var sumOK int64

	// an array, fix size
	var cell [POS]int
	ended := false

	fmt.Printf("Version %d, CAR %d, POS %d, MAXBLOCK %d\n",
		reflect.TypeOf(CAR).Size()*8, CAR, POS, MAXBLOCK)

	start := time.Now()

	for !ended {
		sum++

		numOK := true
		for k := 0; (numOK) && (k < POS-MAXBLOCK); k++ {
			numOK = false
			for e := k + 1; (!numOK) && (e < k+MAXBLOCK+1); e++ {

				if cell[k] != cell[e] {

					numOK = true
				}
			}

		}

		if numOK {
			sumOK++
		}

		cell[0]++
		i := 0
		for cell[i] >= CAR {
			cell[i] = 0
			i++
			if i < POS {
				cell[i]++
			} else {
				ended = true
				break
			}
		}
	}

	elapsed := time.Since(start)

	fmt.Printf("Sum   %d \n", sum)

	fmt.Printf("SumOK %d \n", sumOK)

	fmt.Printf("Time: %s \n", elapsed)
}
