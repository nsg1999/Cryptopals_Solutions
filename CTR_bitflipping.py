from Crypto.Cipher import AES
import Crypto.Util.Counter
import os
import struct


key=os.urandom(16)
nonce=os.urandom(8)
count=0

def encryption_func(final_str):
	ctr = Crypto.Util.Counter.new(64, prefix = nonce, initial_value = count) #rest of the 64 bits will belong to nonce this fn will be for count
	obj = AES.new(key, AES.MODE_CTR, counter = ctr)
	return(obj.encrypt(final_str))


def pre_and_app_func(inp):
	prepend_str = "comment1=cooking%20MCs;userdata="
	append_str = ";comment2=%20like%20a%20pound%20of%20bacon"
	replaced = inp.replace(';','?').replace('=','?')
	#print(replace)
	final_str = prepend_str + replaced + append_str
	return (encryption_func(final_str)).encode("base64")

def decrypter(encrypted_str):
	ctr = Crypto.Util.Counter.new(64, prefix = nonce, initial_value = count) #rest of the 64 bits will belong to nonce this fn will be for count
	obj = AES.new(key, AES.MODE_CTR, counter = ctr)
	return(obj.decrypt(encrypted_str))

def decryption(encrypted_str):
	decrypted_str = decrypter(encrypted_str)
	print(decrypted_str)
	if ";admin=true;" in decrypted_str:
		print("Ho gaya flip")
	else:
		print("fail ho gaya flip, try again later")

def check_func(_string):
	L = list(_string)
	L[32]=chr(ord(L[32])^ord('?')^ord(';'))
	L[38]=chr(ord(L[38])^ord('?')^ord('='))
	L[43]=chr(ord(L[43])^ord('?')^ord(';'))
	return "".join(L)



input_str = ";admin=true;"
string_ = pre_and_app_func(input_str)
decryption(check_func(string_.decode("base64")))
