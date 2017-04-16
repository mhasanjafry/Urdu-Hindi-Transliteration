import codecs
verb_case_marker =[]
root_pronouns = []
pronouns_case_markers =[]
verb_case_marker_2 =[]
verb_mid_case_marker=[]
verb_mid_case_marker_2=[]
verb_mid_case_marker_3 = []
sample_pronoun= ''
sample_verb =''
punctuation_marks = []

def process_verb_list():
    file = codecs.open('data/verb_list/idxverb.txt', encoding='utf-8')
    hindi_verbs_list = []
    root_word_list = []
    for line in file:
            #this is for extracting the line numbers from the start, we can use them to match lines in Hindi
        if bool(line.strip()):
            updated_string = ""
            start_index = 0
            for i in range(0,len(line)):
                if ord(line[i])>255:
                    break
            updated_string = line[i:]
            space_index =  updated_string.find(' ')
            updated_string = updated_string[:space_index]
            underscore_index =  updated_string.find('_') 
            if underscore_index >= 0:root_word_list.append(updated_string[:underscore_index]) 
            else:   root_word_list.append(updated_string) 
            hindi_verbs_list.append(updated_string)
    write_root_verbs(root_word_list)        
    

def write_root_verbs(root_word_list):
    global verb_case_marker
    verbs_set = set()
    for word in root_word_list:
        if word.endswith(verb_case_marker):    verbs_set.add(word[:-2])
        else:   verbs_set.add(word)

    with codecs.open("data/verb_list/verbs_list", "w", "utf-8-sig") as output_file:
        for word in verbs_set:
            if word.strip():
                output_file.write(word)
                output_file.write("\n")
    
    print(verbs_set)

"""
    Check if the given word is a form of pronoun, if it is, then it is split into root form + case marker
    
"""
def pre_process_pronouns(word):
    global root_pronouns
    global pronouns_case_markers
    updated_pronoun = []
    if (word[:-2] in root_pronouns) or (word[:-3] in root_pronouns):
        if (word[:-2] in root_pronouns) :   
            if word[-2:] in pronouns_case_markers:
                updated_pronoun = [word[:-2], word[-2:]]
        elif word[-3:] in pronouns_case_markers:
            updated_pronoun = [word[:-3], word[-3:]]
    #print updated_pronoun
    return updated_pronoun
    
"""
    Check if the given word is a form of verb, if it is, then it is split into root form + case marker
    
"""
def get_verb_list():
    verb_file = codecs.open('data/verb_list/verbs_list', encoding="utf-8-sig")
    verb_list = []
    for line in verb_file:
        if line.strip():
            verb_list.append(line.strip())
    return verb_list



def pre_process_verbs(verb):
    global verb_list
    updated_verb = []
    global verb_case_marker_2
    global verb_mid_case_marker
#     print(verb) 
    #verbs_case_marker = tuple(verb_case_marker)
    if verb.endswith(verb_case_marker_2):
        root_verb = verb[:-2]
        if root_verb.endswith(verb_mid_case_marker):
            root_verb = process_mid_casemakers(root_verb)
        if root_verb in verb_list:
            updated_verb = [verb[:-2], verb[-2:]]
#     if not word_updted: updated_verb = [verb]
    #print(updated_verb)
    return updated_verb    

def process_mid_casemakers(root_verb):
    global verb_mid_case_marker_2
    global verb_mid_case_marker_3
    if root_verb.endswith(verb_mid_case_marker_3):
        root_verb = root_verb[:-1]
    elif root_verb.endswith(verb_mid_case_marker_2):
        root_verb = root_verb[:-2]
            
    return root_verb

def get_case_markers_from_file(filename):
    file = codecs.open(filename, encoding='utf-8')
    global punctuation_marks, sample_verb, sample_pronoun, verb_case_marker, root_pronouns, pronouns_case_markers, verb_case_marker_2, verb_mid_case_marker, verb_mid_case_marker_2, verb_mid_case_marker_3
    verb_case_marker = tuple(file.readline().strip().split(","))
    root_pronouns = tuple(file.readline().strip().split(","))
    pronouns_case_markers = tuple(file.readline().strip().split(","))
    verb_case_marker_2 = tuple(file.readline().strip().split(","))
    verb_mid_case_marker = tuple(file.readline().strip().split(","))
    verb_mid_case_marker_2 = tuple(file.readline().strip().split(","))
    verb_mid_case_marker_3 = tuple(file.readline().strip().split(","))
    sample_verb = file.readline()
    sample_pronoun = file.readline()
    punctuation_marks = tuple(file.readline().strip().split(","))

def remove_punctuation_marks(word):
    global punctuation_marks
    word = word.strip()
    if word.endswith(punctuation_marks):
        word = word[:-1]
    return word

def updated_list_of_words(line):
    word_list = line.split(" ")     
    
    updated_word_list = []
    for word in word_list:
        word = remove_punctuation_marks(word.strip())
        updated_word = pre_process_verbs(word)
        if len(updated_word) < 1:
            updated_word = pre_process_pronouns(word)
        
        if len(updated_word) < 1:
            updated_word_list.append(word)
        else:
            updated_word_list.extend(updated_word)
    return updated_word_list   
 
        
get_case_markers_from_file("data/verb_list/case_markers.txt")        
process_verb_list()
verb_list = get_verb_list()
#pre_process_verbs(sample_verb.strip())
#pre_process_pronouns(sample_pronoun)

                

