#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
text_file = codecs.open('/home/hasan/Desktop/NLP/data/Anjali/hindi_1.txt', encoding='utf-8')
# inter_file = codecs.open('inter.urd', "w", encoding='utf-8')
output_file = codecs.open("/home/hasan/Desktop/NLP/data/Anjali/hin_conv_to_urd.txt", "w", "utf-8")

for line in text_file:
	output_file.write(line)
	for word in line.split():
		string = ""
		for alphabet in word:
			string += alphabet + " "
		batcmd="echo " + string + " | ~/NLP/SMT/mosesdecoder/bin/moses -f ~/NLP/SMT/working/train/model/moses.ini"
		result = subprocess.check_output(batcmd, shell=True)
		result = result.replace(" ","").replace("\n","")

		output_file.write(result + " ")
	output_file.write("\n")

output_file.close()