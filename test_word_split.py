import codecs
import verParsingList as pd

def read_data():
    file = codecs.open('hindi_test.txt', encoding='utf-8')
    count = 0
    
    for line in file:
        word_list = pd.updated_list_of_words(line)
        print word_list
#         word_list = line.split(" ")
#         
#         count += 1
#         for word in word_list:
#             word = remove_punctuation_marks(word.strip())
#             updated_word = pd.pre_process_verbs(word)
#             if len(updated_word) > 0:
#                 continue
#             else:
#                 updated_word_2 = pd.pre_process_pronouns(word)
# #                 if len(updated_word_2) > 0:
# #                     print(line)
# #                     print(updated_word_2)
 
# def remove_punctuation_marks(word):
#    
#     if word.strip().endswith(punctuation_marks):
#         word = word[:-1]
#     return word
           
read_data()
