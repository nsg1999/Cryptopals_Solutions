dict1 = { '0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J', '10': 'K', '11': 'L', '12': 'M', '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T', '20': 'U','21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z', '26': 'a','27': 'b', '28': 'c', '29': 'd', '30': 'e', '31': 'f', '32': 'g', '33': 'h', '34': 'i', '35': 'j', '36': 'k', '37': 'l', '38': 'm', '39': 'n', '40': 'o','41': 'p', '42': 'q','43': 'r', '44': 's','45': 't', '46': 'u', '47': 'v', '48': 'w', '49': 'x', '50': 'y', '51': 'z', '52': '0', '53': '1', '54': '2','55': '3', '56': '4', '57': '5', '58': '6', '59': '7', '60': '8', '61': '9', '62': '+', '63': '/'}
ch = 'gh2AtAht hS zRfghLz ftg otozofE WRAtTz'

l2=[]
l3=[]
n=0

list = [ord(x) for x in ch]
print(list)

binary = ''.join(bin(x)[2:].zfill(8) for x in list)
print(binary)                                             

if (len(binary) % 24 == 0):
	l2=[binary[i:i+6] for i in range(0,len(binary),6)]   
 	
else:
	while(24*n <= len(binary)):
    n=n+1
    
t = 24*n - len(binary)
l2 = [binary[i:i+6].zfill(6) for i in range(0,len(binary),6)]
print l2    
 
l3 +=((int(l2[i],2))for i in range(0,len(l2)))
lent=len(l3)
l5=[]
																																																			
for i in range(lent):
	for j in range(63):
		if(l3[i] == j):
			l5+=(dict1[str(j)])
print("".join(l5))			

	
