#any alphabet + hallant + same alphabet = alphabet shad
#get all hay characters, check before and after hallant. If alphabet + alphabet ha, write alphabet ha
#for handling the hallant issue, we need this
from itertools import izip as zip, count
#needed for reading unicode files
import codecs
#needed for extracting the start of the line
import re
import itertools


def main():
	#opening the file for reading UTF-8 data
	urdu_file = codecs.open('test.txt', encoding='utf-8')
	output_file = codecs.open("output.txt", "w", "utf-8")
	for urdu_line in urdu_file:
		
		#removing useless characters from line
		urdu_line = urdu_line.replace('(', ' ').replace(')', ' ').replace('!',' ').replace('.',' ')
		#splitting the hindi line based on space
		urdu_words = urdu_line.split()
		for urdu_word in urdu_words:
			for alphabet in urdu_word:
				output_file.write(alphabet + ' ')
			output_file.write('\n')
			#print hindi_ipa_list
	output_file.close()
	urdu_file.close()
main()
