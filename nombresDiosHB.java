/*
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
*/

/*
 * Esta version es una especie de hibrido
 * 
 */

//package nombresdioshb;

import java.util.concurrent.atomic.AtomicLong;
import java.util.concurrent.atomic.AtomicInteger;

/**
 *
 * @author josemi
 */
public class nombresDiosHB {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        		final int CAR = 13;
		final int POS = 9;
		final int MAXBLOCK = 3;

        // somos atomicos!!!
        final AtomicLong sumMT = new AtomicLong(0);
        final AtomicLong sumOKMT = new AtomicLong(0);
        final AtomicInteger thNum = new AtomicInteger(0);

        long begin = System.currentTimeMillis();

        for (int iTh = 0; iTh < CAR; iTh++)
        {

            // cada thread tiene
            int cell[] = new int[POS];
            boolean ended = false;
            long sum = 0;
            long sumOK = 0;

            cell[POS-1]=thNum.getAndIncrement();
            //System.out.println("Arrancado thread "+cell[POS-1]);

            do
            {
                sum++;

                boolean numOK = true;
                for(int k=0; (numOK) && (k<POS-MAXBLOCK);k++)
                {
                    numOK = false;
                    for(int e = k + 1; (!numOK) && (e < k+MAXBLOCK+1); e++)
                    {
                        //System.out.println("k: "+k+" e: "+e);
                        if(cell[k]!=cell[e])
                        {
                            //System.out.println("Verdad");
                            numOK = true;
                        }
                    }

                }


                if(numOK)
                {
                    sumOK++;
                    /*
                    StringBuffer a= new StringBuffer();
                    for(int j=POS-1;j>=0;j--)
                    {
                        a.append((char)(65+cell[j]));
                    }
                    System.out.println(a);
                    */
                }


                cell[0]++;
                int i=0;
                while(cell[i]>=CAR)
                {
                    cell[i]=0;
                    i++;
                    // ojo, ahora llegamos a POS-1, POS esta fijado para
                    // el thread
                    if(i<POS-1)
                    {
                        cell[i]++;
                    }
                    else
                    {
                        ended = true;
                        break;
                    }
                }

            } while(!ended);

            // hemos acabado para este thread, sumamos
            sumMT.getAndAdd(sum);
            sumOKMT.getAndAdd(sumOK);


        }  // del for


		long end = System.currentTimeMillis();

		System.out.println("HB Sum   "+sumMT);

		System.out.println("HB SumOK "+sumOKMT);

		System.out.println("HB Time: "+(end-begin));


    }

}
