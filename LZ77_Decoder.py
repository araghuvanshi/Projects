import struct
import sys
import os
from io import *
from array import *



def unpacker(fileName, MAX_SEARCH):
	file = open("%s.bin" % (fileName), 'rb')
	#file_size = os.path.getsize("%s.bin" % (fileName))
	#print(file_size)
	#file_size_half = file_size/2
	#print(file_size_half)
	byte_string = file.read()
	#unpacked_byte_file = struct.unpack(">%dH" % (file_size_half), byte_string)
	output_string = ""
	#print(byte_string)
	i = 0
	while i<len(byte_string):
		(offset_and_length, char) = struct.unpack(">HB", byte_string[i:i+3])
		offset = offset_and_length >> 6
		length = offset_and_length - (offset<<6)			
		character = chr(char)
		if(offset == 0 and length == 0):
			output_string += character
		else:
			copy_index = len(output_string) - MAX_SEARCH 
			if (copy_index < 0):
				copy_index = offset

			else:
				copy_index += offset

			for j in range(length):
				output_string += output_string[copy_index+j]
			output_string += character

			#print(character)
			#print()
		i+=3
	output_file = open("%s_decompressed.txt" % (sys.argv[1]), 'w')
	output_file.write(output_string)

def main():
	file_name = sys.argv[1]
	MAX_SEARCH_input = int(sys.argv[2])
	unpacker(file_name, MAX_SEARCH_input)

if __name__== '__main__':
	main()
