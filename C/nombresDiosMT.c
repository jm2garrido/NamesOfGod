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

/* linux gcc nombresDiosMT.c -std=c99 -O3 -fopenmp -march=x86-64 -o nombresDiosMT */

#include <stdio.h>
#include <time.h>
#include <omp.h>

#define CAR  (13)
#define POS  (9)
#define MAXBLOCK  (3)
#define TRUE (1)
#define FALSE (0)

long long sum = 0;
long long sumOK = 0;
/* supongo long long 64 bits */

void element(int first_row)
{
		
	int cell[POS];
	int ended = FALSE;
	
	int l,k,j,e;

	/*
	int th_id;
	th_id = omp_get_thread_num();
    	printf("Hello World from thread %d\n", th_id);
	*/	

	for(l=0; l<POS-1;l++) cell[l]=0;
	cell[POS-1] = first_row;
		
		
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
				if(i<POS-1)
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


}


int main(int argc, char** argv)
{

	printf("Version %ld, CAR %d, POS %d, MAXBLOCK %d\n",sizeof(int)*8,CAR,POS,MAXBLOCK);		

	omp_set_num_threads(CAR);		

	//clock_t begin = clock();
	//clock give as proccess time, for MP is way bigger than wall clock
	//This function give us the wall clock
	double begin = omp_get_wtime();	

	#pragma omp parallel for reduction(+:sum,sumOK)	
	for(int iTh = 0; iTh < CAR; iTh++)
	{
		element(iTh);
	}		

		
	//clock_t end = clock();
	double end = omp_get_wtime();	
	
	printf("Sum   %lld \n",sum);
		
	printf("SumOK %lld \n",sumOK);
		
	printf("Time: %f \n",((end-begin)*1000.0));

	return 0;
}
