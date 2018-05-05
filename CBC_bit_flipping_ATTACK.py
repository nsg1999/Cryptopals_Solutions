from Crypto.Cipher import AES
from os import urandom


key = urandom(16)
ini_v = '\x00' * 16

t_list =[]



def pre_and_app(trans_str):   #prepending and appending:
	ans = "comment1=cooking%20MCs;userdata=" + trans_str + "comment2=%20like%20a%20pound%20of%20bacon"
	ans = "".join(ans)
	return ans
	

def padding_fun(str1,le):    #padding 
	pad_l = le - (len(str1)%le)
	byte = chr(pad_l)	
	str1 += (pad_l*byte)
	return str1



def beg_func(_string):	
	cipher = AES.new(key,AES.MODE_CBC,ini_v)
	for i in range(l):
		if( _string[i] == ';' or _string[i] == '='):
			_string = _string.replace( _string[i] , '?')
		
	
	res_str = pre_and_app(_string)
	
	string = padding_fun(res_str,16)
	print(string)

	st1 = cipher.encrypt(string)
	
	return st1
	
	
	
	
def decryption_func(text):	#checking final result
    cipher1 = AES.new(key,AES.MODE_CBC,ini_v)
    
    final_ans = cipher1.decrypt(text)
    print("after decryption")
    print(final_ans)
    if ";admin=true;" in final_ans:
        print "ATTACK IS DONE :)"
    else:
        print "SORRY, TRY LATER :("
        
        

	


input_string = ";admin=true;"

l = len(input_string)

str2  = list(beg_func(input_string))

 
print("BEFORE FLIPPING")
print(str2)

X = ord('?') ^ ord(';')
Y = ord('?') ^ ord('=')
Z = ord('?') ^ ord(';')

str2[16] =(chr(ord(str2[16]) ^ X ))
str2[22] =(chr(ord(str2[22]) ^ Y ))
str2[27] =(chr(ord(str2[27]) ^ Z ))

print("AFTER FLIPPING")
print(str2)
ANSWER = "".join(str2)

print("before decryption") 
print(ANSWER)
decryption_func(ANSWER)
print("HO GAYA: hehe")
	
















	


	
