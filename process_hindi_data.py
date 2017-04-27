# -*- coding: utf-8 -*-
import codecs

hindi_character_mapping = dict()
hindi_character_mapping[u'\u090c'] =u''
hindi_character_mapping[u'\u090d'] =u'\u090f'
hindi_character_mapping[u'\u090e'] =u'\u0910'
hindi_character_mapping[u'\u0911'] =u'\u0906'
hindi_character_mapping[u'\u0912'] =u'\u0913'
hindi_character_mapping[u'\u0933'] =u'\u0932'
hindi_character_mapping[u'\u0934'] =u'\u0932'
hindi_character_mapping[u'\u093d'] =u''
hindi_character_mapping[u' \u0946'] =u'\u0947'
hindi_character_mapping[u'\u0944'] =u''
hindi_character_mapping[u'\u097f'] =u'\u092c'
hindi_character_mapping[u'\u0950'] =u'\u0913\u092e'
hindi_character_mapping[u'\u097b'] =u'\u0930\u094d'
hindi_character_mapping[u'\u0967'] =u''
hindi_character_mapping[u'\u0968'] =u''
hindi_character_mapping[u'\u0969'] =u''
hindi_character_mapping[u'\u096a'] =u''
hindi_character_mapping[u'\u096b'] =u''
hindi_character_mapping[u'\u096c'] =u''
hindi_character_mapping[u'\u096d'] =u''
hindi_character_mapping[u'\u096e'] =u''
hindi_character_mapping[u'\u096f'] =u''
hindi_character_mapping[u'1'] =u''
hindi_character_mapping[u'2'] =u''
hindi_character_mapping[u'3'] =u''
hindi_character_mapping[u'4'] =u''
hindi_character_mapping[u'5'] =u''
hindi_character_mapping[u'6'] =u''
hindi_character_mapping[u'7'] =u''
hindi_character_mapping[u'8'] =u''
hindi_character_mapping[u'9'] =u''
hindi_character_mapping[u'0'] =u''
hindi_character_mapping[u'*'] =u''
hindi_character_mapping[u'.'] =u''
hindi_character_mapping[u'-'] =u''
hindi_character_mapping[u','] =u''
hindi_character_mapping[u'.'] =u''
hindi_character_mapping[u':'] =u''
hindi_character_mapping[u';'] =u''
hindi_character_mapping[u"'"] =u''
hindi_character_mapping[u'@'] =u''
hindi_character_mapping[u'"'] =u''
hindi_character_mapping[u'A'] =u''
hindi_character_mapping[u'B'] =u''
hindi_character_mapping[u'C'] =u''
hindi_character_mapping[u'D'] =u''
hindi_character_mapping[u'E'] =u''
hindi_character_mapping[u'F'] =u''
hindi_character_mapping[u'G'] =u''
hindi_character_mapping[u'H'] =u''
hindi_character_mapping[u'I'] =u''
hindi_character_mapping[u'J'] =u''
hindi_character_mapping[u'K'] =u''
hindi_character_mapping[u'L'] =u''
hindi_character_mapping[u'M'] =u''
hindi_character_mapping[u'N'] =u''
hindi_character_mapping[u'O'] =u''
hindi_character_mapping[u'P'] =u''
hindi_character_mapping[u'Q'] =u''
hindi_character_mapping[u'R'] =u''
hindi_character_mapping[u'S'] =u''
hindi_character_mapping[u'T'] =u''
hindi_character_mapping[u'U'] =u''
hindi_character_mapping[u'V'] =u''
hindi_character_mapping[u'W'] =u''
hindi_character_mapping[u'X'] =u''
hindi_character_mapping[u'Y'] =u''
hindi_character_mapping[u'Z'] =u''
hindi_character_mapping[u'a'] =u''
hindi_character_mapping[u'b'] =u''
hindi_character_mapping[u'c'] =u''
hindi_character_mapping[u'd'] =u''
hindi_character_mapping[u'e'] =u''
hindi_character_mapping[u'f'] =u''
hindi_character_mapping[u'g'] =u''
hindi_character_mapping[u'h'] =u''
hindi_character_mapping[u'i'] =u''
hindi_character_mapping[u'j'] =u''
hindi_character_mapping[u'k'] =u''
hindi_character_mapping[u'l'] =u''
hindi_character_mapping[u'm'] =u''
hindi_character_mapping[u'n'] =u''
hindi_character_mapping[u'o'] =u''
hindi_character_mapping[u'p'] =u''
hindi_character_mapping[u'q'] =u''
hindi_character_mapping[u'r'] =u''
hindi_character_mapping[u's'] =u''
hindi_character_mapping[u't'] =u''
hindi_character_mapping[u'u'] =u''
hindi_character_mapping[u'v'] =u''
hindi_character_mapping[u'w'] =u''
hindi_character_mapping[u'x'] =u''
hindi_character_mapping[u'y'] =u''
hindi_character_mapping[u'z'] =u''

hindi_full_stop = "।"



"""
    This utility standardised the data we retrieved from wordnet had a lot of 
    unstandardized data
    
    It had a lot of character from different languages like chinese, many other indian languages
    which are standardised by this method. some characters are replaces with similar sounding characters
    and others are removed from the file completely.
     
"""
def process_data():
    arr = []
    hindi_char_arr =["ऌ","ऍ", "ऎ", "ऑ", "ऒ", "ळ", "ऴ", "ऽ"," ॆ", "ॄ", "ॿ", "ॐ", "ॻ",",", ".", ".", "-", ":", ";", "'", "@", '"']
    hindi_num_arr = ["१","२","३","४","५","६","७","८","९"]
    hindi_num_rep_arr = ["","","","","","","","",""]
    eng_char_arr =["a","b", "c", "d", "e", "f", "g", "h"," i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    eng_cap_char_arr =["A","B", "C", "D", "E", "F", "G", "H"," I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    replace_hindi_char_arr =["","ए", "ऐ", "आ", "ओ", "ल", "ल", "","े", "", "ब", "ओम", "र्", "", "", "", "", "", "", "", "", ""]
    numbers_arr =["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "*"]
    numbers_arr_rep =["", "", "", "", "", "", "", "", "", "", ""]
    hindi_character_mapping = dict()
    for i in range(0,len(hindi_char_arr)):
        uni = hindi_char_arr[i].decode('utf-8')
        replace_uni = replace_hindi_char_arr[i].decode('utf-8')
        #print repr(uni), repr(replace_uni)
        print "hindi_character_mapping["+repr(uni)+"] =" +repr(replace_uni) 

def split_word_and_write_in_file(line, output_file, seperate):
    words = []
    if seperate:
        words = line.split(" ")
    else: words.append(line) 
    
    if len(words) > 1:
        print "words split length greater than 1" + words[0] + " : " + words[1]
    for word in words:
        for i in range(0, len(word)):
            output_file.write(word[i])
            output_file.write(" ")
        output_file.write('\n')   
        
        
def standardise_data():
    text_file = codecs.open('data/platts_dict/platts_hindi_updated.txt', encoding='utf-8')
    output_file = codecs.open("data/platts_dict/platts_hindi_updated_standardised.txt", "w", "utf-8")
    char_arr = read_non_hindi_characters()
    count = 0
    for file_line in text_file:
         
        lines_arr = file_line.split(hindi_full_stop.decode('utf-8'))
        if len(lines_arr) > 1:
            print "size of array is greater than 1"
        for line in lines_arr:
            count +=1
            for non_hindi_char in char_arr:
                line = line.replace(non_hindi_char, "")
            
            line = line.replace('(', ' ').replace(')', ' ').replace('!',' ').replace('.',' ')
            line = line.replace('[', ' ').replace(']', ' ')
            
            for key in hindi_character_mapping.keys():
                if key == u'\u097b':
                    if key in line:
                        line = replace_character_with_seq(key, hindi_character_mapping[key], line)
                else: line = line.replace(key, hindi_character_mapping[key])
            if len(line.strip()) > 0:
                line = " ".join(line.split())
                #line = line + hindi_full_stop.decode('utf-8')
                split_word_and_write_in_file(line, output_file, False)
    print count
                
"""
    This utility method replaces a character with a sequence of characters.
    Some data in this file had unicode issues like some sequence of unicodes were 
    replaced with some other language characters  
"""  
def replace_character_with_seq(key, value, line):
    words_arr = line.strip().split()
    updated_line = []
    for word in words_arr:
        if key in word:
            char_loc = word.index(key)
            updated_word = word[0:char_loc-1] + value + word[char_loc-1] + word[char_loc+1:]
            print updated_word
            updated_line.append(updated_word)
        else: updated_line.append(word)
        updated_line.append(" ")
    return ''.join(updated_line)+' '


"""
    This utility method is used for detecting language of a given character:
    Primarily recognizes if the character lies in the devnagari range.
"""
def detect_language(c):
    
    if u'\u0900' <= c <= u'\u097f':
        return True
    return False


"""
    This utility method find the unique list of characters lies in the devnagari range present in that file.
    also seperate out a list of unique non devnagri characters into another file.
"""
def unique_characters():
    
    text_file = codecs.open('/Users/arpita/Documents/Spring2017/NLP/Hindi_Urdu/web.hin.char.standardised.txt', encoding='utf-8')
    output_file = codecs.open('/Users/arpita/Documents/Spring2017/NLP/Hindi_Urdu/uniq_char_set.txt', "w", encoding='utf-8')
    non_hindi_output_file = codecs.open('/Users/arpita/Documents/Spring2017/NLP/Hindi_Urdu/non_hindi_uniq_char_set.txt', "w", encoding='utf-8')
    uniq_char_set = set([])
    uniq_unicode_char_set = set([])
    
    count = 0
    for file_line in text_file:
        words_arr = file_line.split()
        for word in words_arr:
            for alphabet in word:
                count +=1
                uniq_char_set.add(alphabet)
                uniq_unicode_char_set.add(alphabet)
        
    for c in uniq_unicode_char_set:
        if detect_language(c):
            output_file.write(c)
            output_file.write("\n")
        else:
            non_hindi_output_file.write(c)
            non_hindi_output_file.write("\n")        
    
def read_non_hindi_characters():
    text_file = codecs.open('/Users/arpita/Documents/Spring2017/NLP/Hindi_Urdu/non_hindi_uniq_char_set.txt', encoding='utf-8')
    non_hindi_chars = []
    for line in text_file:
        non_hindi_chars.append(line.strip())
    return non_hindi_chars
    
"""
    This method is used to cluster some characters together, for example half ka, is written as Ka + halanth 
    (two characters which actually is considered as 1 for people reading/ writing hindi). Such words are combined
    into one which then can be trained as one when passed to our models  
"""    
def group_letters():
    text_file = codecs.open('/Users/arpita/Documents/Spring2017/NLP/hindi_urdu_transliteration/data/standardised_wordnet_data/web.hin.char.standardised.txt', encoding='utf-8')
    output_file = codecs.open('/Users/arpita/Documents/Spring2017/NLP/Hindi_Urdu/web.hin.standardised.combined.txt', "w", encoding='utf-8')
    halanth = "्".decode('utf-8')
    for word in text_file:
        for i in range(0, len(word)):
            if word[i] != halanth:
                if (i+1)< len(word):
                    if word[i+1] == halanth:
                        output_file.write(word[i] + word[i+1])
                    else:   output_file.write(word[i])
                else:   output_file.write(word[i])
                output_file.write(" ")
        output_file.write("\n")


def average_word_length():
    text_file = codecs.open('/Users/arpita/Documents/Spring2017/NLP/hindi_urdu_transliteration/data/standardised_wordnet_data/web.hin.char.standardised.txt', encoding='utf-8')
    
    size = 0
    count = 0
    for line in text_file:
        size = size + len(line)
        count = count +1
    print size
    print count
    print (float(size)/float(count))

#average_word_length()                               
#standardise_data()    
#process_data()
group_letters()
#unique_characters()
