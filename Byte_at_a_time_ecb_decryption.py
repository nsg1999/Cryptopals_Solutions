from Crypto.Cipher import AES
import os

string = "a" * 15
def K():
	key = os.urandom(16)
	return key


def padding_fun(ini_str , l):
	ini_str = ini_str + chr(l - (l1%l)) * (l - (l1%l))
	return ini_str


def func_1(x,ll,strn):                    
	final_string = ""
	for i in range(0,ll):
		s1 = strn + chr(padding_answer[i])
		answer1 = CIPHER.decrypt(s1)
		check = str(func_2(strn,answer1))
		final_string+= check
		strn = s1[1:]
	return final_string       
	
def func_2(strn,answer_1):             
	for i in range(256):
		s2 = strn + chr(i)
		answer2 = CIPHER.decrypt(s2)
		if(answer_1 == answer2):
			return chr(i)
			

CIPHER = AES.new(K(),AES.MODE_ECB)

strr ="Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3AIE5vLCBJIGp1c3QgZHJvdmUgYnkK=".decode("base64")
 
ini_str = bytearray(strr)
 
l1 = len(ini_str)
padding_answer = padding_fun(ini_str, 16)
l2 = len(padding_answer)	
flag = func_1(ini_str,l2,string)
print(flag)
