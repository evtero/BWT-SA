from utils_bwt import *
import sys
print(sys.argv[1],sys.argv[2])
try: 
	with open(sys.argv[1], "tr") as file:
		t = file.read(int(sys.argv[2])) + '$'		
		bwt = sa2btw(t,get_sa_bf(t))
		
except FileNotFoundError:
	print("fichero no encontrado")
		
try: 
	with open(sys.argv[1] + '_BTW' + sys.argv[2] + '.txt', "tw") as file:
		file.write(bwt)
except FileNotFoundError:
	print("fichero no encontrado")


