import math 
def _pad(string, block_size):
   
    no_of_blocks = math.ceil(len(string)/float(block_size))
    pad_value = int(no_of_blocks * block_size - len(string))

    if pad_value == 0:
        return string + ("\\" + hex(block_size)) * block_size
    else:
        return string + ("\\" + hex(pad_value)) * pad_value

print"ENTER THE STRING"
string= raw_input()
print"ENTER THE BLOCK SIZE:)"
block_size = input()
print(_pad(string,block_size))
