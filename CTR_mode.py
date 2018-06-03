from Crypto.Cipher import AES

key = "YELLOW SUBMARINE"

_input = "L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==".decode("base64") 


nonce = 0
c = 0

def count_func(nonce, c):
	inc_c = nonce + c
	c = c + 1
	return inc_c
	
	


counter = str(count_func(nonce,c))

cipher = AES.new(key,AES.MODE_CTR,counter)

answer = cipher.decrypt(_input)

    
