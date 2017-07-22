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

using System;

namespace nombresDios
{
	class nombresDios
	{
		public static void Main(string[] args)
		{
		// 13,9,3
		int car = 13;
		int pos = 9;
		int maxblock = 3;

        if( args.Length == 3)
        {
            car = int.Parse(args[0]);
            pos = int.Parse(args[1]);
            maxblock = int.Parse(args[2]);
        }
  
		long sum = 0;
		long sumOK = 0;

		// variacion entre C# y Java
		int[] cell = new int[pos];
		bool ended = false;
		
		Console.WriteLine("Caracteres   "+car);
		Console.WriteLine("Posiciones   "+pos);
		Console.WriteLine("Repeticiones "+maxblock);

		// medicion del tiempo en C#
		DateTime begin = DateTime.Now;

		do {
			sum++;

			bool numOK = true;
			for(int k=0; (numOK) && (k<pos-maxblock);k++)
			{
				numOK = false;
				for(int e = k + 1; (!numOK) && (e < k+maxblock+1); e++)
				{
					//Console.WriteLine("k: "+k+" e: "+e);
					if(cell[k]!=cell[e])
					{
						//Console.WriteLine("Verdad");
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
				Console.WriteLine(a);
				*/
			}


			cell[0]++;
			int i=0;
			while(cell[i]>=car)
			{
				cell[i]=0;
				i++;
				if(i<pos)
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

		DateTime end = DateTime.Now;

		TimeSpan duration = end - begin;	
			
		Console.WriteLine("Sum   "+sum);

		Console.WriteLine("SumOK "+sumOK);

		Console.WriteLine("Time: "+duration.TotalMilliseconds);

		}
	}
}
