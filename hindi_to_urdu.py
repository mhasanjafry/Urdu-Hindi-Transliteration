#jahan jahan ddaal aa raha hai wahan rray bhi daal do

#any alphabet + hallant + same alphabet = alphabet shad
#get all hay characters, check before and after hallant. If alphabet + alphabet ha, write alphabet ha
#for handling the hallant issue, we need this
from itertools import izip as zip, count
from collections import defaultdict 
#needed for reading unicode files
import codecs
#needed for extracting the start of the line
import re
import itertools
import verParsingList as vpl
import subprocess
import numpy as np

#making dictionaries global so don't have to pass around
hindi_ipa_urdu_dict = dict()
urdu_ipa_dict = dict()
ipa_urdu_dict = dict()
hindi_ipa_dict = dict()
urdu_word_dict = dict()
urdu_phrase_dict = dict()
hindi_ipa_urdu_dict_start = dict()
hindi_ipa_urdu_dict_middle = dict()
hindi_ipa_urdu_dict_end = dict()
hallant_dict = dict()
unique_word_dict = dict()
#-------------------------------------------------------------HALLANT DICTIONARY--------------------------------------------------------------------------
hallant_dict[u'\u006B'] = [u'\u006B',u'\u02B0']	# kiyaaf
hallant_dict[u'\u0261'] = [u'\u0261',u'\u0324'] # gaaf

hallant_dict[u'\u0074\u0361\u0283'] = [u'\u0074\u0361\u0283',u'\u0074\u0361\u0283\u02B0'] # chay
hallant_dict[u'\u0064\u0361\u0292'] = [u'\u0064\u0361\u0292',u'\u0064\u0361\u0292\u0324'] # jeem
hallant_dict[u'\u0288'] = [u'\u0288',u'\u0288\u02B0'] # ttay
hallant_dict[u'\u0256'] = [u'\u0256',u'\u0256\u0324'] # ddaal
hallant_dict[u'\u0074\u032A'] = [u'\u0074\u032A',u'\u0074\u032A\u02B0'] # tay
hallant_dict[u'\u0064'] = [u'\u0064',u'\u0064\u0324'] # daal
hallant_dict[u'\u0070'] = [u'\u0070',u'\u0070\u02B0'] # pay
hallant_dict[u'\u0062'] = [u'\u0062',u'\u0062\u0324'] # bay
hallant_dict[u'\u027D'] = [u'\u027D',u'\u027D\u0324'] # rray
hallant_dict[u'\u006E'] = [u'\u006E'] #noon
hallant_dict[u'\u006D'] = [u'\u006D'] #meem
hallant_dict[u'\u0072'] = [u'\u0072']  # ray
hallant_dict[u'\u006C'] = [u'\u006C']  # laam
hallant_dict[u'\u028B'] = [u'\u028B']  # wow
hallant_dict[u'\u0283'] = [u'\u0283']  # sheen
hallant_dict[u'\u0282'] = [u'\u0282']  # sheen
hallant_dict[u'\u0073'] = [u'\u0073']  # 32 seen, say, suaad
hallant_dict[u'\u0266'] = [u'\u0266']  # 33 hay or gol hay
hallant_dict[u'\u0071'] = [u'\u0071']  # 34 kaaf or kiyaaf
hallant_dict[u'\u0078'] = [u'\u0078']  # 35 khay
hallant_dict[u'\u0263'] = [u'\u0263']  # 36 ghain
hallant_dict[u'\u007A'] = [u'\u007A']  # 37 zaal, zay, zuaad, zuain
hallant_dict[u'\u0292'] = [u'\u0292']  # 38 yay
hallant_dict[u'\u0066'] = [u'\u0066']  # 41 fay
#-------------------------------------------------HINDI IPA TO URDU ALPHABET START DICTIONARY-------------------------------------------------------------
hindi_ipa_urdu_dict_start[u'\u094D'] = [] #replacing hallant with no symbol, handled in code
hindi_ipa_urdu_dict_start[u'\u0651'] = [u'\u0651'] #replacing shad with shad, handled in code
#--right table
hindi_ipa_urdu_dict_start[u'\u0259'] = [u'\u0627\u064E',u'\u0639'] #1 alif or aain
hindi_ipa_urdu_dict_start[u'\u0061'] = [u'\u0622', u'\u0639']  # 2 rule if in the start alif mad aa else alif or aain
hindi_ipa_urdu_dict_start[u'\u026A'] = [u'\u0627\u0650']  # 3 if in the start put alif zair, if in the middle put hamza choti yay
#hindi_ipa_urdu_dict_start[u'\u0069'] = [u'\u0627\u0650\uFBFE']  # 4 beginning alif zair yay, middle zair yay, end zair choti yay
hindi_ipa_urdu_dict_start[u'\u0069'] = [u'\u0627\u0650\u06CC']  # 4 beginning alif zair yay, middle zair yay, end zair choti yay
hindi_ipa_urdu_dict_start[u'\u028A'] = [u'\u0627\u064F']  # 5 rule: beginning alif paish
hindi_ipa_urdu_dict_start[u'\u0075'] = [u'\u0627\u0648',u'\u0627\u064F',u'\u0627\u0624']  # 6 rule: beginning alif wow or alif paish
hindi_ipa_urdu_dict_start[u'\u090B'] = [u'\0631']  # 7 hindi character rhi ...no ipa ...directly mapping characters
#hindi_ipa_urdu_dict_start[u'\u0065'] = [u'\u0627\uFBFE']  # 8  beginning alif yay, middle yay, end bari yay
hindi_ipa_urdu_dict_start[u'\u0065'] = [u'\u0627\u06CC']  # 8  beginning alif yay, middle yay, end bari yay
#hindi_ipa_urdu_dict_start[u'\u025B'] = [u'\u0627\u064E\uFBFE']  # 9 beginning alif zabar yay, middle yay, end bari yay
hindi_ipa_urdu_dict_start[u'\u025B'] = [u'\u0627\u064E\u06CC']  # 9 beginning alif zabar yay, middle yay, end bari yay
hindi_ipa_urdu_dict_start[u'\u006F'] = [u'\u0627\u0648',u'\u0627\u0624']  # 10 rule: beginning alif wow else wow
hindi_ipa_urdu_dict_start[u'\u0254'] = [u'\u0627\u064E\u0648',u'\u0627\u064E\u0624']  # 11 rule: beginning alif zabar wow
hindi_ipa_urdu_dict_start[u'\u0303'] = [u'\u0646']  # 12 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_start[u'\u014B'] = [u'\u0646']  # 13 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_start[u'\u0272'] = [u'\u0646']  # 13 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_start[u'\u0273'] = [u'\u0646']  # 13 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_start[u'\u006E'] = [u'\u0646']  # 13 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_start[u'\u006D'] = [u'\u0646']  # 13 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_start[u'\u0303'] = [u'\u0646']  # 13 rule: start or middle noon, end noon ghunna 


#--left table
hindi_ipa_urdu_dict_start[u'\u006B'] = [u'\u06A9',u'\u0642'] #1 kiyaaf or kaaf
hindi_ipa_urdu_dict_start[u'\u02B0'] = [u'\u06A9\u06BE',u'\u06A9\u06C1',u'\u062E']  # 2 kiyaaf doochasmi hey or kiyaaf gol hey
hindi_ipa_urdu_dict_start[u'\u0261'] = [u'\u06AF', u'\u063A']  # 3 gaaf, ghain (Ghain Added by Sami after empirical testing)
hindi_ipa_urdu_dict_start[u'\u0324'] = [u'\u06AF\u06BE', u'\u06AF\u06C1', u'\u063A\u06BE', u'\u063A\u06C1']  # 4 gaaf doochasmi hey or gaaf gol hey or ghain doochasmi hey or ghain gol hey

hindi_ipa_urdu_dict_start[u'\u0074\u0361\u0283'] = [u'\u0686']  # 6 chay
hindi_ipa_urdu_dict_start[u'\u0074\u0361\u0283\u02B0'] = [u'\u0686\u06BE',u'\u0686\u06C1']  # 7 chay doochasmi hey or chay gol hey
hindi_ipa_urdu_dict_start[u'\u0064\u0361\u0292'] = [u'\u062C',u'\u0632']  # 8 jeem
hindi_ipa_urdu_dict_start[u'\u0064\u0361\u0292\u0324'] = [u'\u062C\u06BE',u'\u062C\u06C1']  # 9 jeem doochasmi hey or jeem gol hey

hindi_ipa_urdu_dict_start[u'\u0288'] = [u'\u0679']  # 11 ttay
hindi_ipa_urdu_dict_start[u'\u0288\u02B0'] = [u'\u0679\u06BE', u'\u0679\u06C1']  # 12 ttay doochasmi hey or ttay gol hey
hindi_ipa_urdu_dict_start[u'\u0256'] = [u'\u0688',u'\u0691']  # 13 ddaal or rray
hindi_ipa_urdu_dict_start[u'\u0256\u0324'] = [u'\u0688\u06BE',u'\u0688\u06C1',u'\u0691\u06BE',u'\u0691\u06C1']  # 14 ddaal doochasmi hey or ddaal gol hey, with rray too


hindi_ipa_urdu_dict_start[u'\u0074\u032A'] = [u'\u062a',u'\u0637']  # 16 tay or #tuain
hindi_ipa_urdu_dict_start[u'\u0074\u032A\u02B0'] = [u'\u062a\u06BE',u'\u062a\u06C1',u'\u0637\u06BE',u'\u0637\u06C1']  # 17 tay doochasmi hey or tay gol hey
hindi_ipa_urdu_dict_start[u'\u0064'] = [u'\u062F']  # 18 daal
hindi_ipa_urdu_dict_start[u'\u0064\u0324'] = [u'\u062F\u06BE',u'\u062F\u06C1']  # 19 daal doochasmi hey or daal gol hey
hindi_ipa_urdu_dict_start[u'\u006E'] = [u'\u0646']  # 20 rule: start or middle noon, end noon ghunna

hindi_ipa_urdu_dict_start[u'\u0070'] = [u'\u067e']  # 21 pay
#hindi_ipa_urdu_dict_end[u'\u0070\u02B0'] = [u'\u067e\u06BE',u'\u067e\u06C1']  # 22 pay doochasmi hey or pay gol hey 
hindi_ipa_urdu_dict_start[u'\u0070\u02B0'] = [u'\u0641'] # 22 fay changed here by Sami
hindi_ipa_urdu_dict_start[u'\u0062'] = [u'\u0628']  # 23 bay
hindi_ipa_urdu_dict_start[u'\u0062\u0324'] = [u'\u0628\u06BE',u'\u0628\u06C1']  # 24 bay doochasmi hey or bay gol hey
hindi_ipa_urdu_dict_start[u'\u006D'] = [u'\u0645']  # 25 meem

hindi_ipa_urdu_dict_start[u'\u006A'] = [u'\u06CC']  # 26 rule: if in the start, yay
hindi_ipa_urdu_dict_start[u'\u0072'] = [u'\u0631']  # 27 ray
hindi_ipa_urdu_dict_start[u'\u006C'] = [u'\u0644']  # 28 laam
hindi_ipa_urdu_dict_start[u'\u028B'] = [u'\u0648']  # 29 wow
hindi_ipa_urdu_dict_start[u'\u0283'] = [u'\u0634']  # 30 sheen

hindi_ipa_urdu_dict_start[u'\u0282'] = [u'\u0634']  # 31 sheen
hindi_ipa_urdu_dict_start[u'\u0073'] = [u'\u0633',u'\u062B',u'\u0635']  # 32 seen, say, suaad
hindi_ipa_urdu_dict_start[u'\u0266'] = [u'\u062D',u'\u06C1']  # 33 hay or gol hay
hindi_ipa_urdu_dict_start[u'\u0071'] = [u'\u0642',u'\u06A9']  # 34 kaaf or kiyaaf
hindi_ipa_urdu_dict_start[u'\u0078'] = [u'\u062E']  # 35 khay

hindi_ipa_urdu_dict_start[u'\u0263'] = [u'\u063A']  # 36 ghain
hindi_ipa_urdu_dict_start[u'\u007A'] = [u'\u0630',u'\u0632',u'\u0636',u'\u0638']  # 37 zaal, zay, zuaad, zuain
hindi_ipa_urdu_dict_start[u'\u0292'] = [u'\u0698']  # 38 yay
hindi_ipa_urdu_dict_start[u'\u027D'] = [u'\u0691']  # 39 rray
hindi_ipa_urdu_dict_start[u'\u027D\u0324'] = [u'\u0691\u06BE',u'\u0691\u06C1']  # 40 rray doochasmi hey or rray gol hey
hindi_ipa_urdu_dict_start[u'\u0066'] = [u'\u0641']  # 41 fay

#-------------------------------------------------HINDI IPA TO URDU ALPHABET MIDDLE DICTIONARY-------------------------------------------------------------
hindi_ipa_urdu_dict_middle[u'\u094D'] = [] #replacing hallant with no symbol, handled in code
hindi_ipa_urdu_dict_middle[u'\u0651'] = [u'\u0651'] #replacing shad with shad, handled in code

#--right table
hindi_ipa_urdu_dict_middle[u'\u0259'] = [u'\u064E'] #1 alif
hindi_ipa_urdu_dict_middle[u'\u0061'] = [u'\u0627',u'\u0622',u'\u0670']  # 2 if in the start alif mad aa, if in the middle, alif, alif mad aa, khari zabar
#hindi_ipa_urdu_dict_middle[u'\u026A'] = [u'\u0621\uFBFF']  # 3 this is the original rule if in the middle put hamza choti yay Changed by Sami. Reason below
hindi_ipa_urdu_dict_middle[u'\u026A'] = [u'\u0626',u'\u0650'] # 3 earlier hamza choti yay were two characters, now using single character that represents the same thing. Also can be zair
#hindi_ipa_urdu_dict_middle[u'\u0069'] = [u'\u0650\uFBFF']  # 4 middle zair yay
hindi_ipa_urdu_dict_middle[u'\u0069'] = [u'\u0650\u06CC']  # 4 middle zair yay
hindi_ipa_urdu_dict_middle[u'\u028A'] = [u'\u0648',u'\u064F']  # 5 rule: middle paish
hindi_ipa_urdu_dict_middle[u'\u0075'] = [u'\u0648',u'\u064F',u'\u0624']  # 6 middle wow or paish
hindi_ipa_urdu_dict_middle[u'\u090B'] = [u'\0631']  # 7 hindi character rhi ...no ipa ...directly mapping characters
#hindi_ipa_urdu_dict_middle[u'\u0065'] = [u'\uFBFF']  # 8  beginning alif yay, middle yay, end bari yay
hindi_ipa_urdu_dict_middle[u'\u0065'] = [u'\u06CC']  # 8  beginning alif yay, middle yay, end bari yay
#hindi_ipa_urdu_dict_middle[u'\u025B'] = [u'\u064E\uFBFF']  # 9 beginning alif yay, middle zabar yay, zabar bari yay
hindi_ipa_urdu_dict_middle[u'\u025B'] = [u'\u064E\u06CC']  # 9 beginning alif yay, middle zabar yay, zabar bari yay
hindi_ipa_urdu_dict_middle[u'\u006F'] = [u'\u0648',u'\u0624',u'\u06C1']  # 10 rule: beginning alif wow else wow, added gol hey to adjust for the word "woh"
hindi_ipa_urdu_dict_middle[u'\u0254'] = [u'\u064E\u0648',u'\u064E\u0624']  # 11 rule: middle zabar wow
hindi_ipa_urdu_dict_middle[u'\u0303'] = [u'\u0646']  # 12 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_middle[u'\u014B'] = [u'\u0646']  # 13 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_middle[u'\u0272'] = [u'\u0646']  # 13 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_middle[u'\u0273'] = [u'\u0646']  # 13 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_middle[u'\u006E'] = [u'\u0646']  # 13 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_middle[u'\u006D'] = [u'\u0646']  # 13 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_middle[u'\u0303'] = [u'\u0646']  # 13 rule: start or middle noon, end noon ghunna 


#--left table
hindi_ipa_urdu_dict_middle[u'\u006B'] = [u'\u06A9',u'\u0642'] #1 kiyaaf or kaaf
hindi_ipa_urdu_dict_middle[u'\u02B0'] = [u'\u06A9\u06BE',u'\u06A9\u06C1',u'\u062E']  # 2 kiyaaf doochasmi hey or kiyaaf gol hey
hindi_ipa_urdu_dict_middle[u'\u0261'] = [u'\u06AF', u'\u063A']  # 3 gaaf, ghain (Ghain Added by Sami after empirical testing)
hindi_ipa_urdu_dict_middle[u'\u0324'] = [u'\u06AF\u06BE', u'\u06AF\u06C1', u'\u063A\u06BE', u'\u063A\u06C1']  # 4 gaaf doochasmi hey or gaaf gol hey or ghain doochasmi hey or ghain gol hey

hindi_ipa_urdu_dict_middle[u'\u0074\u0361\u0283'] = [u'\u0686']  # 6 chay
hindi_ipa_urdu_dict_middle[u'\u0074\u0361\u0283\u02B0'] = [u'\u0686\u06BE',u'\u0686\u06C1']  # 7 chay doochasmi hey or chay gol hey
hindi_ipa_urdu_dict_middle[u'\u0064\u0361\u0292'] = [u'\u062C',u'\u0632']  # 8 jeem
hindi_ipa_urdu_dict_middle[u'\u0064\u0361\u0292\u0324'] = [u'\u062C\u06BE',u'\u062C\u06C1']  # 9 jeem doochasmi hey or jeem gol hey

hindi_ipa_urdu_dict_middle[u'\u0288'] = [u'\u0679']  # 11 rule: ttay 
hindi_ipa_urdu_dict_middle[u'\u0288\u02B0'] = [u'\u0679\u06BE', u'\u0679\u06C1']  # 12 ttay doochasmi hey or ttay gol hey
hindi_ipa_urdu_dict_middle[u'\u0256'] = [u'\u0688',u'\u0691']  # 13 ddaal or rray
hindi_ipa_urdu_dict_middle[u'\u0256\u0324'] = [u'\u0688\u06BE',u'\u0688\u06C1',u'\u0691\u06BE',u'\u0691\u06C1']  # 14 ddaal doochasmi hey or ddaal gol hey with rray too


hindi_ipa_urdu_dict_middle[u'\u0074\u032A'] = [u'\u062a',u'\u0637']  # 16 tay or #tuain
hindi_ipa_urdu_dict_middle[u'\u0074\u032A\u02B0'] = [u'\u062a\u06BE',u'\u062a\u06C1']  # 17 tay doochasmi hey or tay gol hey
hindi_ipa_urdu_dict_middle[u'\u0064'] = [u'\u062F']  # 18 daal
hindi_ipa_urdu_dict_middle[u'\u0064\u0324'] = [u'\u062F\u06BE',u'\u062F\u06C1']  # 19 daal doochasmi hey or daal gol hey
hindi_ipa_urdu_dict_middle[u'\u006E'] = [u'\u0646',u'\u06BA']  # 20 rule: start or middle noon, end noon ghunna

hindi_ipa_urdu_dict_middle[u'\u0070'] = [u'\u067e']  # 21 pay
#hindi_ipa_urdu_dict_end[u'\u0070\u02B0'] = [u'\u067e\u06BE',u'\u067e\u06C1']  # 22 pay doochasmi hey or pay gol hey 
hindi_ipa_urdu_dict_middle[u'\u0070\u02B0'] = [u'\u0641'] # 22  fay changed here by Sami
hindi_ipa_urdu_dict_middle[u'\u0062'] = [u'\u0628']  # 23 bay
hindi_ipa_urdu_dict_middle[u'\u0062\u0324'] = [u'\u0628\u06BE',u'\u0628\u06C1']  # 24 bay doochasmi hey or bay gol hey
hindi_ipa_urdu_dict_middle[u'\u006D'] = [u'\u0645']  # 25 meem

#hindi_ipa_urdu_dict_middle[u'\u006A'] = [u'\uFBFF']  # 26 rule: if in centre, yay if in end, bari yay
hindi_ipa_urdu_dict_middle[u'\u006A'] = [u'\u06CC']  # 26 rule: if in centre, yay if in end, bari yay
hindi_ipa_urdu_dict_middle[u'\u0072'] = [u'\u0631']  # 27 ray
hindi_ipa_urdu_dict_middle[u'\u006C'] = [u'\u0644']  # 28 laam
hindi_ipa_urdu_dict_middle[u'\u028B'] = [u'\u0648',u'\u0624']  # 29 wow
hindi_ipa_urdu_dict_middle[u'\u0283'] = [u'\u0634']  # 30 sheen

hindi_ipa_urdu_dict_middle[u'\u0282'] = [u'\u0634']  # 31 sheen
hindi_ipa_urdu_dict_middle[u'\u0073'] = [u'\u0633',u'\u062B',u'\u0635']  # 32 seen, say, suaad
hindi_ipa_urdu_dict_middle[u'\u0266'] = [u'\u062D',u'\u06C1']  # 33 hay or gol hay
hindi_ipa_urdu_dict_middle[u'\u0071'] = [u'\u0642',u'\u06A9']  # 34 kaaf or kiyaaf
hindi_ipa_urdu_dict_middle[u'\u0078'] = [u'\u062E']  # 35 khay

hindi_ipa_urdu_dict_middle[u'\u0263'] = [u'\u063A']  # 36 ghain
hindi_ipa_urdu_dict_middle[u'\u007A'] = [u'\u0630',u'\u0632',u'\u0636',u'\u0638']  # 37 zaal, zay, zuaad, zuain
hindi_ipa_urdu_dict_middle[u'\u0292'] = [u'\u0698']  # 38 yay
hindi_ipa_urdu_dict_middle[u'\u027D'] = [u'\u0691']  # 39 rray
hindi_ipa_urdu_dict_middle[u'\u027D\u0324'] = [u'\u0691\u06BE',u'\u0691\u06C1']  # 40 rray doochasmi hey or rray gol hey
hindi_ipa_urdu_dict_middle[u'\u0066'] = [u'\u0641']  # 41 fay

#-------------------------------------------------HINDI IPA TO URDU ALPHABET END DICTIONARY-------------------------------------------------------------
#All words with hay sounds in left table, if in hindi same character appears with hallant, to remove the character and write mad instead

hindi_ipa_urdu_dict_end[u'\u094D'] = [] #replacing hallant with no symbol, handled in code
hindi_ipa_urdu_dict_end[u'\u0651'] = [u'\u0651'] #replacing shad with shad, handled in code

#--right table
hindi_ipa_urdu_dict_end[u'\u0259'] = [u'\u0627'] #1 alif
hindi_ipa_urdu_dict_end[u'\u0061'] = [u'\u0627',u'\u06CC\u0670',u'\u06C1']  # 2 rule if in the end, alif or choti yay khari zabar as in aalaa
hindi_ipa_urdu_dict_end[u'\u026A'] = [u'\u0650']  # 3 putting as zair in the end
hindi_ipa_urdu_dict_end[u'\u0069'] = [u'\u0650\u06CC']  # 4 zair choti yay
hindi_ipa_urdu_dict_end[u'\u028A'] = [u'\u06BA']  # 5 rule: never appears at the end
hindi_ipa_urdu_dict_end[u'\u0075'] = [u'\u0648', u'\u064F',u'\u0624']  # 6 ending wow or paish
hindi_ipa_urdu_dict_end[u'\u090B'] = [u'\0631']  # 7 hindi character rhi ...no ipa ...directly mapping characters
hindi_ipa_urdu_dict_end[u'\u0065'] = [u'\u06D2']  # 8  beginning alif yay, middle yay, end bari yay
hindi_ipa_urdu_dict_end[u'\u025B'] = [u'\u064E\u06D2']  # 9 beginning alif yay, middle yay, end zabar bari yay
hindi_ipa_urdu_dict_end[u'\u006F'] = [u'\u0648',u'\u0624',u'\u06C1']  # 10 rule: beginning alif wow else wow, also added gol hey to adjust for the word "woh"
hindi_ipa_urdu_dict_end[u'\u0254'] = [u'\u064E\u0648',u'\u064E\u0624']  # 11 rule: end zabar wow
hindi_ipa_urdu_dict_end[u'\u0303'] = [u'\u06BA']  # 12 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_end[u'\u014B'] = [u'\u06BA']  # 13 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_end[u'\u0272'] = [u'\u06BA']  # 13 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_end[u'\u0273'] = [u'\u06BA']  # 13 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_end[u'\u006E'] = [u'\u06BA']  # 13 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_end[u'\u006D'] = [u'\u06BA']  # 13 rule: start or middle noon, end noon ghunna 
hindi_ipa_urdu_dict_end[u'\u0303'] = [u'\u06BA']  # 13 rule: start or middle noon, end noon ghunna 


#--left table
hindi_ipa_urdu_dict_end[u'\u006B'] = [u'\u06A9',u'\u0642'] #1 kiyaaf or kaaf
hindi_ipa_urdu_dict_end[u'\u02B0'] = [u'\u06A9\u06BE',u'\u06A9\u06C1',u'\u062E']  # 2 kiyaaf doochasmi hey or kiyaaf gol hey
hindi_ipa_urdu_dict_end[u'\u0261'] = [u'\u06AF', u'\u063A']  # 3 gaaf, ghain (Ghain Added by Sami after empirical testing)
hindi_ipa_urdu_dict_end[u'\u0324'] = [u'\u06AF\u06BE', u'\u06AF\u06C1', u'\u063A\u06BE', u'\u063A\u06C1']  # 4 gaaf doochasmi hey or gaaf gol hey or ghain doochasmi hey or ghain gol hey

hindi_ipa_urdu_dict_end[u'\u0074\u0361\u0283'] = [u'\u0686']  # 6 chay
hindi_ipa_urdu_dict_end[u'\u0074\u0361\u0283\u02B0'] = [u'\u0686\u06BE',u'\u0686\u06C1']  # 7 chay doochasmi hey or chay gol hey
hindi_ipa_urdu_dict_end[u'\u0064\u0361\u0292'] = [u'\u062C',u'\u0632']  # 8 jeem
hindi_ipa_urdu_dict_end[u'\u0064\u0361\u0292\u0324'] = [u'\u062C\u06BE',u'\u062C\u06C1']  # 9 jeem doochasmi hey or jeem gol hey

hindi_ipa_urdu_dict_end[u'\u0288'] = [u'\u0679']  # 11 rule: ttay 
hindi_ipa_urdu_dict_end[u'\u0288\u02B0'] = [u'\u0679\u06BE', u'\u0679\u06C1']  # 12 ttay doochasmi hey or ttay gol hey
hindi_ipa_urdu_dict_end[u'\u0256'] = [u'\u0688', u'\u0691']  # 13 ddaal or rray
hindi_ipa_urdu_dict_end[u'\u0256\u0324'] = [u'\u0688\u06BE',u'\u0688\u06C1',u'\u0691\u06BE',u'\u0691\u06C1']  # 14 ddaal doochasmi hey or ddaal gol hey, with rray too


hindi_ipa_urdu_dict_end[u'\u0074\u032A'] = [u'\u062a',u'\u0637']  # 16 tay or #tuain
hindi_ipa_urdu_dict_end[u'\u0074\u032A\u02B0'] = [u'\u062a\u06BE',u'\u062a\u06C1']  # 17 tay doochasmi hey or tay gol hey
hindi_ipa_urdu_dict_end[u'\u0064'] = [u'\u062F']  # 18 daal
hindi_ipa_urdu_dict_end[u'\u0064\u0324'] = [u'\u062F\u06BE',u'\u062F\u06C1']  # 19 daal doochasmi hey or daal gol hey
hindi_ipa_urdu_dict_end[u'\u006E'] = [u'\u0646',u'\u06BA']  # 20 rule: start or middle noon, end noon ghunna

hindi_ipa_urdu_dict_end[u'\u0070'] = [u'\u067e']  # 21 pay
#hindi_ipa_urdu_dict_end[u'\u0070\u02B0'] = [u'\u067e\u06BE',u'\u067e\u06C1']  # 22 pay doochasmi hey or pay gol hey 
hindi_ipa_urdu_dict_end[u'\u0070\u02B0'] = [u'\u0641'] # 22 changed to fay by Sami
hindi_ipa_urdu_dict_end[u'\u0062'] = [u'\u0628']  # 23 bay
hindi_ipa_urdu_dict_end[u'\u0062\u0324'] = [u'\u0628\u06BE',u'\u0628\u06C1']  # 24 bay doochasmi hey or bay gol hey
hindi_ipa_urdu_dict_end[u'\u006D'] = [u'\u0645']  # 25 meem

hindi_ipa_urdu_dict_end[u'\u006A'] = [u'\u06D2']  # 26 rule: if in centre, yay if in end, bari yay
hindi_ipa_urdu_dict_end[u'\u0072'] = [u'\u0631']  # 27 ray
hindi_ipa_urdu_dict_end[u'\u006C'] = [u'\u0644']  # 28 laam
hindi_ipa_urdu_dict_end[u'\u028B'] = [u'\u0648',u'\u0624']  # 29 wow
hindi_ipa_urdu_dict_end[u'\u0283'] = [u'\u0634']  # 30 sheen

hindi_ipa_urdu_dict_end[u'\u0282'] = [u'\u0634']  # 31 sheen
hindi_ipa_urdu_dict_end[u'\u0073'] = [u'\u0633',u'\u062B',u'\u0635']  # 32 seen, say, suaad
hindi_ipa_urdu_dict_end[u'\u0266'] = [u'\u062D',u'\u06C1']  # 33 hay or gol hay
hindi_ipa_urdu_dict_end[u'\u0071'] = [u'\u0642',u'\u06A9']  # 34 kaaf or kiyaaf
hindi_ipa_urdu_dict_end[u'\u0078'] = [u'\u062E']  # 35 khay

hindi_ipa_urdu_dict_end[u'\u0263'] = [u'\u063A']  # 36 ghain
hindi_ipa_urdu_dict_end[u'\u007A'] = [u'\u0630',u'\u0632',u'\u0636',u'\u0638']  # 37 zaal, zay, zuaad, zuain
hindi_ipa_urdu_dict_end[u'\u0292'] = [u'\u0698']  # 38 yay
hindi_ipa_urdu_dict_end[u'\u027D'] = [u'\u0691']  # 39 rray
hindi_ipa_urdu_dict_end[u'\u027D\u0324'] = [u'\u0691\u06BE',u'\u0691\u06C1']  # 40 rray doochasmi hey or rray gol hey
hindi_ipa_urdu_dict_end[u'\u0066'] = [u'\u0641']  # 41 fay

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


#---------------------------HINDI ALPHABETS TO IPA CONVERSION DICTIONARY---------------------------------------------------------------------------------

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

hindi_ipa_dict[u'\u0905'] = [u'\u0259']  # DEVANAGARI LETTER  A
hindi_ipa_dict[u'\u0906'] = [u'\u0061']  # DEVANAGARI LETTER AA
hindi_ipa_dict[u'\u0907'] = [u'\u026A']  # DEVANAGARI LETTER I
hindi_ipa_dict[u'\u0908'] = [u'\u0069']  # DEVANAGARI LETTER II
hindi_ipa_dict[u'\u0909'] = [u'\u028A']  # DEVANAGARI LETTER U
hindi_ipa_dict[u'\u090A'] = [u'\u0075']  # DEVANAGARI LETTER UU
hindi_ipa_dict[u'\u090B'] = [u'\u090B']  # DEVANAGARI LETTER VOCALIC R (could not find)
hindi_ipa_dict[u'\u090F'] = [u'\u0065']  # DEVANAGARI LETTER E
hindi_ipa_dict[u'\u0910'] = [u'\u025B']  # DEVANAGARI LETTER AI
hindi_ipa_dict[u'\u0913'] = [u'\u006F']  # DEVANAGARI LETTER O
hindi_ipa_dict[u'\u0914'] = [u'\u0254']  # DEVANAGARI LETTER AU
hindi_ipa_dict[u'\u0901'] = [u'\u0303']  # DEVANAGARI SIGN CANDRABINDU
#hindi_ipa_dict[u'\u0902'] = [u'\u014B', u'\u0272', u'\u0273', u'\u006E', u'\u006D', u'\u0303']  # DEVANAGARI SIGN ANUSVARA
hindi_ipa_dict[u'\u0902'] = [u'\u006E']  # DEVANAGARI SIGN ANUSVARA, adjusted with Noon here
hindi_ipa_dict[u'\u0903'] = [u'\u0266']  # DEVANAGARI SIGN VISARGA
hindi_ipa_dict[u'\u0945'] = [u'\u0065']  # DEVANAGARI VOWEL SIGN CANDRA E (check)

# Independent vowels
# Consonants
hindi_ipa_dict[u'\u0915'] = [u'\u006B']  # DEVANAGARI LETTER  KA
hindi_ipa_dict[u'\u0916'] = [u'\u02B0']  # DEVANAGARI LETTER KHA
hindi_ipa_dict[u'\u0917'] = [u'\u0261']  # DEVANAGARI LETTER GA
hindi_ipa_dict[u'\u0918'] = [u'\u0324']  # DEVANAGARI LETTER GHA
hindi_ipa_dict[u'\u0919'] = [u'\u014B']  # DEVANAGARI LETTER NGA
hindi_ipa_dict[u'\u091A'] = [u'\u0074\u0361\u0283']  # DEVANAGARI LETTER CA
hindi_ipa_dict[u'\u091B'] = [u'\u0074\u0361\u0283\u02B0']  # DEVANAGARI LETTER CHA
hindi_ipa_dict[u'\u091C'] = [u'\u0064\u0361\u0292']  # DEVANAGARI LETTER JA
hindi_ipa_dict[u'\u091D'] = [u'\u0064\u0361\u0292\u0324']  # DEVANAGARI LETTER JHA
hindi_ipa_dict[u'\u091E'] = [u'\u0272']  # DEVANAGARI LETTER NYA
hindi_ipa_dict[u'\u091F'] = [u'\u0288']  # DEVANAGARI SIGN TTA
hindi_ipa_dict[u'\u0920'] = [u'\u0288\u02B0']  # DEVANAGARI SIGN TTHA
hindi_ipa_dict[u'\u0921'] = [u'\u0256']  # DEVANAGARI SIGN DDA
hindi_ipa_dict[u'\u0922'] = [u'\u0256\u0324']  # DEVANAGARI LETTER DDHA
hindi_ipa_dict[u'\u0923'] = [u'\u0273']  # DEVANAGARI LETTER NNA
hindi_ipa_dict[u'\u0924'] = [u'\u0074\u032A']  # DEVANAGARI LETTER TA
hindi_ipa_dict[u'\u0925'] = [u'\u0074\u032A\u02B0']  # DEVANAGARI LETTER THA
hindi_ipa_dict[u'\u0926'] = [u'\u0064']  # DEVANAGARI LETTER DA
hindi_ipa_dict[u'\u0927'] = [u'\u0064\u0324']  # DEVANAGARI LETTER DHA
hindi_ipa_dict[u'\u0928'] = [u'\u006E']  # DEVANAGARI LETTER NA
hindi_ipa_dict[u'\u092A'] = [u'\u0070']  # DEVANAGARI LETTER PA
hindi_ipa_dict[u'\u092B'] = [u'\u0070\u02B0']  # DEVANAGARI LETTER PHA
hindi_ipa_dict[u'\u092C'] = [u'\u0062']  # DEVANAGARI LETTER BA
hindi_ipa_dict[u'\u092D'] = [u'\u0062\u0324']  # DEVANAGARI LETTER BHA
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
hindi_ipa_dict[u'\u094D'] = [u'\u094D']  # DEVANAGARI  SIGN Virama (hallant)

#Various signs
hindi_ipa_dict[u'\u093C'] = [] #DEVANAGARI SIGN NUKTA

#Abbreviation sign
hindi_ipa_dict[u'\u0970'] = []  # DEVANAGARI ABBREVIATION SIGN(intended for Devanagari-specific abbreviation)

#---------------------------END OF DICTIONARIES---------------------------------------------------------------------------------
#this function will handle the Hallant issue before further processing
def handleHallant(hindi_ipa_list):
	returned_list = []
	#in case there are more than one Hindi IPA representation, we are going to loop one by one
	for index in range(len(hindi_ipa_list)):
		#splitting the ipa symbols based on # symbol
		ipa_symbol_list = hindi_ipa_list[index].strip('#').split('#')
		#checking if hallant is present in the list
		hallant_index_list = [i for i, j in zip(count(), ipa_symbol_list) if j == u'\u094D']
		#if hallant is not present
		if not hallant_index_list:
			#no need to modify the input string
			returned_list.append(hindi_ipa_list[index])
		else:
			#hallant is present
			#print 'Hallant was found', hallant_index_list
			#may be multiple hallants in one word, so looping one by one
			for hallant_index in sorted(hallant_index_list, reverse=True):
			#for hallant_index in hallant_index_list:
				#what to do if hallant is the first character in the word
				if hallant_index == 0:
					print 'Hallant is at starting index!!! What to do???'
				#what to do if hallant is the last character in the word
				elif hallant_index == (len(ipa_symbol_list) - 1):
					print 'Hallant is at ending index!!! What to do???'
				else:
					flag = True
					#getting the alphabet before the hallant symbol
					before_hallant = ipa_symbol_list[hallant_index - 1]
					#getting the alphabet after the hallant symbol
					after_hallant = ipa_symbol_list[hallant_index + 1]
					#if before character is present as key of dictionary	
					if before_hallant in hallant_dict:
						#if after character is present as value in dictionary
						if after_hallant in hallant_dict[before_hallant]:
							#delete hallant and the character before it
							del ipa_symbol_list[(hallant_index - 1):(hallant_index + 1)]
							#add the shad character after the repeated character
							ipa_symbol_list.insert(hallant_index,u'\u0651')
							#join all the broken tokens with the # symbol for correct formatting in the future
							ipa_string = '#'.join(ipa_symbol_list)
							#add this modified string to the returned list	
							returned_list.append(ipa_string)
							flag = False

					if flag == True:
						returned_list.append(hindi_ipa_list[index])
	return returned_list
#given a single Hindi IPA word, it will create all possible representations in Urdu
#using hindi_ipa_urdu_dict
def covertHindiIPAToUrduWords(hindi_ipa_list):
	hindi_ipa_list = handleHallant(hindi_ipa_list)
	#this will store the all the urdu representation of the input hindi ipa word 
	combined_urdu_word_list=[]
	
	#in case there are more than one Hindi IPA representation, we are going to loop one by one
	for index in range(len(hindi_ipa_list)):
		urdu_word_list = []
		
		ipa_symbol_list = hindi_ipa_list[index].strip('#').split('#')
		#--------------------------------HANDLING THE FIRST ALPHABET SEPARATELY
		flag = True		
		symbol = ipa_symbol_list[0]
		if symbol in hindi_ipa_urdu_dict_start and len(hindi_ipa_urdu_dict_start[symbol]) > 0:
			if len(hindi_ipa_urdu_dict_start[symbol]) > 1:
				if not urdu_word_list:
					for i in range(len(hindi_ipa_urdu_dict_start[symbol])):
						urdu_word_list.append(hindi_ipa_urdu_dict_start[symbol][i])
				else:
					cartesian_product = itertools.product(urdu_word_list,hindi_ipa_urdu_dict_start[symbol])
					urdu_word_list[:] = []
					for value in cartesian_product:
						urdu_word_list.append(value[0]+value[1])
			else:
				if not urdu_word_list:
					urdu_word_list.append(hindi_ipa_urdu_dict_start[symbol][0])
					flag = False

				if flag == True:
					for index in range(len(urdu_word_list)):
						urdu_word_list[index] += hindi_ipa_urdu_dict_start[symbol][0] 
		else:
			print 'Start: Symbol is not in the dictionary'

		flag = True
		#--------------------------------HANDLING THE MIDDLE ALPHABETs SEPARATELY
		for symbol in ipa_symbol_list[1:-1]:
			if symbol in hindi_ipa_urdu_dict_middle and len(hindi_ipa_urdu_dict_middle[symbol]) > 0:
					
				if len(hindi_ipa_urdu_dict_middle[symbol]) > 1:
					if not urdu_word_list:
						for i in range(len(hindi_ipa_urdu_dict_middle[symbol])):
							urdu_word_list.append(hindi_ipa_urdu_dict_middle[symbol][i])
					else:
						cartesian_product = itertools.product(urdu_word_list,hindi_ipa_urdu_dict_middle[symbol])
						urdu_word_list[:] = []
						for value in cartesian_product:
							urdu_word_list.append(value[0]+value[1])
				else:
					if not urdu_word_list:
						urdu_word_list.append(hindi_ipa_urdu_dict_middle[symbol][0])
						flag = False

					if flag == True:
						for index in range(len(urdu_word_list)):
							urdu_word_list[index] += hindi_ipa_urdu_dict_middle[symbol][0] 
			else:
				print 'Middle: Symbol is not in the dictionary'
		#--------------------------------HANDLING THE LAST ALPHABET SEPARATELY
		
		flag = True
		
		symbol = ipa_symbol_list[-1]		
		if symbol in hindi_ipa_urdu_dict_end and len(hindi_ipa_urdu_dict_end[symbol]) > 0:
			if len(hindi_ipa_urdu_dict_end[symbol]) > 1:
				if not urdu_word_list:
					for i in range(len(hindi_ipa_urdu_dict_end[symbol])):
						urdu_word_list.append(hindi_ipa_urdu_dict_end[symbol][i])
				else:
					cartesian_product = itertools.product(urdu_word_list,hindi_ipa_urdu_dict_end[symbol])
					urdu_word_list[:] = []
					for value in cartesian_product:
						urdu_word_list.append(value[0]+value[1])
			else:
				if not urdu_word_list:
					urdu_word_list.append(hindi_ipa_urdu_dict_end[symbol][0])
					flag = False

				if flag == True:
					for index in range(len(urdu_word_list)):
						urdu_word_list[index] += hindi_ipa_urdu_dict_end[symbol][0] 
		else:
			print 'End: Symbol is not in the dictionary'

	for word in urdu_word_list:
		combined_urdu_word_list.append(word)

	return combined_urdu_word_list	
#the goal of this function is to convert hindi words into equivalent IPA sounds
#input is a single hindi word
#output is list of ipa representation of this hindi word
#In case of DEVANAGARI SIGN ANUSVARA, we will have more than one element
#else just a single IPA string 
def covertHindiWordToIPA(hindi_word):
	
	#this will store the ipa of hindi word
	hindi_ipa = []
	#looping over alphabet by alphabet
	for alphabet in list(hindi_word):
		#print 'Alphabet code', repr(alphabet)
		#this means that we have not entered the alphabet in the dictionary
		if alphabet not in hindi_ipa_dict:
			print 'The alphabet ' + alphabet + ' is not present in the dictionary' 
			continue
		#this means that we have not put in the mapping yet
		if len(hindi_ipa_dict[alphabet]) == 0:
			print 'There is no mapping for the alphabet ' + alphabet + ' in the dictionary'
			continue
		elif len(hindi_ipa_dict[alphabet]) > 1:
			if not hindi_ipa:
				for i in range(len(hindi_ipa_dict[alphabet])):
					hindi_ipa.append('#'+hindi_ipa_dict[alphabet][i])
			else:
				cartesian_product = itertools.product(hindi_ipa,hindi_ipa_dict[alphabet])
				hindi_ipa[:] = []
				for value in cartesian_product:
					hindi_ipa.append(value[0]+'#'+value[1])
		else:
			if not hindi_ipa:
				hindi_ipa.append('#'+hindi_ipa_dict[alphabet][0])
				continue

			for index in range(len(hindi_ipa)):
				hindi_ipa[index] += '#'+hindi_ipa_dict[alphabet][0] 
	return hindi_ipa

#this function will load all the urdu words from Urdu dictionary
def loadUrduDictionary():
	#opening the file for reading UTF-8 data
	urdu_file = codecs.open('wordlist.txt', encoding='utf-8')

	for line in urdu_file:
		phrase = line.strip()
		words = line.strip().split()
		if len(words) == 1:
			urdu_word_dict[phrase] = ''
		else:
			urdu_phrase_dict[phrase] = ''
			for word in words:
				urdu_word_dict[word] = ''	
	urdu_file.close()

def removeDiatricalMarks(word):
	#print repr(word)
	diatrical_marks = u'\u064E\u0650\u064F\u0651'
	translate_table = dict((ord(char), None) for char in diatrical_marks)
	word = word.translate(translate_table)
	return word
def main():
	loadUrduDictionary()


	#print len(urdu_word_dict)
	total_words = 0
	correct_words = 0
	wrong_words = 0
	unique_correct = 0
	#opening the file for reading UTF-8 data
	urdu_file = codecs.open('urdu_standardized.txt', encoding='utf-8')
	#urdu_file = codecs.open('test.google.hin.urd.txt', encoding='utf-8')
	line_number = 1
	hindi_file = codecs.open('hindi_1.txt', encoding='utf-8')
	output_file = codecs.open("output.txt", "w", "utf-8")
	#looping over line by line in both files simultaneously
	for urdu_line, hindi_line in zip(urdu_file, hindi_file):
	#for hindi_line in hindi_file:
		
		#removing useless characters from line
		hindi_line = hindi_line.replace('(', ' ').replace(')', ' ').replace('!',' ').replace('.',' ').replace('?',' ')
		hindi_line = hindi_line.strip()
		urdu_line = urdu_line.replace('(', ' ').replace(')', ' ').replace('!',' ').replace('.',' ').replace('?',' ')
		urdu_line = urdu_line.strip()
		urdu_words = urdu_line.split()
		#splitting the hindi line based on space
		#hindi_words = hindi_line.split()
		hindi_words = vpl.updated_list_of_words(hindi_line)
		hindi_words = filter(None, hindi_words) # removing all emtpy strings
		#print 'After splitting we have ',len(hindi_words), ' words'
		output_file.write(str(line_number)+'. ')
		#print hindi_words
		for hindi_word in hindi_words:
				
			hindi_ipa_list = covertHindiWordToIPA(hindi_word)
			#print hindi_ipa_list
			urdu_word_list = covertHindiIPAToUrduWords(hindi_ipa_list)

			urdu_word_list = list(set(urdu_word_list))
			
			#print urdu_word_list
			if (len(urdu_word_list) > 3):
				temp_file = codecs.open("temp.txt", "w", "utf-8")
				for word in urdu_word_list:
					word = removeDiatricalMarks(word)
					for character in word:
						temp_file.write(character+' ')

					temp_file.write('\n')

				temp_file.close()
				#print urdu_word_list
				#test files
				batcmd = "/home/sami/Desktop/NLP_Project/bin/i686-m64/ngram -order 4 -lm ngram_urdu_4.txt -ppl temp.txt -debug 2 | grep -o 'ppl= [0-9]*[.][0-9]*'"
				#batcmd="/home/sami/Desktop/NLP_Project/bin/i686-m64/ngram -lm ngram_model.txt -ppl temp.txt -debug 2 | grep -o 'ppl= [0-9]*[.][0-9]*'"
					
				result = subprocess.check_output(batcmd, shell=True)
				result = result.strip().split()
				prob = [float(i) for i in result[1::2]]
				del prob[-1]
				prob_array = np.array(prob)
				#print 'Prob Array', prob_array				
				index_list = list(prob_array.argsort()[:1])
				#print index_list
				#print len(urdu_word_list)
				small_word_list = []
				for value in index_list:
					small_word_list.append(urdu_word_list[value])

				urdu_word_list = small_word_list
				#print urdu_word_list
			
			flag = False
			for word in urdu_word_list:
				
				word = removeDiatricalMarks(word)
				#print word
				#output_file.write(word+',')
				if (word in urdu_word_dict) or (word in urdu_phrase_dict):
					if word in urdu_words:
						output_file.write(word+',')
						flag = True
						if word not in unique_word_dict:
							unique_word_dict[word] = ''
							unique_correct += 1
				
			if flag == False:
				wrong_words += 1
				output_file.write('Not found Start: ')
				for word in urdu_word_list:
					word = removeDiatricalMarks(word)
				#print urdu_word_list
					output_file.write(word+',')
				output_file.write('Not found End')
			else:
				correct_words += 1
			
			total_words += 1
		output_file.write('\n')
		
		line_number += 1		
		
	output_file.close()
	hindi_file.close()
	print 'Total Words: ', total_words
	print 'Correct Words: ', correct_words
	print 'Wrong Words: ', wrong_words
	#print 'Unique Correct Words', unique_correct
	print 'Percentage Correct: ', (float(correct_words)/total_words)*100, '%'
	#print 'Percentage Correct: (Unique)', float(correct_words)/(unique_correct), '%'
main()
