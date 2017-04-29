import codecs

def main():
	#opening the file for reading UTF-8 data
	#urdu_file = codecs.open('urdu.txt', encoding='utf-8')
	character_file = codecs.open('test.txt', encoding='utf-8')
	output_file = codecs.open("output.txt", "w", "utf-8")
	#looping over line by line in both files simultaneously
	#for urdu_line, hindi_line in zip(urdu_file, hindi_file):

	tabin = u'\u0690\u0699\u0698\u0640\u0647\u064A\u06CC\uFBA9\u067F'
	tabout = u'\u0688\u0691\u068E\u06D2\u0647\u06CC\u06CC\u06C1\u0679'
	tabin = [ord(char) for char in tabin]
	translate_table = dict(zip(tabin, tabout))
	for line in character_file:
		line = line.translate(translate_table)
		print repr(line)
		output_file.write(line+'\n')		
		#line = line.strip().split()
		#print line[1], ' ', repr(line[1])
		
	output_file.close()
	character_file.close()

main()

