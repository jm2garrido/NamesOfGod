=begin
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

Thanks to Carlos Arce

=end




def nombresDios(car,pos,maxblock)

	sum = 0
	sumOK = 0
	
	ended = false

	cell = [0]  # crea un vector con una posición
	(pos-1).times { cell << 0 }  # agrega las demás posiciones para que quede un vector de POS posiciones

	# comienza el bucle principal
	begin
		#incrementamos el número de combinaciones generadas
		sum=sum+1


		# comprobar número

		k=0
		begin
			numOK = false;
			e=k+1
			begin 
				#print ("k: #{k} e: #{e}")
				if(cell[k]!=cell[e])			
					#print ("Verdad")
					numOK = true;
				end
			e+=1
			end while ((!numOK) && (e < k+maxblock+1))		
		k+=1
		end while (k<= (pos-maxblock) && numOK)





		#imprimir el número
		if (numOK)
			sumOK+=1
			#print "#{cell} \n"
		end




		# incrementar el número
		cell[0]+=1
		i=0
		while(cell[i]>=car)
			cell[i]=0
			i+=1

			if(i<pos)
				cell[i]+=1
			else
				ended = true
				break
			end
		end

	end while(!ended)  
	
    return sum, sumOK

end

# 13,9,3
CAR = 13 	# 13 caracteres posibles
POS = 7 	# 9 posiciones
MAXBLOCK = 3	# lo máximo admitido

if (ARGV.length == 3)
    car = ARGV[0].to_i
    pos = ARGV[1].to_i
    maxblock = ARGV[2].to_i
else
    car = CAR
    pos = POS
    maxblock = MAXBLOCK
end

print "Car      #{car}\n"
print "Pos      #{pos}\n"
print "MAXBLOCK #{maxblock}\n"

start = Time.now

    sum, sumOK = nombresDios car,pos,maxblock

ending = Time.now

print "Sum    #{sum}\n"
print "SumOK  #{sumOK}\n"
print "Time   #{((ending-start)*1000).to_i}\n"
