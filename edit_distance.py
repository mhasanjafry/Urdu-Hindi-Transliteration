import codecs
import math
def updated_list_of_words(line):
    word_list=line.split()
    #print line
    updated_word_list=[]
    for word in word_list:
        updated_word_list.append(word)
    #print  "return updated_word_list",updated_word_list
    return updated_word_list


def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in xrange(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    for j in xrange(-1, lenstr2 + 1):
        d[(-1, j)] = j + 1

    for i in xrange(lenstr1):
        for j in xrange(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,  # deletion
                d[(i, j - 1)] + 1,  # insertion
                d[(i - 1, j - 1)] + cost,  # substitution
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)  # transposition

    return d[lenstr1 - 1, lenstr2 - 1]

def main():
    hindi_file_1 = codecs.open('urdu_standardized.txt', encoding='utf-8')
    hindi_file_2 = codecs.open('output111.txt', encoding='utf-8')
    edit_distance = []

    for hindi_line_1,hindi_line_2 in zip(hindi_file_1,hindi_file_2) :
        hindi_line_1 = hindi_line_1.replace('(', ' ').replace(')', ' ').replace('!', ' ').replace('.', ' ')
        hindi_words_1 = updated_list_of_words(hindi_line_1)

        hindi_line_2 = hindi_line_2.replace('(', ' ').replace(')', ' ').replace('!', ' ').replace('.', ' ')
        hindi_words_2 = updated_list_of_words(hindi_line_2)

        if(len(hindi_words_1) == len(hindi_words_2)):
            for word1, word2 in zip(hindi_words_1,hindi_words_2):
                a = damerau_levenshtein_distance(word1, word2)
                edit_distance.append(a)
    print "average edit distance for urdu", float(sum(edit_distance))/float(len(edit_distance))

main()

