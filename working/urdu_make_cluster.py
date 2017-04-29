#needed for reading unicode files
import codecs

def main():
	#opening the file for reading UTF-8 data
	urdu_file = codecs.open('web.urd.full_standardized.txt', encoding='utf-8')
	output_file = codecs.open("web.urd.full_standardized_combined.txt", "w", "utf-8")
	# urdu_file = codecs.open('platts_urdu_standardized.txt', encoding='utf-8')
	# output_file = codecs.open("platts_urdu_standardized_combined.txt", "w", "utf-8")

	for urdu_word in urdu_file:
		urdu_word = urdu_word.strip()
		for index in range(0,len(urdu_word)):
			if urdu_word[index] == u'\u06BE' or urdu_word[index] == u'\u062D' or urdu_word[index] == u'\u06C1':
				continue
			if index != (len(urdu_word)-1):
				if urdu_word[index+1] == u'\u06BE' or urdu_word[index+1] == u'\u062D' or urdu_word[index+1] == u'\u06C1':
					output_file.write(urdu_word[index]+urdu_word[index+1]+' ')
				else:
					output_file.write(urdu_word[index]+' ')
			else:
				output_file.write(urdu_word[index]+' ')

		output_file.write('\n')

	urdu_file.close()
	output_file.close()
main()
