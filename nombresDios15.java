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
// version 1.5
// esta version tiene un nuevo "comprobador" pero parece 
// que no ha salido muy bien, es peor que con el antiguo

public class nombresDios {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// 13, 9, 3
		final int CAR = 13;
		final int POS = 9;
		final int MAXBLOCK = 3;
		
		long sum = 0;
		long sumOK = 0;
		
		
		int cell[] = new int[POS];
		boolean ended = false;
	
		System.out.println("Caracteres   "+CAR);
		System.out.println("Posiciones   "+POS);
		System.out.println("Repeticiones "+MAXBLOCK);

		long begin = System.currentTimeMillis();
		
		do {	
			sum++;
			
			boolean numOK = true;
			int acc = 1;
			for(int k=1; (k<POS);k++)
			{
				if(cell[k-1]==cell[k])
				{
					acc++;
					if(acc>MAXBLOCK)
					{
						numOK=false;
						break;
					}
				}
				else
				{
					acc=1;
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
				if(i<POS)
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
		
		long end = System.currentTimeMillis();
		
		System.out.println("Sum   "+sum);
		
		System.out.println("SumOK "+sumOK);

		System.out.println("Time: "+(end-begin));
	}

}
