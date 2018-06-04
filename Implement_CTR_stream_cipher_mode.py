from Crypto.Cipher import AES
import struct


key = "YELLOW SUBMARINE"

_input = "L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==".decode("base64") 

nonce = 0
c = 0

def count_func():
	global c
	n = struct.pack("<Q", nonce)  #Q returns 8 bytes(long int)
	c1 = struct.pack("<Q", c)
	inc_c = n + c1
	c = c + 1
	return inc_c
	
	

cipher = AES.new(key,AES.MODE_CTR,counter=count_func)
answer = cipher.decrypt(_input)

print(answer)
print("--------")
    
