def PKCS7_padding_validation(s):
	
	 global count 
	 count = 0
	
	 last_byte = s[-1]
	 ord_byte = ord(last_byte)
	 
	 if( last_byte == 0 ):
	 	print("invalid padding")

	 else:
	 	if( last_byte <= 0 and last_byte > 16):
	 	 	print("invalid padding")
	 	 	
	  else:	
	 	 	for i in range(len(s)):
	 			if( s[i] == last_byte ):
	 	 			count = count + 1
	 	 			
	 		if( count == ord_byte ):
				print("valid padding:)") 
	    else:
		   	print("invalid padding")		



s = "ICE ICE BABY\x04\x04\x04\x04"
PKCS7_padding_validation(s)	
