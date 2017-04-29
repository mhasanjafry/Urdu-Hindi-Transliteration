#needed for reading unicode files
import codecs
#needed for extracting the start of the line
import re

#making dictionaries global so don't have to pass around
urdu_ipa_dict = dict()
hindi_ipa_dict = dict()
word_dict = dict()
#given two IPA words, this function will return the Levenshtein distance between them
def findLevenshteinDistance(source, target):
	if source == target:
		return 0


	# Prepare a matrix
	slen, tlen = len(source), len(target)
	dist = [[0 for i in range(tlen+1)] for x in range(slen+1)]
	for i in xrange(slen+1):
		dist[i][0] = i
	for j in xrange(tlen+1):
		dist[0][j] = j

	# Counting distance, here is my function
	for i in xrange(slen):
		for j in xrange(tlen):
			cost = 0 if source[i] == target[j] else 1
			dist[i+1][j+1] = min(
				dist[i][j+1] + 1,   # deletion
				dist[i+1][j] + 1,   # insertion
				dist[i][j] + cost   # substitution
				)
	return dist[-1][-1]

#given an IPA word and IPA list, this function will return the index of the ipa word in the list with which the Levenshtein is minimum
def findMinimumDistance(urdu_ipa_word, hindi_ipa_list):
	min_distance = 1000000000
	index = 0
	min_index = 0
	for hindi_word_ipa in hindi_ipa_list:
		current_distance = findLevenshteinDistance(urdu_ipa_word, hindi_word_ipa)
		if current_distance < min_distance:
			min_distance = current_distance
			min_index = index

		index += 1


	return min_index, min_distance
#given two IPA lists, this function will map each Urdu word to its nearest Hindi words based on some distance measure
def matchWordsBasedOnIPA(urdu_ipa_list, hindi_ipa_list):
	#this dictionary will store the matching indexes in the IPA list which will use later on to match words in both languages	
	index_dict = dict()
	urdu_index = 0
	for word in urdu_ipa_list:
		min_hindi_index, min_distance = findMinimumDistance(word, hindi_ipa_list)
		index_dict[urdu_index] = [min_hindi_index, min_distance]

		urdu_index += 1

	return index_dict
#the goal of this function is to convert urdu words into equivalent IPA sounds
#input is list of urdu words
#output is list of ipa representation of these urdu words
def covertUrduWordsinIPA(urdu_words):
	#using the global urdu ipa dictionary
	global urdu_ipa_dict
	#print urdu_words
	
	#this will store the ipa conversions of urdu words
	urdu_ipa_list = []
	#utf8 encoding of madd symbol in urdu	
	madd = u'\u0651'
	#looping over word by word
	for word in urdu_words:
			#this string will store the ipa conversion for one word
			ipa_word = ''
			#looping over alphabet by alphabet
			i = 0
			for alphabet in list(word):
				#print alphabet
				a1 = alphabet
				#a2 = u'\u0670'
				#print a1,a2
				#if a1.encode('UTF-8') == a2.encode('UTF-8'):
				#	print word
				if a1.encode('UTF-8') == madd.encode('UTF-8'):
					#print word
					#print a1
					ipa_word += urdu_ipa_dict[list(word)[i-1]][0]
					#print word
					#print 'Repeated the sound of the alphabet' + list(word)[i-1]					
					i += 1
					continue
				#this means that we have not entered the alphabet in the dictionary
				if alphabet not in urdu_ipa_dict:
					#print 'The alphabet ' + alphabet + ' is not present in the dictionary'
					i += 1 
					continue
				#this means that we have not put in the mapping yet
				if len(urdu_ipa_dict[alphabet]) == 0:
					i += 1
					#print 'There is no mapping for the alphabet ' + alphabet + ' in the dictionary'
					continue
				else:
					ipa_word += urdu_ipa_dict[alphabet][0]
					i += 1
			
			#print ipa_word
			urdu_ipa_list.append(ipa_word)

	return urdu_ipa_list

#the goal of this function is to convert hindi words into equivalent IPA sounds
#input is list of hindi words
#output is list of ipa representation of these hindi words 
def covertHindiWordsinIPA(hindi_words):
	#using the global hindi ipa dictionary
	global hindi_ipa_dict
	#print hindi_words
	
	#this will store the ipa conversions of hindi words
	hindi_ipa_list = []
	#looping over word by word
	for word in hindi_words:
			#this string will store the ipa conversion for one word
			ipa_word = ''
			#looping over alphabet by alphabet
			for alphabet in list(word):
				#this means that we have not entered the alphabet in the dictionary
				if alphabet not in hindi_ipa_dict:
					#print 'The alphabet ' + alphabet + ' is not present in the dictionary' 
					continue
				#this means that we have not put in the mapping yet
				if len(hindi_ipa_dict[alphabet]) == 0:
					#print 'There is no mapping for the alphabet ' + alphabet + ' in the dictionary'
					continue
				else:
					ipa_word += hindi_ipa_dict[alphabet][0]
			
			#print ipa_word
			hindi_ipa_list.append(ipa_word)

	return hindi_ipa_list

def main():
	global word_dict
	global urdu_ipa_dict
	urdu_ipa_dict[u'\u06D4'] = [] #arabic dot....what to do with it?
	urdu_ipa_dict[u'\u060C'] = [] #arabic comma...what to do with it?
	urdu_ipa_dict[u'\u061F'] = [] #arabic question mark...what to do it with it 
	urdu_ipa_dict[u'\uFDFA'] = [] #salutation for Prophet Muhammad....what to do with it?
	urdu_ipa_dict[u'\u0611'] = [] #salutation for all Prophets (Aleh Assalam)....what to do with it
	urdu_ipa_dict[u'\u0613'] = [] #salutation for companions of Prophet (Razi Allah)....what to do with it
	urdu_ipa_dict[u'\u0624'] = [] #hamza wow....what to do with it
	urdu_ipa_dict[u'\u0650'] = [] #I think this is zair...what to do with it
	urdu_ipa_dict[u'\u064E'] = [] #I think this is zair...what to do with it
	urdu_ipa_dict[u'\u064B'] = [] #I think this is do zabar...what to do with it
	urdu_ipa_dict[u'\u0674'] = [] #high hamza...what to do with it
	urdu_ipa_dict[u'\u064F'] = [] #I think this is paish...what to do with it
	urdu_ipa_dict[u'\u0670'] = [] #Superscript Alif...what to do with it
	urdu_ipa_dict[u'\u0629'] = [u'\u0074\u032A'] #gol hey with two dots on top...replacing it with tay sound
	urdu_ipa_dict[u'\u064A'] = [u'\u025B\u02D0',u'\u0065\u02D0'] #choti yay with two dots below...replacing it with sound of bari yay (just 2 occurences in all corpus)
	urdu_ipa_dict[u'\u0651'] = [] #arabic shad...handled it in code. Repeated the sound of previous alphabet 
	urdu_ipa_dict[u'\u064C'] = [] #arabic dammatan...ignoring it because it is Arabic specific
	urdu_ipa_dict[u'\u0653'] = [] #arabic madda above...ignoring it because it is Arabic specific
	urdu_ipa_dict[u'\u0626'] = [u'\u026A', u'\u0065\u02D0'] #hamza choti yay...replaced it with sounds of i and ay


	urdu_ipa_dict[u'\u0627'] = [u'\u0251\u02D0', u'\u0294', u'\u2205'] #alif
	urdu_ipa_dict[u'\u0622'] = [u'\u0061\u02D0'] #alif mad aa
	urdu_ipa_dict[u'\u0628'] = [u'\u0062'] #bay
	urdu_ipa_dict[u'\u067e'] = [u'\u0070'] #pay
	urdu_ipa_dict[u'\u062a'] = [u'\u0074\u032A'] #tay
	urdu_ipa_dict[u'\u0679'] = [u'\u0288'] #ttay
	urdu_ipa_dict[u'\u062B'] = [u'\u0073'] #say
	urdu_ipa_dict[u'\u062C'] = [u'\u0064\u0361\u0292'] #jeem
	urdu_ipa_dict[u'\u0686'] = [u'\u0074\u0361\u0283'] #chay
	urdu_ipa_dict[u'\u062D'] = [u'\u0068', u'\u0266'] #hay
	urdu_ipa_dict[u'\u062E'] = [u'\u0078'] #khay
	urdu_ipa_dict[u'\u062F'] = [u'\u0064\u032A'] #daal
	urdu_ipa_dict[u'\u0688'] = [u'\u0256'] #ddaal
	urdu_ipa_dict[u'\u0630'] = [u'\u007A'] #zaal
	urdu_ipa_dict[u'\u0631'] = [u'\u0072'] #ray	
 	urdu_ipa_dict[u'\u0691'] = [u'\u027D'] #rray
	urdu_ipa_dict[u'\u0632'] = [u'\u007A'] #zay
	urdu_ipa_dict[u'\u0698'] = [u'\u0292'] #yay
	urdu_ipa_dict[u'\u0633'] = [u'\u0073'] #seen........
	urdu_ipa_dict[u'\u0634'] = [u'\u0283'] #sheen	
	urdu_ipa_dict[u'\u0635'] = [u'\u0073'] #suaad
	urdu_ipa_dict[u'\u0636'] = [u'\u007A'] #zawad
	urdu_ipa_dict[u'\u0637'] = [u'\u0074\u032A'] #tuain
	urdu_ipa_dict[u'\u0638'] = [u'\u007A'] #zuain
	urdu_ipa_dict[u'\u0639'] = [u'\u0251\u02D0', u'\u006F\u02D0', u'\u0065\u02D0', u'\u0294', u'\u0295', u'\u2205'] #aain	
	urdu_ipa_dict[u'\u063A'] = [u'\u0263'] #ghain
	urdu_ipa_dict[u'\u0641'] = [u'\u0066'] #fay
	urdu_ipa_dict[u'\u0642'] = [u'\u0071'] #kaaf
	urdu_ipa_dict[u'\u06A9'] = [u'\u006B'] #kiyaaf
	urdu_ipa_dict[u'\u06AF'] = [u'\u0067'] #gaaf
	urdu_ipa_dict[u'\u0644'] = [u'\u006C'] #laam
	urdu_ipa_dict[u'\u0645'] = [u'\u006D'] #meme
	urdu_ipa_dict[u'\u0646'] = [u'\u006E',u'\u0272',u'\u0273',u'\u014B'] #noon
	urdu_ipa_dict[u'\u06BA'] = [u'\u0303'] #noon ghunna
	urdu_ipa_dict[u'\u0648'] = [u'\u028B',u'\u0075\u02D0',u'\u006F\u02D0',u'\u0254\u02D0'] #wow
	urdu_ipa_dict[u'\u06C1'] = [u'\u0068',u'\u0266',u'\u2205'] #hey
	urdu_ipa_dict[u'\u0647'] = [u'\u0068',u'\u0266',u'\u2205'] #hey
	urdu_ipa_dict[u'\u06BE'] = [u'\u02B0',u'\u02B1'] #dochashmi hey
	urdu_ipa_dict[u'\u0621'] = [u'\u0294', u'\u2205'] #hamza 
	urdu_ipa_dict[u'\u06CC'] = [u'\u006A',u'\u0069\u02D0',u'\u0251\u02D0'] #choti yay 
	urdu_ipa_dict[u'\u06D2'] = [u'\u025B\u02D0',u'\u0065\u02D0'] #bari yay

	#------------------------------------------------------------------------------------------------------------
	#Hindi dictionary
	global hindi_ipa_dict


	#punctuation
	hindi_ipa_dict[u'\u0964'] = []  # Hindi dot (purnaviram)
	hindi_ipa_dict[u'\u0965'] = []  # deergh viram
	hindi_ipa_dict[','] = []  #  comma
	hindi_ipa_dict['?'] = []  #  question mark
	hindi_ipa_dict['"'] = []  #  double quotes
	hindi_ipa_dict[';'] = []  #  semi collon
	hindi_ipa_dict['_'] = []  # underscore
	hindi_ipa_dict['-'] = []  # dash
	hindi_ipa_dict["'"] = []  # single quotes
	hindi_ipa_dict[':'] = []  # collon
	hindi_ipa_dict['\\'] = []  # double back slash
	hindi_ipa_dict['1'] = []  # one
	hindi_ipa_dict[u'\u200c'] = []  #ZERO WIDTH NON - JOINER
	hindi_ipa_dict[u'\u200d'] = [] #ZERO WIDTH JOINER
	hindi_ipa_dict[u'\u2018'] = []  #curly right single quote
	hindi_ipa_dict[u'\u2019'] = []  #curly left single quote
	hindi_ipa_dict[u'\u201c'] = []  # curly right double quote
	hindi_ipa_dict[u'\u201d'] = []  # curly left double quote
	hindi_ipa_dict[u'\u2013'] = []  #dont know



	#numbers
	hindi_ipa_dict[u'\u0966'] = []  # DEVANAGARI DIGIT ZERO
	hindi_ipa_dict[u'\u0967'] = []  # DEVANAGARI DIGIT ONE
	hindi_ipa_dict[u'\u0968'] = []  # DEVANAGARI DIGIT TWO
	hindi_ipa_dict[u'\u0969'] = []  # DEVANAGARI DIGIT THREE
	hindi_ipa_dict[u'\u096A'] = []  # DEVANAGARI DIGIT FOUR
	hindi_ipa_dict[u'\u096B'] = []  # DEVANAGARI DIGIT FIVE
	hindi_ipa_dict[u'\u096C'] = []  # DEVANAGARI DIGIT SIX
	hindi_ipa_dict[u'\u096D'] = []  # DEVANAGARI DIGIT SEVEN
	hindi_ipa_dict[u'\u096E'] = []  # DEVANAGARI DIGIT EIGHT
	hindi_ipa_dict[u'\u096F'] = []  # DEVANAGARI DIGIT NINE

	#Independent vowels
	hindi_ipa_dict[u'\u0905'] = [u'\u0259'] #DEVANAGARI LETTER  A
	hindi_ipa_dict[u'\u0906'] = [u'\u0061'] #DEVANAGARI LETTER AA
	hindi_ipa_dict[u'\u0907'] = [u'\u026A'] #DEVANAGARI LETTER I
	hindi_ipa_dict[u'\u0908'] = [u'\u0069'] #DEVANAGARI LETTER II
	hindi_ipa_dict[u'\u0909'] = [u'\u028A'] #DEVANAGARI LETTER U
	hindi_ipa_dict[u'\u090A'] = [u'\u0075']  # DEVANAGARI LETTER UU
	hindi_ipa_dict[u'\u090B'] = []  # DEVANAGARI LETTER VOCALIC R (could not find)
	hindi_ipa_dict[u'\u090F'] = [u'\u0065']  # DEVANAGARI LETTER E
	hindi_ipa_dict[u'\u0910'] = [u'\u025B']  # DEVANAGARI LETTER AI
	hindi_ipa_dict[u'\u0913'] = [u'\u006F']  #DEVANAGARI LETTER O
	hindi_ipa_dict[u'\u0914'] = [u'\u0254']  # DEVANAGARI LETTER AU
	hindi_ipa_dict[u'\u0901'] = [u'\u0303']  # DEVANAGARI SIGN CANDRABINDU
	hindi_ipa_dict[u'\u0902'] = [u'\u014B\u0272\u0273\u006E\u006D\u0303']  # DEVANAGARI SIGN ANUSVARA
	hindi_ipa_dict[u'\u0903'] = [u'\u0266'] #DEVANAGARI SIGN VISARGA
	hindi_ipa_dict[u'\u0945'] = [u'\u0065'] #DEVANAGARI VOWEL SIGN CANDRA E (check)

	# Consonants
	hindi_ipa_dict[u'\u0915'] = [u'\u006B']  # DEVANAGARI LETTER  KA
	hindi_ipa_dict[u'\u0916'] = [u'\u02B0']  # DEVANAGARI LETTER KHA
	hindi_ipa_dict[u'\u0917'] = [u'\u0261']  # DEVANAGARI LETTER GA
	hindi_ipa_dict[u'\u0918'] = [u'\u0324']  # DEVANAGARI LETTER GHA
	hindi_ipa_dict[u'\u0919'] = [u'\u014B']  # DEVANAGARI LETTER NGA
	hindi_ipa_dict[u'\u091A'] = [u'\u0074\u0361\u0283']  # DEVANAGARI LETTER CA
	hindi_ipa_dict[u'\u091B'] = [u'\u02B0']  # DEVANAGARI LETTER CHA
	hindi_ipa_dict[u'\u091C'] = [u'\u0064\u0361\u0292']  # DEVANAGARI LETTER JA
	hindi_ipa_dict[u'\u091D'] = [u'\u0324\u0292']  # DEVANAGARI LETTER JHA
	hindi_ipa_dict[u'\u091E'] = [u'\u0272']  # DEVANAGARI LETTER NYA
	hindi_ipa_dict[u'\u091F'] = [u'\u0288']  # DEVANAGARI SIGN TTA
	hindi_ipa_dict[u'\u0920'] = [u'\u02B0']  # DEVANAGARI SIGN TTHA
	hindi_ipa_dict[u'\u0921'] = [u'\u0256']  # DEVANAGARI SIGN DDA
	hindi_ipa_dict[u'\u0922'] = [u'\u0324']  # DEVANAGARI LETTER DDHA
	hindi_ipa_dict[u'\u0923'] = [u'\u0273']  # DEVANAGARI LETTER NNA
	hindi_ipa_dict[u'\u0924'] = [u'\u0074']  # DEVANAGARI LETTER TA
	hindi_ipa_dict[u'\u0925'] = [u'\u02B0']  # DEVANAGARI LETTER THA
	hindi_ipa_dict[u'\u0926'] = [u'\u0064']  # DEVANAGARI LETTER DA
	hindi_ipa_dict[u'\u0927'] = [u'\u0324']  # DEVANAGARI LETTER DHA
	hindi_ipa_dict[u'\u0928'] = [u'\u006E']  # DEVANAGARI LETTER NA
	hindi_ipa_dict[u'\u092A'] = [u'\u0070']  # DEVANAGARI LETTER PA
	hindi_ipa_dict[u'\u092B'] = [u'\u02B0']  # DEVANAGARI LETTER PHA
	hindi_ipa_dict[u'\u092C'] = [u'\u0062']  # DEVANAGARI LETTER BA
	hindi_ipa_dict[u'\u092D'] = [u'\u0324']  # DEVANAGARI LETTER BHA
	hindi_ipa_dict[u'\u092E'] = [u'\u006D']  # DEVANAGARI LETTER MA
	hindi_ipa_dict[u'\u092F'] = [u'\u006A']  # DEVANAGARI LETTER YA
	hindi_ipa_dict[u'\u0930'] = [u'\u0072']  # DEVANAGARI LETTER RA
	hindi_ipa_dict[u'\u0932'] = [u'\u006C']  # DEVANAGARI LETTER LA
	hindi_ipa_dict[u'\u0935'] = [u'\u028B']  # DEVANAGARI LETTER VA
	hindi_ipa_dict[u'\u0936'] = [u'\u0283']  # DEVANAGARI LETTER SHA
	hindi_ipa_dict[u'\u0937'] = [u'\u0282']  # DEVANAGARI LETTER SSA
	hindi_ipa_dict[u'\u0938'] = [u'\u0073']  # DEVANAGARI LETTER SA
	hindi_ipa_dict[u'\u0939'] = [u'\u0266']  # DEVANAGARI LETTER HA

	#Additional consonants
	hindi_ipa_dict[u'\u0958'] = [u'\u0071']  # DEVANAGARI LETTER QA
	hindi_ipa_dict[u'\u0959'] = [u'\u0078']  # DEVANAGARI LETTER KHHA
	hindi_ipa_dict[u'\u095A'] = [u'\u0263']  # DEVANAGARI LETTER GHHA
	hindi_ipa_dict[u'\u095B'] = [u'\u007A']  # DEVANAGARI LETTER ZA
	hindi_ipa_dict[u'\u095C'] = [u'\u0256']  # DEVANAGARI LETTER DDDHA
	hindi_ipa_dict[u'\u095C'] = [u'\u027D']  # DEVANAGARI LETTER DDDHA
	hindi_ipa_dict[u'\u095D'] = []  # DEVANAGARI LETTER RHA (not available)
	hindi_ipa_dict[u'\u095E'] = [u'\u0066']  # DEVANAGARI LETTER FA
	hindi_ipa_dict[u'\u0929'] = [u'\u0928\u093C']  #DEVANAGARI LETTER NNNA
	hindi_ipa_dict[u'\u0931'] = [u'\u0930\u093C']  # DEVANAGARI LETTER RRA
	hindi_ipa_dict[u'\u095F'] = [u'\u092F\u093C']  # DEVANAGARI LETTER YYA

	#Dependent vowel signs
	hindi_ipa_dict[u'\u093E'] = [u'\u0061']  # DEVANAGARI VOWEL SIGN AA
	hindi_ipa_dict[u'\u093F'] = [u'\u026A']  # DEVANAGARI VOWEL SIGN I
	hindi_ipa_dict[u'\u0940'] = [u'\u0069']  # DEVANAGARI VOWEL SIGN II
	hindi_ipa_dict[u'\u0941'] = [u'\u028A']  # DEVANAGARI VOWEL SIGN U
	hindi_ipa_dict[u'\u0942'] = [u'\u0075']  # DEVANAGARI VOWEL SIGN UU
	hindi_ipa_dict[u'\u0943'] = []  # DEVANAGARI VOWEL SIGN VOCALIC R [not available]
	hindi_ipa_dict[u'\u0947'] = [u'\u0065']  # DEVANAGARI VOWEL SIGN E
	hindi_ipa_dict[u'\u0948'] = [u'\u025B']  #DEVANAGARI VOWEL SIGN AI
	hindi_ipa_dict[u'\u094B'] = [u'\u006F']  #DEVANAGARI VOWEL SIGN O
	hindi_ipa_dict[u'\u094C'] = [u'\u0254']  # DEVANAGARI VOWEL SIGN AU
	hindi_ipa_dict[u'\u0946'] = [u'\u0065']  #DEVANAGARI VOWEL SIGN SHORT E
	hindi_ipa_dict[u'\u094A'] = [u'\u006F']  #DEVANAGARI VOWEL SIGN SHORT O

	#Virama
	hindi_ipa_dict[u'\u094D'] = []  # DEVANAGARI  SIGN Virama (hallant)

	#Various signs
	hindi_ipa_dict[u'\u093C'] = [] #DEVANAGARI SIGN NUKTA

	#Abbreviation sign
	hindi_ipa_dict[u'\u0970'] = []  # DEVANAGARI ABBREVIATION SIGN(intended for Devanagari-specific abbreviation)

	#-----------------------------------------------------------------------------------------------------



	
	#opening the file for reading UTF-8 data
	urdu_file = codecs.open('urdu_standardized.txt', encoding='utf-8')
	hindi_file = codecs.open('hindi_1.txt', encoding='utf-8')
	output_file = codecs.open("output_baseline.txt", "w", "utf-8")
	#looping over line by line in both files simultaneously
	for urdu_line, hindi_line in zip(urdu_file, hindi_file):
		#this is for extracting the line numbers from the start, we can use them to match lines in both files
		#start_urdu = re.findall('\d+\|\d+\|', urdu_line)
		start_urdu = ''
		start_hindi = ''
		#start_hindi = re.findall('\d+\|\d+\|', hindi_line)
		#print str(start_urdu)
		#print str(start_hindi)
		#if the start numbers in both files match, we can do further processing
		#if str(start_urdu) == str(start_hindi):
		
		#removing the starting line numbers
		#urdu_line = urdu_line.replace(''.join(start_urdu),'')
		#removing useless characters from line
		urdu_line = urdu_line.replace('(', ' ').replace(')', ' ').replace('!',' ').replace('.',' ')

		#removing the starting line numbers
		#hindi_line = hindi_line.replace(''.join(start_hindi),'')
		#removing useless characters from line
		hindi_line = hindi_line.replace('(', ' ').replace(')', ' ').replace('!',' ').replace('.',' ')

		#verifying that the correct corresponding sentences were read
		#print urdu_line
		#print hindi_line

		#splitting the urdu line based on space
		urdu_words = urdu_line.split()
		#print urdu_words
		urdu_ipa_list = covertUrduWordsinIPA(urdu_words)
		#print len(urdu_ipa_list)	

		#splitting the hindi line based on space
		hindi_words = hindi_line.split()
		#print hindi_words
		hindi_ipa_list = covertHindiWordsinIPA(hindi_words)
		#print len(hindi_ipa_list)

		#got the matches indexes in IPA lists, now using them to match actual words 
		index_dict = matchWordsBasedOnIPA(urdu_ipa_list, hindi_ipa_list)
		
		

		for key,value in index_dict.items():
			if value[1] <= 3:
				output_file.write(str(start_urdu) +'\t'+urdu_words[key]+ '('+ urdu_ipa_list[key]+')'+'\t'+ hindi_words[value[0]]+'('+ hindi_ipa_list[value[0]]+')'+'\t'+ str(value[1])+'\n')
					#print urdu_words[key]+'\t'+ hindi_words[value[0]]+'\t'+ str(value[1])
				
				word_dict[urdu_words[key]] = [(hindi_words[value[0]], value[1])]


				
		#else:
		#	print 'Line numbers have misaligned!!! Please check and verify...'
		
	output_file.close()
	#for alphabet,ipa in urdu_ipa_dict.items():
	#	print alphabet+':'
	#	for one in ipa:
	#		print(one)
	#print unicode(urdu_ipa_dict)

main()
