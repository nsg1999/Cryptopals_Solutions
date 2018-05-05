"""
Detect AES in ECB mode
----------------------
In this file are a bunch of hex-encoded ciphertexts.
One of them has been encrypted with ECB.
Detect it.
Remember that the problem with ECB is that it is stateless and deterministic;
the same 16 byte plaintext block will always produce the same 16 byte
ciphertext.
"""

def detecting_AES_in_ECB(txt):
   

    string = [txt[i:i+16*2] for i in range(0, len(txt), 16*2)]
    return not (len(set(string)) == len(string))


with open('ch8.txt', 'r') as f:
    txts = [line.strip() for line in f]
for txt in txts:
    if detecting_AES_in_ECB(txt):
	print txt
