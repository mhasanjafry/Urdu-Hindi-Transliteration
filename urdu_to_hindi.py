from itertools import izip as zip, count
import codecs
import itertools
import numpy as np

urdu_ipa_hindi_dict_start = dict()
urdu_ipa_hindi_dict_middle = dict()
urdu_ipa_hindi_dict_end = dict()
hindi_word_dict = dict()
unique_word_dict = dict()
ipa_hindi_dict=dict()
ipa_hindi_dict_start=dict()

#---------------------------HINDI ALPHABETS TO IPA CONVERSION DICTIONARY ( START)---------------------------------------------------------------------------------
ipa_hindi_dict_start[u'\u0259'] = [u'\u0905']  # DEVANAGARI LETTER  A
ipa_hindi_dict_start[u'\u0061'] = [u'\u0906']   # DEVANAGARI LETTER AA
ipa_hindi_dict_start[u'\u026A'] = [u'\u0907']   # DEVANAGARI LETTER I
ipa_hindi_dict_start[u'\u0069'] = [u'\u0908']  # DEVANAGARI LETTER II
ipa_hindi_dict_start[u'\u028A'] = [u'\u0909']   # DEVANAGARI LETTER U
ipa_hindi_dict_start[u'\u0075'] = [u'\u090A']   # DEVANAGARI LETTER UU
ipa_hindi_dict_start[u'\u090B'] = [u'\u090B']   # DEVANAGARI LETTER VOCALIC R (could not find)
ipa_hindi_dict_start[u'\u0065'] = [u'\u090F',u'\u0945']  # DEVANAGARI LETTER E
ipa_hindi_dict_start[u'\u025B'] = [u'\u0910']  # DEVANAGARI LETTER AI
ipa_hindi_dict_start[u'\u006F'] = [u'\u0913']   # DEVANAGARI LETTER O
ipa_hindi_dict_start[u'\u0254'] = [u'\u0914',u'\u0913',u'\u094b']   # DEVANAGARI LETTER AU
ipa_hindi_dict_start[u'\u0303'] = [u'\u0901', u'\u0902']   # DEVANAGARI SIGN CANDRABINDU
#ipa_hindi_dict_start[u'\u0902'] = [u'\u014B', u'\u0272', u'\u0273', u'\u006E', u'\u006D', u'\u0303']  # DEVANAGARI SIGN ANUSVARA
ipa_hindi_dict_start[u'\u006E'] = [u'\u0902']   # DEVANAGARI SIGN ANUSVARA, adjusted with Noon here
ipa_hindi_dict_start[u'\u0266'] = [u'\u0903']  # DEVANAGARI SIGN VISARGA
#ipa_hindi_dict_start[u'\u0065'] = []  # DEVANAGARI VOWEL SIGN CANDRA E (check)

# Independent vowels
# Consonants
ipa_hindi_dict_start[u'\u006B'] = [u'\u0915']  # DEVANAGARI LETTER  KA
ipa_hindi_dict_start[u'\u02B0'] = [u'\u0916'] # DEVANAGARI LETTER KHA
ipa_hindi_dict_start[u'\u0261'] = [u'\u0917']   # DEVANAGARI LETTER GA
ipa_hindi_dict_start[u'\u0324'] = [u'\u0918']   # DEVANAGARI LETTER GHA
ipa_hindi_dict_start[u'\u014B'] = [u'\u0919']   # DEVANAGARI LETTER NGA

ipa_hindi_dict_start[u'\u0074\u0361\u0283'] = [u'\u091A']   # DEVANAGARI LETTER CA
ipa_hindi_dict_start[u'\u0074\u0361\u0283\u02B0'] = [u'\u091B']   # DEVANAGARI LETTER CHA
ipa_hindi_dict_start[u'\u0064\u0361\u0292'] = [u'\u091C']  # DEVANAGARI LETTER JA
ipa_hindi_dict_start[u'\u0064\u0361\u0292\u0324'] = [u'\u091D']   # DEVANAGARI LETTER JHA
ipa_hindi_dict_start[u'\u0272'] = [u'\u091E']   # DEVANAGARI LETTER NYA

ipa_hindi_dict_start[u'\u0288'] = [u'\u091F']  # DEVANAGARI SIGN TTA
ipa_hindi_dict_start[u'\u0288\u02B0'] = [u'\u0920']   # DEVANAGARI SIGN TTHA
ipa_hindi_dict_start[u'\u0256'] = [u'\u0921']   # DEVANAGARI SIGN DDA
ipa_hindi_dict_start[u'\u0256\u0324'] = [u'\u0922']  # DEVANAGARI LETTER DDHA
ipa_hindi_dict_start[u'\u0273'] = [u'\u0923']   # DEVANAGARI LETTER NNA

ipa_hindi_dict_start[u'\u0074\u032A'] = [u'\u0924']  # DEVANAGARI LETTER TA
ipa_hindi_dict_start[u'\u0074\u032A\u02B0'] = [u'\u0925']   # DEVANAGARI LETTER THA
ipa_hindi_dict_start[u'\u0064'] = [u'\u0926']   # DEVANAGARI LETTER DA
ipa_hindi_dict_start[u'\u0064\u0324'] = [u'\u0927']   # DEVANAGARI LETTER DHA
ipa_hindi_dict_start[u'\u006E'] = [u'\u0928']   # DEVANAGARI LETTER NA

ipa_hindi_dict_start[u'\u0070'] = [u'\u092A']  # DEVANAGARI LETTER PA
ipa_hindi_dict_start[u'\u0070\u02B0'] = [u'\u092B']   # DEVANAGARI LETTER PHA
ipa_hindi_dict_start[u'\u0062'] = [u'\u092C']   # DEVANAGARI LETTER BA
ipa_hindi_dict_start[u'\u0062\u0324'] = [u'\u092D']   # DEVANAGARI LETTER BHA
ipa_hindi_dict_start[u'\u006D'] = [u'\u092E']   # DEVANAGARI LETTER MA

ipa_hindi_dict_start[u'\u006A'] = [u'\u092F']   # DEVANAGARI LETTER YA
ipa_hindi_dict_start[u'\u0072'] = [u'\u0930']   # DEVANAGARI LETTER RA
ipa_hindi_dict_start[u'\u006C'] = [u'\u0932']   # DEVANAGARI LETTER LA
ipa_hindi_dict_start[u'\u028B'] = [u'\u0935']   # DEVANAGARI LETTER VA
ipa_hindi_dict_start[u'\u0283'] = [u'\u0936']   # DEVANAGARI LETTER SHA

ipa_hindi_dict_start[u'\u0282'] = [u'\u0937']   # DEVANAGARI LETTER SSA
ipa_hindi_dict_start[u'\u0073'] = [u'\u0938']   # DEVANAGARI LETTER SA
ipa_hindi_dict_start[u'\u0266'] = [u'\u0939']  # DEVANAGARI LETTER HA

#Additional consonants
ipa_hindi_dict_start[u'\u0071'] = [u'\u0958']   # DEVANAGARI LETTER QA
ipa_hindi_dict_start[u'\u0078'] = [u'\u0959']   # DEVANAGARI LETTER KHHA
ipa_hindi_dict_start[u'\u0263'] = [u'\u095A']   # DEVANAGARI LETTER GHHA
ipa_hindi_dict_start[u'\u007A'] = [u'\u095B']   # DEVANAGARI LETTER ZA
ipa_hindi_dict_start[u'\u0256'] = [u'\u095C']   # DEVANAGARI LETTER DDDHA
ipa_hindi_dict_start[u'\u027D'] = [u'\u095C']   # DEVANAGARI LETTER DDDHA
ipa_hindi_dict_start[u'\u027D\u0324'] = [u'\u095D']  #rha

ipa_hindi_dict_start[u'\u0066'] = [u'\u095E']   # DEVANAGARI LETTER FA
ipa_hindi_dict_start[u'\u0928\u093C'] = [u'\u0929']   #DEVANAGARI LETTER NNNA
ipa_hindi_dict_start[u'\u0930\u093C'] = [u'\u0931']   # DEVANAGARI LETTER RRA
ipa_hindi_dict_start[u'\u092F\u093C'] = [u'\u095F']   # DEVANAGARI LETTER YYA

#---------------------------HINDI ALPHABETS TO IPA CONVERSION DICTIONARY (EXCEPT START)---------------------------------------------------------------------------------

ipa_hindi_dict[u'\u0259'] = [u'\u0905']  # DEVANAGARI LETTER  A
ipa_hindi_dict[u'\u0061'] = [u'\u0906',u'\u093E']   # DEVANAGARI LETTER AA
ipa_hindi_dict[u'\u026A'] = [u'\u0907',u'\u093F']   # DEVANAGARI LETTER I
ipa_hindi_dict[u'\u0069'] = [u'\u0908',u'\u0940']  # DEVANAGARI LETTER II
ipa_hindi_dict[u'\u028A'] = [u'\u0909',u'\u0941']   # DEVANAGARI LETTER U
ipa_hindi_dict[u'\u0075'] = [u'\u090A',u'\u0942']   # DEVANAGARI LETTER UU
ipa_hindi_dict[u'\u090B'] = [u'\u090B']   # DEVANAGARI LETTER VOCALIC R (could not find)
ipa_hindi_dict[u'\u0065'] = [u'\u090F',u'\u0947',u'\u0946',u'\u0945']  # DEVANAGARI LETTER E
ipa_hindi_dict[u'\u025B'] = [u'\u0910',u'\u0948']  # DEVANAGARI LETTER AI
ipa_hindi_dict[u'\u006F'] = [u'\u0913',u'\u094B',u'\u094A']   # DEVANAGARI LETTER O
ipa_hindi_dict[u'\u0254'] = [u'\u0914',u'\u094C',u'\u0913' ,u'\u094b' ]   # DEVANAGARI LETTER AU
ipa_hindi_dict[u'\u0303'] = [u'\u0901', u'\u0902']   # DEVANAGARI SIGN CANDRABINDU
ipa_hindi_dict[u'\u0902'] = [u'\u014B', u'\u0272', u'\u0273', u'\u006E', u'\u006D', u'\u0303']  # DEVANAGARI SIGN ANUSVARA
ipa_hindi_dict[u'\u006E'] = [u'\u0902']   # DEVANAGARI SIGN ANUSVARA, adjusted with Noon here
ipa_hindi_dict[u'\u0266'] = [u'\u0903']  # DEVANAGARI SIGN VISARGA

# Independent vowels
# Consonants
ipa_hindi_dict[u'\u006B'] = [u'\u0915']  # DEVANAGARI LETTER  KA
ipa_hindi_dict[u'\u02B0'] = [u'\u0916'] # DEVANAGARI LETTER KHA
ipa_hindi_dict[u'\u0261'] = [u'\u0917']   # DEVANAGARI LETTER GA
ipa_hindi_dict[u'\u0324'] = [u'\u0918']   # DEVANAGARI LETTER GHA
ipa_hindi_dict[u'\u014B'] = [u'\u0919']   # DEVANAGARI LETTER NGA

ipa_hindi_dict[u'\u0074\u0361\u0283'] = [u'\u091A']   # DEVANAGARI LETTER CA
ipa_hindi_dict[u'\u0074\u0361\u0283\u02B0'] = [u'\u091B']   # DEVANAGARI LETTER CHA
ipa_hindi_dict[u'\u0064\u0361\u0292'] = [u'\u091C']  # DEVANAGARI LETTER JA
ipa_hindi_dict[u'\u0064\u0361\u0292\u0324'] = [u'\u091D']   # DEVANAGARI LETTER JHA
ipa_hindi_dict[u'\u0272'] = [u'\u091E']   # DEVANAGARI LETTER NYA

ipa_hindi_dict[u'\u0288'] = [u'\u091F']  # DEVANAGARI SIGN TTA
ipa_hindi_dict[u'\u0288\u02B0'] = [u'\u0920']   # DEVANAGARI SIGN TTHA
ipa_hindi_dict[u'\u0256'] = [u'\u0921']   # DEVANAGARI SIGN DDA
ipa_hindi_dict[u'\u0256\u0324'] = [u'\u0922']  # DEVANAGARI LETTER DDHA
ipa_hindi_dict[u'\u0273'] = [u'\u0923']   # DEVANAGARI LETTER NNA

ipa_hindi_dict[u'\u0074\u032A'] = [u'\u0924']  # DEVANAGARI LETTER TA
ipa_hindi_dict[u'\u0074\u032A\u02B0'] = [u'\u0925']   # DEVANAGARI LETTER THA
ipa_hindi_dict[u'\u0064'] = [u'\u0926']   # DEVANAGARI LETTER DA
ipa_hindi_dict[u'\u0064\u0324'] = [u'\u0927']   # DEVANAGARI LETTER DHA
ipa_hindi_dict[u'\u027D\u0324'] = [u'\u095D']  #rha


ipa_hindi_dict[u'\u006E'] = [u'\u0928']   # DEVANAGARI LETTER NA

ipa_hindi_dict[u'\u0070'] = [u'\u092A']  # DEVANAGARI LETTER PA
ipa_hindi_dict[u'\u0070\u02B0'] = [u'\u092B']   # DEVANAGARI LETTER PHA
ipa_hindi_dict[u'\u0062'] = [u'\u092C']   # DEVANAGARI LETTER BA
ipa_hindi_dict[u'\u0062\u0324'] = [u'\u092D']   # DEVANAGARI LETTER BHA
ipa_hindi_dict[u'\u006D'] = [u'\u092E']   # DEVANAGARI LETTER MA

ipa_hindi_dict[u'\u006A'] = [u'\u092F']   # DEVANAGARI LETTER YA
ipa_hindi_dict[u'\u0072'] = [u'\u0930']   # DEVANAGARI LETTER RA
ipa_hindi_dict[u'\u006C'] = [u'\u0932']   # DEVANAGARI LETTER LA
ipa_hindi_dict[u'\u028B'] = [u'\u0935']   # DEVANAGARI LETTER VA
ipa_hindi_dict[u'\u0283'] = [u'\u0936']   # DEVANAGARI LETTER SHA

ipa_hindi_dict[u'\u0282'] = [u'\u0937']   # DEVANAGARI LETTER SSA
ipa_hindi_dict[u'\u0073'] = [u'\u0938']   # DEVANAGARI LETTER SA
ipa_hindi_dict[u'\u0266'] = [u'\u0939']  # DEVANAGARI LETTER HA

#Additional consonants
ipa_hindi_dict[u'\u0071'] = [u'\u0958']   # DEVANAGARI LETTER QA
ipa_hindi_dict[u'\u0078'] = [u'\u0959']   # DEVANAGARI LETTER KHHA
ipa_hindi_dict[u'\u0263'] = [u'\u095A']   # DEVANAGARI LETTER GHHA
ipa_hindi_dict[u'\u007A'] = [u'\u095B']   # DEVANAGARI LETTER ZA
ipa_hindi_dict[u'\u0256'] = [u'\u095C']   # DEVANAGARI LETTER DDDHA
ipa_hindi_dict[u'\u027D'] = [u'\u095C']   # DEVANAGARI LETTER DDDHA
ipa_hindi_dict[u'\u0066'] = [u'\u095E']   # DEVANAGARI LETTER FA
ipa_hindi_dict[u'\u0928\u093C'] = [u'\u0929']   #DEVANAGARI LETTER NNNA
ipa_hindi_dict[u'\u0930\u093C'] = [u'\u0931']   # DEVANAGARI LETTER RRA
ipa_hindi_dict[u'\u092F\u093C'] = [u'\u095F']   # DEVANAGARI LETTER YYA

#-------------------------------------------------HINDI IPA TO URDU ALPHABET START DICTIONARY-------------------------------------------------------------
urdu_ipa_hindi_dict_start[u'\u094D'] = [] #replacing hallant with no symbol, handled in code
urdu_ipa_hindi_dict_start[u'\u0651'] = [u'\u0651']  #replacing shad with shad, handled in code

#--right table
urdu_ipa_hindi_dict_start[u'\u0627'] = [u'\u0259',u'\u0061',u'\u028A',u'\u0075'] #A
urdu_ipa_hindi_dict_start[u'\u0639'] = [u'\u0259',u'\u0061'] #A
urdu_ipa_hindi_dict_start[u'\u0622'] = [u'\u0061',u'\u0259'] #AA
urdu_ipa_hindi_dict_start[u'\u0627\u06CC'] = [u'\u0069',u'\u0065']    # 4 II
urdu_ipa_hindi_dict_start[u'\u0627\u0648']=[u'\u0075',u'\u006F',u'\u0254'] # 6 rule:
urdu_ipa_hindi_dict_start[u'\u0627\u0624']=[u'\u0075',u'\u006F',u'\u0254']# 6 rule:
urdu_ipa_hindi_dict_start[u'\u0631'] = [u'\u090B']    # 7 hindi character rhi ...no ipa ...directly mapping characters
urdu_ipa_hindi_dict_start [u'\u0627\uFBFE']  = [u'\u0065',u'\u025B']  # 8  beginning alif yay, middle yay, end bari yay
urdu_ipa_hindi_dict_start [u'\u0646'] = [u'\u006E', u'\u0303',u'\u014B',u'\u0272',u'\u0273',u'\u006E',u'\u006D',u'\u0303' ]   # 12 rule: start or middle noon, end noon ghunna

#--left table
urdu_ipa_hindi_dict_start[u'\u067e\u06be'] = [u'\u0070\u02B0']
urdu_ipa_hindi_dict_start[u'\u06be'] = [u'\u0266']
urdu_ipa_hindi_dict_start[u'\u06D2'] = [u'\u006A', u'\u0065']#ya
urdu_ipa_hindi_dict_start[u'\u06A9'] = [u'\u006B', u'\u0071']  #1 kiyaaf or kaaf
urdu_ipa_hindi_dict_start[u'\u0642'] = [u'\u006B', u'\u0071']  #1 kiyaaf or kaaf
urdu_ipa_hindi_dict_start[u'\u06A9\u06BE'] = [u'\u02B0'] # 2 kiyaaf doochasmi hey or kiyaaf gol hey
urdu_ipa_hindi_dict_start[u'\u062E'] = [u'\u02B0',u'\u0078'] # 2 kiyaaf doochasmi hey or kiyaaf gol hey
urdu_ipa_hindi_dict_start[u'\u06AF'] = [u'\u0261']   # 3 gaaf, ghain (Ghain Added by Sami after empirical testing)
urdu_ipa_hindi_dict_start[u'\u063A'] = [u'\u0261',u'\u0263']   # 3 gaaf, ghain (Ghain Added by Sami after empirical testing)
urdu_ipa_hindi_dict_start[u'\u06AF\u06BE'] = [u'\u0324']   # 4 gaaf doochasmi hey or gaaf gol hey or ghain doochasmi hey or ghain gol hey
urdu_ipa_hindi_dict_start[u'\u063A\u06BE'] = [u'\u0324']   # 4 gaaf doochasmi hey or gaaf gol hey or ghain doochasmi hey or ghain gol hey
urdu_ipa_hindi_dict_start[u'\u0686'] = [u'\u0074\u0361\u0283']   # 6 chay
urdu_ipa_hindi_dict_start[u'\u0686\u06BE'] = [u'\u0074\u0361\u0283\u02B0']   # 7 chay doochasmi hey or chay gol hey
urdu_ipa_hindi_dict_start[u'\u062C'] = [u'\u0064\u0361\u0292']   # 8 jeem
urdu_ipa_hindi_dict_start[u'\u062C\u06BE'] = [u'\u0064\u0361\u0292\u0324']    # 9 jeem doochasmi hey or jeem gol hey
urdu_ipa_hindi_dict_start[u'\u0679'] = [u'\u0288']   # 11 ttay
urdu_ipa_hindi_dict_start[u'\u0679\u06BE'] = [u'\u0288\u02B0']   # 12 ttay doochasmi hey or ttay gol hey
urdu_ipa_hindi_dict_start[u'\u0688'] = [u'\u0256']   # 13 ddaal or rray
urdu_ipa_hindi_dict_start[u'\u0691'] = [u'\u0256',u'\u027D']   # 13 ddaal or rray
urdu_ipa_hindi_dict_start[u'\u0688\u06BE'] = [u'\u0256\u0324']   # 14 ddaal doochasmi hey or ddaal gol hey, with rray too
urdu_ipa_hindi_dict_start[u'\u0691\u06BE'] = [u'\u0256\u0324',u'\u027D\u0324']   # 14 ddaal doochasmi hey or ddaal gol hey, with rray too
urdu_ipa_hindi_dict_start[u'\u062a'] = [u'\u0074\u032A']   # 16 tay or #tuain
urdu_ipa_hindi_dict_start[u'\u0637'] = [u'\u0074\u032A']   # 16 tay or #tuain
urdu_ipa_hindi_dict_start[u'\u062a\u06BE'] = [u'\u0074\u032A\u02B0']   # 17 tay doochasmi hey or tay gol hey
urdu_ipa_hindi_dict_start[u'\u0637\u06BE'] = [u'\u0074\u032A\u02B0']   # 17 tay doochasmi hey or tay gol hey
urdu_ipa_hindi_dict_start[u'\u062F'] = [u'\u0064']    # 18 daal
urdu_ipa_hindi_dict_start[u'\u062F\u06BE'] = [u'\u0064\u0324']   # 19 daal doochasmi hey or daal gol hey
urdu_ipa_hindi_dict_start[u'\u067e'] = [u'\u0070']   # 21 pay
urdu_ipa_hindi_dict_start[u'\u0641'] = [u'\u0070\u02B0',u'\u0066']  # 22 pay doochasmi hey or pay gol heychanged here by Sami
urdu_ipa_hindi_dict_start[u'\u0628'] = [u'\u0062']   # 23 bay
urdu_ipa_hindi_dict_start[u'\u0628\u06BE'] = [u'\u0062\u0324']   # 24 bay doochasmi hey or bay gol hey
urdu_ipa_hindi_dict_start[u'\u0645'] = [u'\u006D']   # 25 meem
urdu_ipa_hindi_dict_start[u'\u06CC']  = [u'\u006A']  # 26 rule: if in the start, yay
urdu_ipa_hindi_dict_start[u'\u0631'] = [u'\u0072']   # 27 ray
urdu_ipa_hindi_dict_start[u'\u0644']  = [u'\u006C']  # 28 laam
urdu_ipa_hindi_dict_start[u'\u0648'] = [u'\u028B']   # 29 wow
urdu_ipa_hindi_dict_start[u'\u0634']  = [u'\u0283',u'\u0282']  # 30 sheen
urdu_ipa_hindi_dict_start[u'\u0633'] = [u'\u0073']   # 32 seen, say, suaad
urdu_ipa_hindi_dict_start[u'\u062B'] = [u'\u0073']   # 32 seen, say, suaad
urdu_ipa_hindi_dict_start[u'\u0635'] = [u'\u0073']   # 32 seen, say, suaad
urdu_ipa_hindi_dict_start[u'\u062D']  = [u'\u0266']  # 33 hay or gol hay
urdu_ipa_hindi_dict_start[u'\u06C1']  = [u'\u0266']  # 33 hay or gol hay
urdu_ipa_hindi_dict_start[u'\u0630']  = [u'\u007A']  # 37 zaal, zay, zuaad, zuain
urdu_ipa_hindi_dict_start[u'\u0632']  = [u'\u007A', u'\u0064\u0361\u0292']  # 37 zaal, zay, zuaad, zuain
urdu_ipa_hindi_dict_start[u'\u0636']  = [u'\u007A']  # 37 zaal, zay, zuaad, zuain
urdu_ipa_hindi_dict_start[u'\u0638']  = [u'\u007A']  # 37 zaal, zay, zuaad, zuain
urdu_ipa_hindi_dict_start[u'\u0698'] = [u'\u0292']   # 38 yay

#-------------------------------------------------HINDI IPA TO URDU ALPHABET MIDDLE DICTIONARY-------------------------------------------------------------
urdu_ipa_hindi_dict_middle[u'\u094D'] = [] #replacing hallant with no symbol, handled in code
urdu_ipa_hindi_dict_middle[u'\u0651'] = [u'\u0651']  #replacing shad with shad, handled in code

#--right table
urdu_ipa_hindi_dict_middle[u'\u0627'] = [u'\u0061']   # 2 if in the start alif mad aa, if in the middle, alif, alif mad aa, khari zabar
urdu_ipa_hindi_dict_middle[u'\u0622'] = [u'\u0061']   # 2 if in the start alif mad aa, if in the middle, alif, alif mad aa, khari zabar
urdu_ipa_hindi_dict_middle[u'\u0670'] = [u'\u0061']   # 2 if in the start alif mad aa, if in the middle, alif, alif mad aa, khari zabar
urdu_ipa_hindi_dict_middle[u'\u0626'] = [u'\u026A', u'\u0069',u'\u006A']  # 3 earlier hamza choti yay were two characters, now using single character that represents the same thing. Also can be zair
urdu_ipa_hindi_dict_middle[u'\u0648'] = [u'\u028A', u'\u0075', u'\u006F', u'\u028B',u'\u0254']   # 5 rule: middle paish
urdu_ipa_hindi_dict_middle[u'\u0624'] = [u'\u0075', u'\u006F', u'\u028B',u'\u0254']   # 6 middle wow or paish
urdu_ipa_hindi_dict_middle[u'\u0631'] = [u'\u090B',u'\u0072']   # 7 hindi character rhi ...no ipa ...directly mapping characters
urdu_ipa_hindi_dict_middle[u'\u06CC'] = [u'\u0065',u'\u006A',u'\u025B',u'\u0069']   # 8  beginning alif yay, middle yay, end bari yay
urdu_ipa_hindi_dict_middle [u'\u0646'] = [u'\u006E', u'\u0303',u'\u014B',u'\u0272',u'\u0273',u'\u006E',u'\u006D',u'\u0303' ]   # 12 rule: start or middle noon, end noon ghunna

#--left table
urdu_ipa_hindi_dict_middle[u'\u067e\u06be'] = [u'\u0070\u02B0']
urdu_ipa_hindi_dict_middle[u'\u06be'] = [u'\u0266']
urdu_ipa_hindi_dict_middle[u'\u06D2'] = [u'\u006A',u'\u0065',u'\u026A',u'\u0069' ]#ya ey ii
urdu_ipa_hindi_dict_middle[u'\u0639'] = [u'\u0259',u'\u0061']
urdu_ipa_hindi_dict_middle[u'\u06A9'] = [u'\u006B',u'\u0071']   #1 kiyaaf or kaaf
urdu_ipa_hindi_dict_middle[u'\u0642'] = [u'\u006B',u'\u0071']   #1 kiyaaf or kaaf
urdu_ipa_hindi_dict_middle[u'\u06A9\u06BE'] = [u'\u02B0']  # 2 kiyaaf doochasmi hey or kiyaaf gol hey
urdu_ipa_hindi_dict_middle[u'\u062E'] = [u'\u02B0',u'\u0078']  # 2 kiyaaf doochasmi hey or kiyaaf gol hey
urdu_ipa_hindi_dict_middle[u'\u06AF'] = [u'\u0261']   # 3 gaaf, ghain (Ghain Added by Sami after empirical testing)
urdu_ipa_hindi_dict_middle[u'\u063A'] = [u'\u0261',u'\u0263']   # 3 gaaf, ghain (Ghain Added by Sami after empirical testing)
urdu_ipa_hindi_dict_middle[u'\u06AF\u06BE'] = [u'\u0324']   # 4 gaaf doochasmi hey or gaaf gol hey or ghain doochasmi hey or ghain gol hey
urdu_ipa_hindi_dict_middle[u'\u063A\u06BE'] = [u'\u0324']   # 4 gaaf doochasmi hey or gaaf gol hey or ghain doochasmi hey or ghain gol hey
urdu_ipa_hindi_dict_middle[u'\u0686']  = [u'\u0074\u0361\u0283']  # 6 chay
urdu_ipa_hindi_dict_middle [u'\u0686\u06BE'] = [u'\u0074\u0361\u0283\u02B0']  # 7 chay doochasmi hey or chay gol hey
urdu_ipa_hindi_dict_middle[u'\u062C'] = [u'\u0064\u0361\u0292']   # 8 jeem
urdu_ipa_hindi_dict_middle[u'\u062C\u06BE'] = [u'\u0064\u0361\u0292\u0324']  # 9 jeem doochasmi hey or jeem gol hey
urdu_ipa_hindi_dict_middle[u'\u0679'] = [u'\u0288']   # 11 rule: ttay
urdu_ipa_hindi_dict_middle[u'\u0679\u06BE']  = [u'\u0288\u02B0']  # 12 ttay doochasmi hey or ttay gol hey
urdu_ipa_hindi_dict_middle[u'\u0688']  = [u'\u0256',u'\u027D']  # 13 ddaal or rray
urdu_ipa_hindi_dict_middle[u'\u0691']  = [u'\u0256']  # 13 ddaal or rray
urdu_ipa_hindi_dict_middle[u'\u0688\u06BE'] = [u'\u0256\u0324']  # 14 ddaal doochasmi hey or ddaal gol hey with rray too
urdu_ipa_hindi_dict_middle[u'\u0691\u06BE'] = [u'\u0256\u0324',u'\u027D\u0324']  # 14 ddaal doochasmi hey or ddaal gol hey with rray too
urdu_ipa_hindi_dict_middle[u'\u062a'] = [u'\u0074\u032A']   # 16 tay or #tuain
urdu_ipa_hindi_dict_middle[u'\u0637'] = [u'\u0074\u032A']   # 16 tay or #tuain
urdu_ipa_hindi_dict_middle[u'\u062a\u06BE'] = [u'\u0074\u032A\u02B0']   # 17 tay doochasmi hey or tay gol hey
urdu_ipa_hindi_dict_middle[u'\u062F'] = [u'\u0064']  # 18 daal
urdu_ipa_hindi_dict_middle[u'\u062F\u06BE'] = [u'\u0064\u0324']   # 19 daal doochasmi hey or daal gol hey
urdu_ipa_hindi_dict_middle[u'\u06BA'] = [u'\u006E',u'\u0902']   # 20 rule: start or middle noon, end noon ghunna
urdu_ipa_hindi_dict_middle[u'\u067e']  = [u'\u0070']  # 21 pay
urdu_ipa_hindi_dict_middle[u'\u0641'] = [u'\u0070\u02B0',u'\u0066']  # 22  fay changed here by Sami
urdu_ipa_hindi_dict_middle[u'\u0628'] = [u'\u0062']  # 23 bay
urdu_ipa_hindi_dict_middle[u'\u0628\u06BE']  = [u'\u0062\u0324']  # 24 bay doochasmi hey or bay gol hey
urdu_ipa_hindi_dict_middle[u'\u0645'] = [u'\u006D']   # 25 meem
urdu_ipa_hindi_dict_middle[u'\u0644']  = [u'\u006C']  # 28 laam
urdu_ipa_hindi_dict_middle[u'\u0634'] = [u'\u0283',u'\u0282']   # 30 sheen
urdu_ipa_hindi_dict_middle[u'\u0633'] = [u'\u0073']   # 32 seen, say, suaad
urdu_ipa_hindi_dict_middle[u'\u062B'] = [u'\u0073']   # 32 seen, say, suaad
urdu_ipa_hindi_dict_middle[u'\u0635'] = [u'\u0073']   # 32 seen, say, suaad
urdu_ipa_hindi_dict_middle[u'\u062D'] = [u'\u0266']   # 33 hay or gol hay
urdu_ipa_hindi_dict_middle[u'\u06C1'] = [u'\u0266']   # 33 hay or gol hay
urdu_ipa_hindi_dict_middle[u'\u0630'] = [u'\u007A']   # 37 zaal, zay, zuaad, zuain
urdu_ipa_hindi_dict_middle[u'\u0632'] = [u'\u007A']   # 37 zaal, zay, zuaad, zuain
urdu_ipa_hindi_dict_middle[u'\u0636'] = [u'\u007A']   # 37 zaal, zay, zuaad, zuain
urdu_ipa_hindi_dict_middle[u'\u0638'] = [u'\u007A']   # 37 zaal, zay, zuaad, zuain
urdu_ipa_hindi_dict_middle[u'\u0698'] = [u'\u0292']   # 38 yay

#-------------------------------------------------HINDI IPA TO URDU ALPHABET END DICTIONARY-------------------------------------------------------------
#All words with hay sounds in left table, if in hindi same character appears with hallant, to remove the character and write mad instead

urdu_ipa_hindi_dict_end[u'\u094D'] = [] #replacing hallant with no symbol, handled in code
urdu_ipa_hindi_dict_end[u'\u0651'] = [u'\u0651'] #replacing shad with shad, handled in code

#--right table
urdu_ipa_hindi_dict_end[u'\u0626'] = [u'\u026A', u'\u0069',u'\u006A']  # 3 earlier hamza choti yay were two characters, now using single character that represents the same thing. Also can be zair
urdu_ipa_hindi_dict_end[u'\u0639'] = [u'\u0259',u'\u0061'] #A
urdu_ipa_hindi_dict_end[u'\u0622'] = [u'\u0061'] #AA
urdu_ipa_hindi_dict_end[u'\u06CC'] = [u'\u026A' ,u'\u0069',u'\u0065' ] #badi yay or choti yay
urdu_ipa_hindi_dict_end[u'\u0627'] = [u'\u0259',u'\u0061']  #1 alif
urdu_ipa_hindi_dict_end[u'\u06CC\u0670'] = [u'\u0061']   # 2 rule if in the end, alif or choti yay khari zabar as in aalaa
urdu_ipa_hindi_dict_end[u'\u06C1'] = [u'\u0061',u'\u0266']   # 2 rule if in the end, alif or choti yay khari zabar as in aalaa
urdu_ipa_hindi_dict_end[u'\u0648'] = [u'\u0075',u'\u006F',u'\u028B',u'\u0254']   # 6 ending wow or paish
urdu_ipa_hindi_dict_end[u'\u0624'] = [u'\u0075',u'\u006F',u'\u028B',u'\u0254']   # 6 ending wow or paish
urdu_ipa_hindi_dict_end[u'\0631'] = [u'\u090B']   # 7 hindi character rhi ...no ipa ...directly mapping characters
urdu_ipa_hindi_dict_end[u'\u06D2'] = [u'\u0065',u'\u006A',u'\u025B']   # 8  beginning alif yay, middle yay, end bari yay
urdu_ipa_hindi_dict_end [u'\u06BA'] = [u'\u0303',u'\u014B',u'\u0272',u'\u0273',u'\u006E',u'\u006D',u'\u0303',u'\u028A' ]   # 12 rule: start or middle noon, end noon ghunna

#--left table
urdu_ipa_hindi_dict_end[u'\u067e\u06be'] = [u'\u0070\u02B0']
urdu_ipa_hindi_dict_end[u'\u06be'] = [u'\u0266']
urdu_ipa_hindi_dict_end[u'\u06A9'] = [u'\u006B',u'\u0071']  #1 kiyaaf or kaaf
urdu_ipa_hindi_dict_end[u'\u0642'] = [u'\u006B',u'\u0071']  #1 kiyaaf or kaaf
urdu_ipa_hindi_dict_end[u'\u06A9\u06BE'] = [u'\u02B0']   # 2 kiyaaf doochasmi hey or kiyaaf gol hey
urdu_ipa_hindi_dict_end[u'\u062E'] = [u'\u02B0',u'\u0078']   # 2 kiyaaf doochasmi hey or kiyaaf gol hey
urdu_ipa_hindi_dict_end[u'\u06AF'] = [u'\u0261']   # 3 gaaf, ghain (Ghain Added by Sami after empirical testing)
urdu_ipa_hindi_dict_end[u'\u063A'] = [u'\u0261',u'\u0263']   # 3 gaaf, ghain (Ghain Added by Sami after empirical testing)
urdu_ipa_hindi_dict_end[u'\u06AF\u06BE'] = [u'\u0324']   # 4 gaaf doochasmi hey or gaaf gol hey or ghain doochasmi hey or ghain gol hey
urdu_ipa_hindi_dict_end[u'\u063A\u06BE'] = [u'\u0324']   # 4 gaaf doochasmi hey or gaaf gol hey or ghain doochasmi hey or ghain gol hey
urdu_ipa_hindi_dict_end[u'\u0686'] = [u'\u0074\u0361\u0283']   # 6 chay
urdu_ipa_hindi_dict_end[u'\u0686\u06BE'] = [u'\u0074\u0361\u0283\u02B0']   # 7 chay doochasmi hey or chay gol hey
urdu_ipa_hindi_dict_end[u'\u062C']  = [u'\u0064\u0361\u0292']  # 8 jeem
urdu_ipa_hindi_dict_end[u'\u062C\u06BE'] = [u'\u0064\u0361\u0292\u0324']   # 9 jeem doochasmi hey or jeem gol hey
urdu_ipa_hindi_dict_end[u'\u0679'] = [u'\u0288']   # 11 rule: ttay
urdu_ipa_hindi_dict_end[u'\u0679\u06BE']  = [u'\u0288\u02B0']  # 12 ttay doochasmi hey or ttay gol hey
urdu_ipa_hindi_dict_end [u'\u0688'] = [u'\u0256']  # 13 ddaal or rray
urdu_ipa_hindi_dict_end [u'\u0691'] = [u'\u0256',u'\u027D']  # 13 ddaal or rray
urdu_ipa_hindi_dict_end[u'\u0688\u06BE'] = [u'\u0256\u0324']   # 14 ddaal doochasmi hey or ddaal gol hey, with rray too
urdu_ipa_hindi_dict_end[u'\u0691\u06BE'] = [u'\u0256\u0324',u'\u027D\u0324']   # 14 ddaal doochasmi hey or ddaal gol hey, with rray too
urdu_ipa_hindi_dict_end[u'\u062a'] = [u'\u0074\u032A']   # 16 tay or #tuain
urdu_ipa_hindi_dict_end[u'\u0637'] = [u'\u0074\u032A']   # 16 tay or #tuain
urdu_ipa_hindi_dict_end[u'\u062a\u06BE'] = [u'\u0074\u032A\u02B0']   # 17 tay doochasmi hey or tay gol hey
urdu_ipa_hindi_dict_end [u'\u062F'] = [u'\u0064']   # 18 daal
urdu_ipa_hindi_dict_end[u'\u062F\u06BE'] = [u'\u0064\u0324']   # 19 daal doochasmi hey or daal gol hey
urdu_ipa_hindi_dict_end[u'\u0646'] = [u'\u006E']   # 20 rule: start or middle noon, end noon ghunna
urdu_ipa_hindi_dict_end[u'\u067e'] = [u'\u0070']   # 21 pay
urdu_ipa_hindi_dict_end[u'\u0641'] = [u'\u0070\u02B0', u'\u0066']  # 22 changed to fay by Sami
urdu_ipa_hindi_dict_end[u'\u0628']  = [u'\u0062']  # 23 bay
urdu_ipa_hindi_dict_end[u'\u0628\u06BE'] = [u'\u0062\u0324']   # 24 bay doochasmi hey or bay gol hey
urdu_ipa_hindi_dict_end[u'\u0645'] = [u'\u006D']   # 25 meem
urdu_ipa_hindi_dict_end[u'\u0631'] = [u'\u0072']   # 27 ray
urdu_ipa_hindi_dict_end[u'\u0644']  = [u'\u006C']  # 28 laam
urdu_ipa_hindi_dict_end[u'\u0634'] = [u'\u0283',u'\u0282']   # 30 sheen
urdu_ipa_hindi_dict_end[u'\u0633']  = [u'\u0073']  # 32 seen, say, suaad
urdu_ipa_hindi_dict_end[u'\u062B']  = [u'\u0073']  # 32 seen, say, suaad
urdu_ipa_hindi_dict_end[u'\u0635']  = [u'\u0073']  # 32 seen, say, suaad
urdu_ipa_hindi_dict_end[u'\u062D']  = [u'\u0266']  # 33 hay or gol hay
urdu_ipa_hindi_dict_end[u'\u0630'] = [u'\u007A']   # 37 zaal, zay, zuaad, zuain
urdu_ipa_hindi_dict_end[u'\u0632'] = [u'\u007A']   # 37 zaal, zay, zuaad, zuain
urdu_ipa_hindi_dict_end[u'\u0636'] = [u'\u007A']   # 37 zaal, zay, zuaad, zuain
urdu_ipa_hindi_dict_end[u'\u0638'] = [u'\u007A']   # 37 zaal, zay, zuaad, zuain
urdu_ipa_hindi_dict_end[u'\u0698'] = [u'\u0292']   # 38 yay

def loadHindiDictionary():
    #opening the file for reading UTF-8 data
    hindi_file = codecs.open('platts_hindi_dictionary.txt', encoding='utf-8')
    for line in hindi_file:
        line = line.replace(u'\u0964','')
        phrase = line.strip()
        hindi_word_dict[phrase] = ''
    hindi_file.close()

def updated_list_of_words(line):
    word_list=line.split()
    updated_word_list=[]
    for word in word_list:
        wprd1 = word.replace('(', '').replace(')', '').replace('!', '').replace('.', '').replace(',', '')
        updated_word_list.append(wprd1)
    return updated_word_list




# given a single Urdu  word, it will create all possible representations in IPA
# using hindi_ipa_urdu_dict
# given a single Hindi IPA word, it will create all possible representations in Urdu
# using hindi_ipa_urdu_dict
def covertHindiIPAToHindiWords(hindi_ipa_list):

    combined_hindi_word_list=[]
    # in case there are more than one Hindi IPA representation, we are going to loop one by one
    for index in range(len(hindi_ipa_list)):
        hindi_word_list = []
        ipa_symbol_list = hindi_ipa_list[index].strip('#').split('#')
        # --------------------------------HANDLING THE FIRST ALPHABET SEPARATELY
        flag = True
        symbol = ipa_symbol_list[0]
        if symbol in ipa_hindi_dict_start and len(ipa_hindi_dict_start[symbol]) > 0:
            if len(ipa_hindi_dict_start[symbol]) > 1:
                if not hindi_word_list:

                    for i in range(len(ipa_hindi_dict_start[symbol])):
                        hindi_word_list.append(ipa_hindi_dict_start[symbol][i])
                else:

                    cartesian_product = itertools.product(hindi_word_list, ipa_hindi_dict_start[symbol])
                    hindi_word_list[:] = []
                    for value in cartesian_product:
                        hindi_word_list.append(value[0] + value[1])
            else:
                if not hindi_word_list:

                    hindi_word_list.append(ipa_hindi_dict_start[symbol][0])
                    flag = False

                if flag == True:

                    for index_1 in range(len(hindi_word_list)):
                        hindi_word_list[index_1] += ipa_hindi_dict_start[symbol][0]
        else:
            print 'Start: Symbol is not in the dictionary'

        flag = True
        # --------------------------------HANDLING THE MIDDLE ALPHABETs SEPARATELY
        for symbol in ipa_symbol_list[1:]:
            if(not symbol):
                continue
            if symbol in ipa_hindi_dict and len(ipa_hindi_dict[symbol]) > 0:
                if len(ipa_hindi_dict[symbol]) > 1:

                    if not hindi_word_list:
                        for i in range(len(ipa_hindi_dict[symbol])):
                            hindi_word_list.append(ipa_hindi_dict[symbol][i])
                    else:

                        cartesian_product = itertools.product(hindi_word_list, ipa_hindi_dict[symbol])
                        hindi_word_list[:] = []
                        for value in (cartesian_product):
                            hindi_word_list.append(value[0] + value[1])
                else:
                    if not hindi_word_list:
                        hindi_word_list.append(ipa_hindi_dict[symbol][0])
                        flag = False

                    if flag == True:
                        for index_2 in range(len(hindi_word_list)):
                            hindi_word_list[index_2] += ipa_hindi_dict[symbol][0]
            else:
                print 'Middle: Symbol is not in the dictionary',repr(symbol)

        for word in hindi_word_list:
            combined_hindi_word_list.append(word)

    return combined_hindi_word_list




def covertUrduWordToHindiIPA(urdu_word_list):
    #extra characters to be added as urdu has missing diactrical marks
    extra_char_for_first = [u'\u0061',u'\u026A',u'\u028A','']
    unfoundSymbol=""
    # this will store the all the urdu representation of the input hindi ipa word
    hindi_ipa_list = []
    ipa_symbol_list_1=[]
    # in case there are more than one Hindi IPA representation, we are going to loop one by one
    for index in range(len(urdu_word_list)):
        ipa_symbol_list = urdu_word_list[index].strip('#').split('#')
        ipa_symbol_list_1.append(ipa_symbol_list[0])
    idx = 0
    n = 3
    newflag=True

    for j in range(n,0,-1):
        combined_char =  ''.join(ipa_symbol_list_1[0:j])

        flag = True
        symbol = combined_char
        unfoundSymbol=symbol
        if symbol in urdu_ipa_hindi_dict_start and len(urdu_ipa_hindi_dict_start[symbol]) > 0:
            newflag=False

            if len(urdu_ipa_hindi_dict_start[symbol]) > 1:
                if not hindi_ipa_list:
                    for i in range(len(urdu_ipa_hindi_dict_start[symbol])):
                        for ch in extra_char_for_first:
                            hindi_ipa_list.append("#" + urdu_ipa_hindi_dict_start[symbol][i] + "#" + ch)
                else:
                    cartesian_product = itertools.product(hindi_ipa_list, urdu_ipa_hindi_dict_start[symbol])
                    hindi_ipa_list[:] = []
                    for value in cartesian_product:
                        hindi_ipa_list.append(value[0] + "#" + value[1])
            else:
                if not hindi_ipa_list:
                    for ch in extra_char_for_first:
                        hindi_ipa_list.append("#" + urdu_ipa_hindi_dict_start[symbol][0] + "#" + ch)
                    flag = False

                if flag == True:
                    for index in range(len(hindi_ipa_list)):
                        hindi_ipa_list[index] += "#" + urdu_ipa_hindi_dict_start[symbol][0]

            idx = len(combined_char)
            break

    if newflag == True:
        print 'Start: Combined symbol not found in dict', repr(unfoundSymbol)

    flag = True
    newflag = True

    idx_m = idx
    list_iter = iter(ipa_symbol_list_1[idx:-1])
    # --------------------------------HANDLING THE MIDDLE ALPHABETs SEPARATELY
    for s in list_iter:
        n = 3

        for j in range(n, 0, -1):
            combined_char = ''.join(ipa_symbol_list_1[idx_m: idx_m+j])
            symbol = combined_char
            unfoundSymbol=symbol
            if symbol in urdu_ipa_hindi_dict_middle and len(urdu_ipa_hindi_dict_middle[symbol]) > 0:
                newflag=False
                idx_m = idx_m + len(combined_char)
                if idx_m>=len(ipa_symbol_list_1):
                    j=len(ipa_symbol_list_1)-idx_m-1
                for k in range(0,j-1):
                    next(list_iter)
                if len(urdu_ipa_hindi_dict_middle[symbol]) > 1:
                    if not hindi_ipa_list:
                        for i in range(len(urdu_ipa_hindi_dict_middle[symbol])):
                            hindi_ipa_list.append("#" + urdu_ipa_hindi_dict_middle[symbol][i])
                    else:
                        cartesian_product = itertools.product(hindi_ipa_list, urdu_ipa_hindi_dict_middle[symbol])
                        hindi_ipa_list[:] = []
                        for value in cartesian_product:
                            hindi_ipa_list.append(value[0] +"#" +  value[1])
                else:
                    if not hindi_ipa_list:
                        hindi_ipa_list.append("#" + urdu_ipa_hindi_dict_middle[symbol][0])
                        flag = False

                    if flag == True:
                        for index in range(len(hindi_ipa_list)):
                            hindi_ipa_list[index] += "#" + urdu_ipa_hindi_dict_middle[symbol][0]

                break
        if newflag == True:
            print 'Middle: Combined symbol not found in dict',repr(unfoundSymbol)
    # --------------------------------HANDLING THE LAST ALPHABET SEPARATELY

    flag = True
    newflag=True
    symbol = ipa_symbol_list_1[-1]
    unfoundSymbol=symbol
    if symbol in urdu_ipa_hindi_dict_end and len(urdu_ipa_hindi_dict_end[symbol]) > 0:
        newflag=False
        if len(urdu_ipa_hindi_dict_end[symbol]) > 1:
            if not hindi_ipa_list:
                for i in range(len(urdu_ipa_hindi_dict_end[symbol])):
                    hindi_ipa_list.append("#" + urdu_ipa_hindi_dict_end[symbol][i])
            else:
                cartesian_product = itertools.product(hindi_ipa_list, urdu_ipa_hindi_dict_end[symbol])
                hindi_ipa_list[:] = []
                for value in cartesian_product:
                    hindi_ipa_list.append(value[0] + "#" + value[1])
        else:
            if not hindi_ipa_list:
                hindi_ipa_list.append("#" + urdu_ipa_hindi_dict_end[symbol][0])
                flag = False

            if flag == True:
                for index in range(len(hindi_ipa_list)):
                    hindi_ipa_list[index] += "#" + urdu_ipa_hindi_dict_end[symbol][0]

    if newflag == True:
        print 'End: Combined symbol not found in dict', repr(unfoundSymbol)

    return hindi_ipa_list




def main():
    line_number = 1
    loadHindiDictionary()

    total_words = 0
    correct_words = 0
    wrong_words = 0
    unique_correct = 0
    urdu_file = codecs.open('urdu_standardized.txt', encoding='utf-8')
    hindi_file = codecs.open('hindi_1.txt', encoding='utf-8')
    output_file = codecs.open("output1.txt", "w", "utf-8")
    for urdu_line, hindi_line in zip(urdu_file,hindi_file):
        urdu_line = urdu_line.replace('(', ' ').replace(')', '').replace('!', ' ').replace('.', ' ')
        hindi_line = hindi_line.replace('(', ' ').replace(')', ' ').replace('!', '').replace('.', ' ').replace(u'\u0964','').replace('?', '')
        urdu_words = updated_list_of_words(urdu_line)
        hindi_words = updated_list_of_words(hindi_line)
        urdu_words = filter(None,(urdu_words))
        output_file.write(str(line_number) + '. ')
        for urdu_word in urdu_words:
            hindi_ipa_list = covertUrduWordToHindiIPA(urdu_word)
            hindi_word_list = covertHindiIPAToHindiWords(hindi_ipa_list)
            hindi_word_list = list(set(hindi_word_list))

            #this code integrates this code with ngram system.-------------------------------------

            if (len(hindi_word_list) > 3):
                temp_file = codecs.open("temp.txt", "w", "utf-8")
                for word in hindi_word_list:

                    for character in word:
                        temp_file.write(character + ' ')

                    temp_file.write('\n')

                temp_file.close()
                # print urdu_word_list
                # test files
                # /home/sami/Desktop/NLP_Project/bin/i686-m64
                batcmd = "/home/sami/Desktop/NLP_Project/bin/i686-m64/ngram -lm ngram_model.txt -ppl temp.txt -debug 2 | grep -o 'ppl= [0-9]*[.][0-9]*'"
                result = subprocess.check_output(batcmd, shell=True)
                result = result.strip().split()
                prob = [float(i) for i in result[1::2]]
                del prob[-1]
                prob_array = np.array(prob)
                # print 'Prob Array', prob_array
                index_list = list(prob_array.argsort()[:1])
                # print index_list
                # print len(urdu_word_list)
                small_word_list = []
                for value in index_list:
                    small_word_list.append(hindi_word_list[value])

                hindi_word_list = small_word_list
                # print urdu_word_list


            # end-------------------------------------

            flag = False
            for word in hindi_word_list:

                if (word in hindi_word_dict):
                    if(word in hindi_words):
                        output_file.write(word + ',')
                        flag = True
                        if word not in unique_word_dict:
                            unique_word_dict[word] = ''
                            unique_correct += 1

            if flag == False:
                wrong_words += 1
                output_file.write('Not found Start: ')
                for word in hindi_word_list:
                    output_file.write(word + ',')
                output_file.write('Not found End')
            else:
                correct_words += 1
            total_words += 1
        output_file.write('\n')
        line_number += 1
    output_file.close()
    urdu_file.close()
    hindi_file.close()
    print 'Total Words: ', total_words
    print 'Correct Words: ', correct_words
    print 'Wrong Words: ', wrong_words
    print 'Unique Correct Words', unique_correct
    print 'Percentage Correct: (Non-Unique)', float(correct_words) / total_words, '%'
    print 'Percentage Correct: (Unique)', float(correct_words) / (correct_words + wrong_words), '%'


main()


