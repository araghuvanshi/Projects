import struct
import sys
import math
from io import *

def LZ77_search(search, lookahead):
	ls = len(search)  # length of search buffer
	llh = len(lookahead) # length of look_ahead buffer

	if(ls == 0):
		return (0,0,lookahead[0])

	if(llh == 0):
		return (-1,-1,"")

	best_offset = 0
	best_length = 0

	buf = search + lookahead
	#print(buf)

	search_pointer = ls

	#print("search: ", search, "lookahead:", lookahead)

	for i in range(0,ls): #all of the potential starting positions for search
		length = 0
		while buf[i+length] == buf[search_pointer+length]:
			#found a match
			length += 1
			#check for search reaching the end of the look_ahead
			if search_pointer + length == len(buf):
				length -= 1
				break 

		if (length > best_length):
				best_offset = i
				best_length = length

	 
	return (best_offset, best_length, buf[search_pointer+best_length])

def file_processor(fileName):
	the_list = []
	file = open(fileName, 'rb')
	text = file.read()
	read_text = list(text)
	for i in read_text:
		the_list=the_list+[i]
	return the_list


def main():
	file_name = sys.argv[1]

	MAX_SEARCH = int(sys.argv[2])
	log_search = int(math.log(MAX_SEARCH, 2))
	lookahead_size = int(math.log(65536, 2) - log_search)
	MAX_LOOKAHEAD = int(math.pow(2, lookahead_size))

	#input = "banana bandana work work work work work rihanna"
	#input = "badadadabaab"
	#input = "bananabandana"
	input = file_processor("%s.txt" % (file_name))
	search_idx = 0
	lookahead_idx = 0
	file = open("%s.bin" % (file_name), 'wb')

	while lookahead_idx < len(input):
		search = input[search_idx:lookahead_idx]
		lookahead = input[lookahead_idx:lookahead_idx+MAX_LOOKAHEAD]
		(offset, length, c) = LZ77_search(search, lookahead)
		#print (offset, length, chr(c))

		#packing into 3 byte tuples:
		shifted_offset = offset << 6
		offset_and_length = shifted_offset + length
		c = struct.pack("B", c)
		ol_bytes = struct.pack(">H", offset_and_length)

		file.write(ol_bytes) #to a .bin file
		file.write(c)

		lookahead_idx += length + 1
		search_idx = lookahead_idx - MAX_SEARCH
		if search_idx < 0:
			search_idx = 0
	file.close()

if __name__== '__main__':
	main()