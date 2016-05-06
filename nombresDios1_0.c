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

/* linux gcc nombresDios1_0.c -march=x86-64 -o nombresDios */

#include <stdio.h>
#include <time.h>

int main(int argc, char** argv)
{
#define CAR  (13)
#define POS  (9)
#define MAXBLOCK  (3)
#define TRUE (1)
#define FALSE (0)
/* esto es la edad media */		
		
		long long sum = 0;
		long long sumOK = 0;
		/* supongo long long 64 bits */
		
		
		int cell[POS];
		int ended = FALSE;
	
		int l,k,j,e;
		/* vaya mierda, tengo que declarar esto aqui */
	
		for(l=0; l<POS;l++) cell[l]=0;
		/* la edad media, no hay duda */
		
		printf("Version %ld, CAR %d, POS %d, MAXBLOCK %d\n",
				sizeof(int)*8,CAR,POS,MAXBLOCK);

		clock_t begin = clock();
		
		do {	
			sum++;
			
			int numOK = TRUE;
			for(k=0; (numOK) && (k<POS-MAXBLOCK);k++)
			{
				numOK = FALSE;
				for(e = k + 1; (!numOK) && (e < k+MAXBLOCK+1); e++)
				{
					
					if(cell[k]!=cell[e])
					{
						
						numOK = TRUE;
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
				/*
				for(j=POS-1;j>=0;j--)
				{
					printf("%c",65+cell[j]);
				}
				printf("\n");
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
					ended = TRUE;
					break;
				}
			}

		} while(!ended);
		
		clock_t end = clock();
		
		printf("Sum   %lld \n",sum);
		
		printf("SumOK %lld \n",sumOK);
		
		printf("Time: %ld \n",((end-begin)*1000)/CLOCKS_PER_SEC);

	return 0;
}
