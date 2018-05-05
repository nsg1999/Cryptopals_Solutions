from Crypto.Cipher import AES
ini_v = '\x00' * 16
input_str = raw_input()     #input_str is the key here


cipher = AES.new(input_str, AES.MODE_CBC, ini_v)
string=""


with open("CBC.txt") as t:
	for st in t:
		s=(st.strip()).decode("base64")
		string+=s
	string.zfill(16)	
	result=cipher.decrypt(string)
print(result)		

           
           
           
           
           
           		
