import codecs
import re

urdu_character_mapping = dict()
urdu_character_mapping[u'\uFE81'] = u'\u0622' #alif mad aa
urdu_character_mapping[u'\u0622'] = u'\u0622' #alif mad aa
urdu_character_mapping[u'\u0623'] = u'\u0627' #hamza alif
urdu_character_mapping[u'\u0672'] = u'\u0627' #hamza alif
urdu_character_mapping[u'\u0625'] = u'\u0627' #alif hamza
urdu_character_mapping[u'\u0676'] = u'\u0624' #hamza wow
urdu_character_mapping[u'\uFE85'] = u'\u0624' #hamza wow
urdu_character_mapping[u'\u0624'] = u'\u0624' #hamza wow
urdu_character_mapping[u'\u0678'] = u'\u0626' #hamza yay
urdu_character_mapping[u'\u0626'] = u'\u0626' #hamza yay
urdu_character_mapping[u'\uFE8B'] = u'\u0626' #hamza yay
urdu_character_mapping[u'\uFE8C'] = u'\u0626' #hamza yay
urdu_character_mapping[u'\uFE8D'] = u'\u0627' #alif
urdu_character_mapping[u'\uFE8E'] = u'\u0627' #alif
urdu_character_mapping[u'\u0671'] = u'\u0627' #alif
urdu_character_mapping[u'\u0673'] = u'\u0627' #alif
urdu_character_mapping[u'\u0627'] = u'\u0627' #alif
urdu_character_mapping[u'\uFE8F'] = u'\u0628' #bay
urdu_character_mapping[u'\uFE91'] = u'\u0628' #bay
urdu_character_mapping[u'\uFE92'] = u'\u0628' #bay
urdu_character_mapping[u'\u0628'] = u'\u0628' #bay
urdu_character_mapping[u'\u0680'] = u'\u0628\u06C1' #bay do chashmi hey
urdu_character_mapping[u'\u067B'] = u'\u0628' #bay
urdu_character_mapping[u'\u067E'] = u'\u067E' #pay
urdu_character_mapping[u'\uFB57'] = u'\u067E' #pay
urdu_character_mapping[u'\uFB58'] = u'\u067E' #pay
urdu_character_mapping[u'\uFB59'] = u'\u067E' #pay
urdu_character_mapping[u'\uFB56'] = u'\u067E' #pay
urdu_character_mapping[u'\u06A6'] = u'\u067E\u06C1' #pay do chashmi hey
urdu_character_mapping[u'\u062A'] = u'\u062A' #tay
urdu_character_mapping[u'\u0629'] = u'\u062A' #tay
urdu_character_mapping[u'\u06C3'] = u'\u062A' #tay
urdu_character_mapping[u'\uFE95'] = u'\u062A' #tay
urdu_character_mapping[u'\uFE96'] = u'\u062A' #tay
urdu_character_mapping[u'\uFE97'] = u'\u062A' #tay
urdu_character_mapping[u'\uFE98'] = u'\u062A' #tay
urdu_character_mapping[u'\uFE93'] = u'\u062A' #tay
urdu_character_mapping[u'\u067A'] = u'\u0679' #ttay
urdu_character_mapping[u'\u067C'] = u'\u0679' #ttay
urdu_character_mapping[u'\u067D'] = u'\u0679' #ttay
urdu_character_mapping[u'\uFB67'] = u'\u0679' #ttay
urdu_character_mapping[u'\uFB69'] = u'\u0679' #ttay
urdu_character_mapping[u'\u067F'] = u'\u0679\u06C1' #ttay do chashmi hey
urdu_character_mapping[u'\u0679'] = u'\u0679' #ttay
urdu_character_mapping[u'\uFE99'] = u'\u062B' #say
urdu_character_mapping[u'\uFE9A'] = u'\u062B' #say
urdu_character_mapping[u'\uFE9B'] = u'\u062B' #say
urdu_character_mapping[u'\uFE9C'] = u'\u062B' #say
urdu_character_mapping[u'\u062B'] = u'\u062B' #say
urdu_character_mapping[u'\uFE9D'] = u'\u062C' #jeem
urdu_character_mapping[u'\uFE9E'] = u'\u062C' #jeem
urdu_character_mapping[u'\uFE9F'] = u'\u062C' #jeem
urdu_character_mapping[u'\uFEA0'] = u'\u062C' #jeem
urdu_character_mapping[u'\u062C'] = u'\u062C' #jeem
urdu_character_mapping[u'\u0684'] = u'\u062C' #jeem
urdu_character_mapping[u'\u0696'] = u'\u062C' #jeem
urdu_character_mapping[u'\u0686'] = u'\u0686' #chay
urdu_character_mapping[u'\uFB7C'] = u'\u0686' #chay
urdu_character_mapping[u'\uFB7D'] = u'\u0686' #chay
urdu_character_mapping[u'\u0687'] = u'\u0686\u06C1' #chay do chashmi hey
urdu_character_mapping[u'\u0681'] = u'\u062D' #halwa hey
urdu_character_mapping[u'\u062D'] = u'\u062D' #halwa hey
urdu_character_mapping[u'\uFEA1'] = u'\u062D' #halwa hey
urdu_character_mapping[u'\uFEA2'] = u'\u062D' #halwa hey
urdu_character_mapping[u'\uFEA3'] = u'\u062D' #halwa hey
urdu_character_mapping[u'\uFEA4'] = u'\u062D' #halwa hey
urdu_character_mapping[u'\u062E'] = u'\u062E' #khay
urdu_character_mapping[u'\u069A'] = u'\u062E' #khay
urdu_character_mapping[u'\uFEA6'] = u'\u062E' #khay
urdu_character_mapping[u'\uFEA7'] = u'\u062E' #khay
urdu_character_mapping[u'\uFEA8'] = u'\u062E' #khay
urdu_character_mapping[u'\uFEA9'] = u'\u062F' #daal
urdu_character_mapping[u'\uFEAA'] = u'\u062F' #daal
urdu_character_mapping[u'\u062F'] = u'\u062F' #daal
urdu_character_mapping[u'\u068F'] = u'\u062F' #daal
urdu_character_mapping[u'\u068C'] = u'\u062F\u06C1' #daal do chashmi hey
urdu_character_mapping[u'\uFEAB'] = u'\u0630' #zaal
urdu_character_mapping[u'\uFEAC'] = u'\u0630' #zaal
urdu_character_mapping[u'\u0630'] = u'\u0630' #zaal
urdu_character_mapping[u'\uFEAD'] = u'\u0631' #ray
urdu_character_mapping[u'\uFEAE'] = u'\u0631' #ray
urdu_character_mapping[u'\u0631'] = u'\u0631' #ray
urdu_character_mapping[u'\uFEAF'] = u'\u0632' #zay
urdu_character_mapping[u'\uFEB0'] = u'\u0632' #zay
urdu_character_mapping[u'\u0632'] = u'\u0632' #zay
urdu_character_mapping[u'\uFEB1'] = u'\u0633' #seen
urdu_character_mapping[u'\uFEB2'] = u'\u0633' #seen
urdu_character_mapping[u'\uFEB3'] = u'\u0633' #seen
urdu_character_mapping[u'\uFEB4'] = u'\u0633' #seen
urdu_character_mapping[u'\u0633'] = u'\u0633' #seen
urdu_character_mapping[u'\u0634'] = u'\u0634' #sheen
urdu_character_mapping[u'\u06FA'] = u'\u0634' #sheen
urdu_character_mapping[u'\uFEB6'] = u'\u0634' #sheen
urdu_character_mapping[u'\uFEB7'] = u'\u0634' #sheen
urdu_character_mapping[u'\uFEB8'] = u'\u0634' #sheen
urdu_character_mapping[u'\uFEB9'] = u'\u0635' #suaad
urdu_character_mapping[u'\uFEBA'] = u'\u0635' #suaad
urdu_character_mapping[u'\uFEBB'] = u'\u0635' #suaad
urdu_character_mapping[u'\uFEBC'] = u'\u0635' #suaad
urdu_character_mapping[u'\u0635'] = u'\u0635' #suaad
urdu_character_mapping[u'\uFEBD'] = u'\u0636' #zuaad
urdu_character_mapping[u'\uFEBE'] = u'\u0636' #zuaad
urdu_character_mapping[u'\uFEBF'] = u'\u0636' #zuaad
urdu_character_mapping[u'\uFEC0'] = u'\u0636' #zuaad
urdu_character_mapping[u'\u0636'] = u'\u0636' #zuaad
urdu_character_mapping[u'\uFEC3'] = u'\u0637' #tuain
urdu_character_mapping[u'\uFEC4'] = u'\u0637' #tuain
urdu_character_mapping[u'\u0637'] = u'\u0637' #tuain
urdu_character_mapping[u'\uFEC6'] = u'\u0638' #zuain
urdu_character_mapping[u'\uFEC7'] = u'\u0638' #zuain
urdu_character_mapping[u'\uFEC8'] = u'\u0638' #zuain
urdu_character_mapping[u'\u0638'] = u'\u0638' #zuain
urdu_character_mapping[u'\uFEC9'] = u'\u0639' #aain
urdu_character_mapping[u'\uFECA'] = u'\u0639' #aain
urdu_character_mapping[u'\uFECB'] = u'\u0639' #aain
urdu_character_mapping[u'\uFECC'] = u'\u0639' #aain
urdu_character_mapping[u'\u0639'] = u'\u0639' #aain
urdu_character_mapping[u'\u063A'] = u'\u063A' #ghain
urdu_character_mapping[u'\uFED0'] = u'\u063A' #ghain
urdu_character_mapping[u'\uFED1'] = u'\u0641' #fay
urdu_character_mapping[u'\uFED2'] = u'\u0641' #fay
urdu_character_mapping[u'\uFED3'] = u'\u0641' #fay
urdu_character_mapping[u'\uFED4'] = u'\u0641' #fay
urdu_character_mapping[u'\u0641'] = u'\u0641' #fay
urdu_character_mapping[u'\u0643'] = u'\u06A9' #kiyaaf
urdu_character_mapping[u'\u0649'] = u'\u06A9' #kiyaaf
urdu_character_mapping[u'\uFED9'] = u'\u06A9' #kiyaaf
urdu_character_mapping[u'\uFEDA'] = u'\u06A9' #kiyaaf
urdu_character_mapping[u'\uFEDB'] = u'\u06A9' #kiyaaf
urdu_character_mapping[u'\uFEDC'] = u'\u06A9' #kiyaaf
urdu_character_mapping[u'\u06AA'] = u'\u06A9' #kiyaaf
urdu_character_mapping[u'\u06A9'] = u'\u06A9' #kiyaaf
urdu_character_mapping[u'\uFB8F'] = u'\u06A9' #kiyaaf
urdu_character_mapping[u'\uFB90'] = u'\u06A9' #kiyaaf
urdu_character_mapping[u'\uFB91'] = u'\u06A9' #kiyaaf
urdu_character_mapping[u'\u06AF'] = u'\u06AF' #gaaf
urdu_character_mapping[u'\u06AB'] = u'\u06AF' #gaaf
urdu_character_mapping[u'\u06AC'] = u'\u06AF' #gaaf
urdu_character_mapping[u'\u06B3'] = u'\u06AF' #gaaf
urdu_character_mapping[u'\uFB93'] = u'\u06AF' #gaaf
urdu_character_mapping[u'\uFB94'] = u'\u06AF' #gaaf
urdu_character_mapping[u'\uFB95'] = u'\u06AF' #gaaf
urdu_character_mapping[u'\u0644'] = u'\u0644' #laam
urdu_character_mapping[u'\u06B5'] = u'\u0644' #laam
urdu_character_mapping[u'\u026D'] = u'\u0644' #laam
urdu_character_mapping[u'\uFEDD'] = u'\u0644' #laam
urdu_character_mapping[u'\uFEDE'] = u'\u0644' #laam
urdu_character_mapping[u'\uFEDF'] = u'\u0644' #laam
urdu_character_mapping[u'\uFEE0'] = u'\u0644' #laam
urdu_character_mapping[u'\u0645'] = u'\u0645' #meem
urdu_character_mapping[u'\uFEE1'] = u'\u0645' #meem
urdu_character_mapping[u'\uFEE2'] = u'\u0645' #meem
urdu_character_mapping[u'\uFEE3'] = u'\u0645' #meem
urdu_character_mapping[u'\uFEE4'] = u'\u0645' #meem
urdu_character_mapping[u'\u0642'] = u'\u0642' #kaaf
urdu_character_mapping[u'\u066F'] = u'\u0642' #kaaf
urdu_character_mapping[u'\uFED6'] = u'\u0642' #kaaf
urdu_character_mapping[u'\uFED7'] = u'\u0642' #kaaf
urdu_character_mapping[u'\uFED8'] = u'\u0642' #kaaf
urdu_character_mapping[u'\uFEE5'] = u'\u06BA' #noon
urdu_character_mapping[u'\uFEE6'] = u'\u06BA' #noon
urdu_character_mapping[u'\uFEE7'] = u'\u06BA' #noon
urdu_character_mapping[u'\uFEE8'] = u'\u06BA' #noon
urdu_character_mapping[u'\u06BA'] = u'\u06BA' #noon
urdu_character_mapping[u'\u0683'] = u'\u06BA' #noon
urdu_character_mapping[u'\u06AD'] = u'\u06BA' #noon
urdu_character_mapping[u'\u06B1'] = u'\u06BA' #noon
urdu_character_mapping[u'\u06BB'] = u'\u06BA' #noon
urdu_character_mapping[u'\u06BC'] = u'\u06BA' #noon
urdu_character_mapping[u'\u0647'] = u'\u06C1' #gol hey
urdu_character_mapping[u'\u06C1'] = u'\u06C1' #gol hey
urdu_character_mapping[u'\u06C0'] = u'\u06C1' #gol hey
urdu_character_mapping[u'\u06C2'] = u'\u06C1' #gol hey
urdu_character_mapping[u'\u06D5'] = u'\u06C1' #gol hey
urdu_character_mapping[u'\uFBA9'] = u'\u06C1' #gol hey
urdu_character_mapping[u'\uFBA6'] = u'\u06C1' #gol hey
urdu_character_mapping[u'\uFBA7'] = u'\u06C1' #gol hey
urdu_character_mapping[u'\uFBA8'] = u'\u06C1' #gol hey
urdu_character_mapping[u'\u06C8'] = u'\u0648' #wow
urdu_character_mapping[u'\u0648'] = u'\u0648' #wow
urdu_character_mapping[u'\uFEED'] = u'\u0648' #wow
urdu_character_mapping[u'\uFEEE'] = u'\u0648' #wow
urdu_character_mapping[u'\u06A4'] = u'\u0648' #wow
urdu_character_mapping[u'\u06C6'] = u'\u0648' #wow
urdu_character_mapping[u'\u06C7'] = u'\u0648' #wow
urdu_character_mapping[u'\u06CB'] = u'\u0648' #wow
urdu_character_mapping[u'\u0690'] = u'\u0688' #ddaal
urdu_character_mapping[u'\u0688'] = u'\u0688' #ddaal
urdu_character_mapping[u'\u0689'] = u'\u0688' #ddaal
urdu_character_mapping[u'\u068A'] = u'\u0688' #ddaal
urdu_character_mapping[u'\uFB88'] = u'\u0688' #ddaal
urdu_character_mapping[u'\uFB89'] = u'\u0688' #ddaal
urdu_character_mapping[u'\u068D'] = u'\u0688\u06C1' #ddaal do chashmi hey
urdu_character_mapping[u'\u068E'] = u'\u0698' #yay teen nuktoon wali
urdu_character_mapping[u'\u0698'] = u'\u0698' #yay teen nuktoon wali
urdu_character_mapping[u'\uFB8C'] = u'\u0691' #rray
urdu_character_mapping[u'\u0699'] = u'\u0691' #rray
urdu_character_mapping[u'\u0691'] = u'\u0691' #rray
urdu_character_mapping[u'\u0692'] = u'\u0691' #rray
urdu_character_mapping[u'\u0693'] = u'\u0691' #rray
urdu_character_mapping[u'\u0699'] = u'\u0691' #rray
urdu_character_mapping[u'\uFB8C'] = u'\u0691' #rray
urdu_character_mapping[u'\uFB8D'] = u'\u0691' #rray
urdu_character_mapping[u'\uFB9E'] = u'\u06BA' #noon ghunna
urdu_character_mapping[u'\uFB9F'] = u'\u06BA' #noon ghunna
urdu_character_mapping[u'\u06BA'] = u'\u06BA' #noon ghunna
urdu_character_mapping[u'\uFBAC'] = u'\u06C1' #do chashmi hey
urdu_character_mapping[u'\u06C1'] = u'\u06C1' #do chashmi hey
urdu_character_mapping[u'\uFBAB'] = u'\u06C1' #do chashmi hey
urdu_character_mapping[u'\uFBAD'] = u'\u06C1' #do chashmi hey
urdu_character_mapping[u'\u06D3'] = u'\u06D2' #bari yay
urdu_character_mapping[u'\uFBAE'] = u'\u06D2' #bari yay
urdu_character_mapping[u'\uFBAF'] = u'\u06D2' #bari yay
urdu_character_mapping[u'\u0640'] = u'\u06D2' #bari yay
urdu_character_mapping[u'\u06D2'] = u'\u06D2' #bari yay
urdu_character_mapping[u'\u0649'] = u'\u06CC' #choti yay
urdu_character_mapping[u'\u06CD'] = u'\u06CC' #choti yay
urdu_character_mapping[u'\u06CC'] = u'\u06CC' #choti yay
urdu_character_mapping[u'\u064A'] = u'\u06CC' #choti yay
urdu_character_mapping[u'\uFBFC'] = u'\u06CC' #choti yay
urdu_character_mapping[u'\uFBFD'] = u'\u06CC' #choti yay
urdu_character_mapping[u'\uFBFE'] = u'\u06CC' #choti yay
urdu_character_mapping[u'\uFBFF'] = u'\u06CC' #choti yay
urdu_character_mapping[u'\uFEEF'] = u'\u06CC' #choti yay
urdu_character_mapping[u'\uFEF0'] = u'\u06CC' #choti yay
urdu_character_mapping[u'\uFEF2'] = u'\u06CC' #choti yay
urdu_character_mapping[u'\uFEF3'] = u'\u06CC' #choti yay
urdu_character_mapping[u'\uFEF4'] = u'\u06CC' #choti yay
urdu_character_mapping[u'\u06CE'] = u'\u06CC' #choti yay
urdu_character_mapping[u'\u06D0'] = u'\u06CC' #choti yay

urdu_character_mapping[u'\u063C'] = '' #kiyaaf kay neechay teen nuktay
urdu_character_mapping[u'\u0674'] = '' #high hamza
urdu_character_mapping[u'\u0685'] = '' #halwa hey with three dots above
urdu_character_mapping[u'\u069E'] = '' #suaad with three dots above
urdu_character_mapping[u'\u06AE'] = '' #kaaf with three dots above
urdu_character_mapping[u'\u06E5'] = '' #choti wow
urdu_character_mapping[u'\u06EE'] = '' #daal with ulta v above
urdu_character_mapping[u'\u06EF'] = '' #ray with ulta v above
urdu_character_mapping[u'\u0758'] = '' #hay with three dots inside pointing up
urdu_character_mapping[u'\uFDF2'] = '' #symbol for Allah
urdu_character_mapping[u'\uFDFA'] = '' #salutation
urdu_character_mapping[u'\uFDFB'] = '' #salutation
urdu_character_mapping[u'\uFE70'] = '' #do zabar producing sound of noon
urdu_character_mapping[u'\uFE76'] = '' #zabar
urdu_character_mapping[u'\u064E'] = '' #zabar
urdu_character_mapping[u'\u0650'] = '' #zair
urdu_character_mapping[u'\u0651'] = '' #shad
urdu_character_mapping[u'\uFE78'] = '' #paish
urdu_character_mapping[u'\uFE80'] = '' #hamza
urdu_character_mapping[u'\uFEFB'] = '' #hamza
urdu_character_mapping[u'\uFEFC'] = '' #hamza
urdu_character_mapping[u'\u0621'] = '' #hamza
urdu_character_mapping[u'\u0674'] = '' #hamza
urdu_character_mapping[u'\uFE80'] = '' #hamza

def main():
	tabin = []
	tabout = []
	for k,v in urdu_character_mapping.items():
		tabin.append(k)
		tabout.append(v)

	translate_table = dict(zip(tabin, tabout))

	#opening the file for reading UTF-8 data
	#urdu_file = codecs.open('urdu.txt', encoding='utf-8')
	text_file = codecs.open('test.google.hin.urd.translated', encoding='utf-8')
	output_file = codecs.open("test.google.hin.urd.translated_standardized.txt", "w", "utf-8")
	# text_file = codecs.open('platts_urdu_updated.txt', encoding='utf-8')
	# output_file = codecs.open("platts_urdu_standardized.txt", "w", "utf-8")

	# text_file = codecs.open('web.urd.full.txt', encoding='utf-8')
	# output_file = codecs.open("web.urd.full_standardized.txt", "w", "utf-8")

	#looping over line by line in both files simultaneously
	#for urdu_line, hindi_line in zip(urdu_file, hindi_file):
	i = 0
	for line in text_file:
		diatrical_marks = u'\u063C\u0674\u0685\u069E\u06AE\u06E5\u06EE\u06EF\u0758\uFDF2\uFDFA\uFDFB\uFE70\uFE76\u064E\u0650\u0651\uFE78\uFE80\uFEFB\uFEFC\u0621\u0674\uFE80'
		removal_table = dict((ord(char), None) for char in diatrical_marks)
		line = line.translate(removal_table)
		line = line.strip()
		word = line.replace(u'\u06d4','').replace(u'\u2026','').replace(u'\u060c','').replace(u'\u061f','').replace('(', '').replace('!','').replace('.','').replace('?','').replace(';','')
		word = word.strip()
		if word and not word.isspace():
			replacement_word = []
			word=filter(lambda x: x in urdu_character_mapping, word)
			for alphabet in word:
				replacement_word.append(urdu_character_mapping[alphabet])
				if alphabet not in urdu_character_mapping:
					print 'Symbol not present', repr(alphabet)
			output_file.write(''.join(replacement_word)+' ')
			output_file.write('\n')
			i += 1	
	output_file.close()
	text_file.close()

main()
