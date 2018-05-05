from Crypto.Cipher import AES

object = AES.new("YELLOW SUBMARINE",AES.MODE_ECB)
string_1 = ''
with open('aes.txt') as t1:
	for s in t1: 	
	
		s = (s.strip()).decode("base64")
		string_1+= s
	print(string_1)
print(object.decrypt(string_1))
		
		
 #or
 
 
 from Crypto.Cipher import AES
 
 object = AES.new("	YELLOW SUBMARINE", AES.MODE_ECB)
 
 cipher_text = ''.join(list(open("aes.txt","r"))).decode("base64")
 print(cipher_text)
 
