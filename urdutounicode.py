#any alphabet + hallant + same alphabet = alphabet shad
#get all hay characters, check before and after hallant. If alphabet + alphabet ha, write alphabet ha
#for handling the hallant issue, we need this
from itertools import izip as zip, count
#needed for reading unicode files
import codecs
#needed for extracting the start of the line
import re
import itertools

#making dictionaries global so don't have to pass around
urdu_ipa_dict = dict()
ipa_urdu_dict = dict()

#-----------------------------URDU ALPHABETS TO IPA CONVERSION DICTIONARY-------------------------------------------------------------------------

urdu_ipa_dict[u'\u06D4'] = [] #arabic dot....what to do with it?
urdu_ipa_dict[u'\u060C'] = [] #arabic comma...what to do with it?
urdu_ipa_dict[u'\u061F'] = [] #arabic question mark...what to do it with it 
urdu_ipa_dict[u'\uFDFA'] = [] #salutation for Prophet Muhammad....what to do with it?
urdu_ipa_dict[u'\u0611'] = [] #salutation for all Prophets (Aleh Assalam)....what to do with it
urdu_ipa_dict[u'\u0613'] = [] #salutation for companions of Prophet (Razi Allah)....what to do with it
urdu_ipa_dict[u'\u0624'] = [] #hamza wow....what to do with it
urdu_ipa_dict[u'\u0650'] = [] #I think this is zair...what to do with it
urdu_ipa_dict[u'\u064E'] = [] #I think this is zabar...what to do with it
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
urdu_ipa_dict[u'\u0636'] = [u'\u007A'] #zuaad
urdu_ipa_dict[u'\u0637'] = [u'\u0074\u032A'] #tuain
urdu_ipa_dict[u'\u0638'] = [u'\u007A'] #zuain
urdu_ipa_dict[u'\u0639'] = [u'\u0251\u02D0', u'\u006F\u02D0', u'\u0065\u02D0', u'\u0294', u'\u0295', u'\u2205'] #aain	
urdu_ipa_dict[u'\u063A'] = [u'\u0263'] #ghain
urdu_ipa_dict[u'\u0641'] = [u'\u0066'] #fay
urdu_ipa_dict[u'\u0642'] = [u'\u0071'] #kaaf
urdu_ipa_dict[u'\u06A9'] = [u'\u006B'] #kiyaaf
urdu_ipa_dict[u'\u06AF'] = [u'\u0067'] #gaaf
urdu_ipa_dict[u'\u0644'] = [u'\u006C'] #laam
urdu_ipa_dict[u'\u0645'] = [u'\u006D'] #meem
urdu_ipa_dict[u'\u0646'] = [u'\u006E',u'\u0272',u'\u0273',u'\u014B'] #noon
urdu_ipa_dict[u'\u06BA'] = [u'\u0303'] #noon ghunna
urdu_ipa_dict[u'\u0648'] = [u'\u028B',u'\u0075\u02D0',u'\u006F\u02D0',u'\u0254\u02D0'] #wow
urdu_ipa_dict[u'\u06C1'] = [u'\u0068',u'\u0266',u'\u2205'] #hey
urdu_ipa_dict[u'\u0647'] = [u'\u0068',u'\u0266',u'\u2205'] #hey
urdu_ipa_dict[u'\u06BE'] = [u'\u02B0',u'\u02B1'] #dochashmi hey
urdu_ipa_dict[u'\u0621'] = [u'\u0294', u'\u2205'] #hamza 
urdu_ipa_dict[u'\u06CC'] = [u'\u006A',u'\u0069\u02D0',u'\u0251\u02D0'] #choti yay 
urdu_ipa_dict[u'\u06D2'] = [u'\u025B\u02D0',u'\u0065\u02D0'] #bari yay


urdu_ipa_dict[u'\u06D4'] = [] #arabic dot....what to do with it?
urdu_ipa_dict[u'\u060C'] = [] #arabic comma...what to do with it?
urdu_ipa_dict[u'\u061F'] = [] #arabic question mark...what to do it with it 
urdu_ipa_dict[u'\uFDFA'] = [] #salutation for Prophet Muhammad....what to do with it?
urdu_ipa_dict[u'\u0611'] = [] #salutation for all Prophets (Aleh Assalam)....what to do with it
urdu_ipa_dict[u'\u0613'] = [] #salutation for companions of Prophet (Razi Allah)....what to do with it
urdu_ipa_dict[u'\u0624'] = [] #hamza wow....what to do with it
urdu_ipa_dict[u'\u0650'] = [] #I think this is zair...what to do with it
urdu_ipa_dict[u'\u064E'] = [] #I think this is zabar...what to do with it
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

#-----------------------------IPA ALPHABETS TO URDU ALPHABET CONVERSION DICTIONARY-------------------------------------------------------------------------

ipa_urdu_dict[u'\u0251\u02D0'] = [u'\u0627'] #alif
ipa_urdu_dict[u'\u0294'] = [u'\u0627'] #alif
ipa_urdu_dict[u'\u2205'] = [u'\u0627'] #alif
ipa_urdu_dict[u'\u0061\u02D0'] = [u'\u0622'] #alif mad aa
ipa_urdu_dict[u'\u0062'] = [u'\u0628'] #bay
ipa_urdu_dict[u'\u0070'] = [u'\u067e'] #pay
ipa_urdu_dict[u'\u0074\u032A'] = [u'\u062a'] #tay
ipa_urdu_dict[u'\u0288'] = [u'\u0679'] #ttay
ipa_urdu_dict[u'\u0073'] = [u'\u062B'] #say
ipa_urdu_dict[u'\u0064\u0361\u0292'] = [u'\u062C'] #jeem
ipa_urdu_dict[u'\u0074\u0361\u0283'] = [u'\u0686'] #chay
ipa_urdu_dict[u'\u0068'] = [u'\u062D'] #hay
ipa_urdu_dict[u'\u0266'] = [u'\u062D'] #hay
ipa_urdu_dict[u'\u0078'] = [u'\u062E'] #khay
ipa_urdu_dict[u'\u0064\u032A'] = [u'\u062F'] #daal
ipa_urdu_dict[u'\u0256'] = [u'\u0688'] #ddaal
ipa_urdu_dict[u'\u007A'] = [u'\u0630'] #zaal
ipa_urdu_dict[u'\u0072'] = [u'\u0631'] #ray	
ipa_urdu_dict[u'\u027D'] = [u'\u0691'] #rray
ipa_urdu_dict[u'\u007A'] = [u'\u0632'] #zay
ipa_urdu_dict[u'\u0292'] = [u'\u0698'] #yay
ipa_urdu_dict[u'\u0073'] = [u'\u0633'] #seen........
ipa_urdu_dict[u'\u0283'] = [u'\u0634'] #sheen	
ipa_urdu_dict[u'\u0073'] = [u'\u0635'] #suaad
ipa_urdu_dict[u'\u007A'] = [u'\u0636'] #zawad
ipa_urdu_dict[u'\u0074\u032A'] = [u'\u0637'] #tuain
ipa_urdu_dict[u'\u007A'] = [u'\u0638'] #zuain
ipa_urdu_dict[u'\u0251\u02D0'] = [u'\u0639'] #aain
ipa_urdu_dict[u'\u006F\u02D0'] = [u'\u0639'] #aain	
ipa_urdu_dict[u'\u0065\u02D0'] = [u'\u0639'] #aain	
ipa_urdu_dict[u'\u0294'] = [u'\u0639'] #aain	
ipa_urdu_dict[u'\u0295'] = [u'\u0639'] #aain	
ipa_urdu_dict[u'\u2205'] = [u'\u0639'] #aain	
ipa_urdu_dict[u'\u0263'] = [u'\u063A'] #ghain
ipa_urdu_dict[u'\u0066'] = [u'\u0641'] #fay
ipa_urdu_dict[u'\u0071'] = [u'\u0642'] #kaaf
ipa_urdu_dict[u'\u006B'] = [u'\u06A9'] #kiyaaf
ipa_urdu_dict[u'\u0067'] = [u'\u06AF'] #gaaf
ipa_urdu_dict[u'\u006C'] = [u'\u0644'] #laam
ipa_urdu_dict[u'\u006D'] = [u'\u0645'] #meme
ipa_urdu_dict[u'\u006E'] = [u'\u0646'] #noon
ipa_urdu_dict[u'\u0272'] = [u'\u0646'] #noon
ipa_urdu_dict[u'\u0273'] = [u'\u0646'] #noon
ipa_urdu_dict[u'\u014B'] = [u'\u0646'] #noon
ipa_urdu_dict[u'\u0303'] = [u'\u06BA'] #noon ghunna
ipa_urdu_dict[u'\u028B'] = [u'\u0648'] #wow
ipa_urdu_dict[u'\u0075\u02D0'] = [u'\u0648'] #wow
ipa_urdu_dict[u'\u006F\u02D0'] = [u'\u0648'] #wow
ipa_urdu_dict[u'\u0254\u02D0'] = [u'\u0648'] #wow

ipa_urdu_dict[u'\u0068'] = [u'\u06C1',u'\u0647'] #hey
ipa_urdu_dict[u'\u0266'] = [u'\u06C1',u'\u0647'] #hey
ipa_urdu_dict[u'\u2205'] = [u'\u06C1',u'\u0647',u'\u2205'] #hey, #hey, hamza

#ipa_urdu_dict[u'\u0647'] = [u'\u0068',u'\u0266',u'\u2205'] #hey
ipa_urdu_dict[u'\u02B0'] = [u'\u06BE'] #dochashmi hey
ipa_urdu_dict[u'\u02B1'] = [u'\u06BE'] #dochashmi hey
ipa_urdu_dict[u'\u0294'] = [u'\u0621'] #hamza 
ipa_urdu_dict[u'\u006A'] = [u'\u06CC'] #choti yay
ipa_urdu_dict[u'\u0069\u02D0'] = [u'\u06CC'] #choti yay
ipa_urdu_dict[u'\u0251\u02D0'] = [u'\u06CC'] #choti yay 
ipa_urdu_dict[u'\u025B\u02D0'] = [u'\u06D2'] #bari yay
ipa_urdu_dict[u'\u0065\u02D0'] = [u'\u06D2'] #bari yay
	
#the goal of this function is to convert urdu words into equivalent IPA sounds
#input is list of urdu words
#output is list of ipa representation of these urdu words
def covertUrduWordsinIPA(urdu_words):
	
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
				print repr(alphabet)
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


def main():
	#opening the file for reading UTF-8 data
	urdu_file = codecs.open('urdu_test.txt', encoding='utf-8')
	for urdu_line in urdu_file:
		
		#removing useless characters from line
		urdu_line = urdu_line.replace('(', ' ').replace(')', ' ').replace('!',' ').replace('.',' ')

		#splitting the hindi line based on space
		urdu_words = urdu_line.split()
		for urdu_word in urdu_words:
			urdu_ipa_list = covertUrduWordsinIPA(urdu_word)
			#print hindi_ipa_list
	
main()
