By: Aman Raghuvanshi, araghuvanshi18@cmc.edu

INSTRUCTIONS FOR USE

1) Ensure you have Python 3.5
2) Uses Terminal arguments in the following format:
	ENCODER:
	2a) MAX_SEARCH can be chosen by the user. Note that 2048 and 4096 did not work in testing. 1024 is recommended.
	2b) Enter just the file name of the input IN QUOTATION MARKS. Do not include extension.
	2c) Format for Terminal commands is: python LZ77_Encoder.py "FILE NAME" (no extensions) MAX_SEARCH size (no quotation marks)

	DECODER:
	2a) MAX_SEARCH can be chosen by the user. Note that 2048 and 4096 did not work in testing. 1024 is recommended.
	2b) Enter just the file name of the input IN QUOTATION MARKS. Do not include extension.
	2c) Format for Terminal commands is: python LZ77_Decoder.py "FILE NAME" (no extensions) MAX_SEARCH size (no quotation marks)

COMPRESSION RATIOS

LZ77_Encoder.py and LZ77_Decoder.py are achieving the following compression ratios using .txt files from Project Gutenberg:

Dead End.txt = 45 KB
Dead End.bin = 32 KB
Entropy of Dead End.bin = 6.885485510612787
Ratio = 0.711:1

The Livestock Producer and Armour.txt = 61 KB
The Livestock Producer and Armour.bin = 42 KB
Entropy of The Livestock Producer and Armour.bin = 6.8818688235604135
Ratio = 0.626:1

Rihanna.txt = 47 bytes
Rihanna.bin = 42 bytes
Entropy of Rihanna.bin = 2.8659484796830337
Ratio = 0.893:1