import re
import codecs

def process_platt_dictionary():
    file = codecs.open("data/platts_dict/platts.txt", encoding='utf-8')
    processed_output_file = codecs.open("data/platts_dict/platts_h_u_a.txt","w", encoding='utf-8')
    processed_hindi_output_file = codecs.open("data/platts_dict/platts_hindi_updated.txt","w", encoding='utf-8')
    processed_urdu_output_file = codecs.open("data/platts_dict/platts_urdu_updated.txt","w", encoding='utf-8')
    count = 0
    print "Starting processing... "
    with codecs.open("data/platts_dict/platts_processed_dic.txt", "w", "utf-8-sig") as output_file:
        for line in file:
            result = re.search('<hw>(.*)</hw>', line)
            if result != None:
                output_file.write(result.group(1))
                output_file.write("\n")
                updated_string = process_hinidi_urdu_words(result.group(1))
                #process_hinidi_urdu_words_dataset(result.group(1), processed_hindi_output_file, processed_urdu_output_file)
                modify_hinidi_urdu_words_dataset(result.group(1), processed_hindi_output_file, processed_urdu_output_file)
                processed_output_file.write(updated_string)
                processed_output_file.write("\n")
                count += 1
        print count
    
def process_hinidi_urdu_words(line):
    result_urdu = re.search('<pa>(.*?)</pa>', line)
    result_hindi = re.search('<d>(.*?)</d>', line)
    result_i = re.search('<i>(.*?)</i>', line)
    
    updated_string = ''
    if result_hindi != None:
        updated_string += "H:" + result_hindi.group(1)
    if result_urdu != None:
        if updated_string != '':
            updated_string += ',    '
        updated_string += "U:" + result_urdu.group(1)
    if result_i != None:
        if updated_string != '':
            updated_string += ',    '
        updated_string += "R:" + result_i.group(1)    
    return updated_string

def process_hinidi_urdu_words_dataset(line, processed_hindi_output_file, processed_urdu_output_file):
    result_urdu = re.search('<pa>(.*?)</pa>', line)
    result_hindi = re.search('<d>(.*?)</d>', line)
    
    if (result_hindi != None) & (result_urdu != None):
        
        if((result_hindi.group(1) == "") or (result_hindi.group(1) == " ")):
            print "space found"
        else:
            processed_hindi_output_file.write(result_hindi.group(1))
            processed_hindi_output_file.write("\n")
            processed_urdu_output_file.write(result_urdu.group(1))
            processed_urdu_output_file.write("\n")
            

def modify_hinidi_urdu_words_dataset(line, processed_hindi_output_file, processed_urdu_output_file):
    result_urdu = re.search('<pa>(.*?)</pa>', line)
    result_hindi = re.search('<d>(.*?)</d>', line)
    
    if (result_hindi != None) & (result_urdu != None):
        
        
        
        if((result_hindi.group(1) == "") or (result_hindi.group(1) == " ")):
            print "space found"
        elif result_urdu.group(1).find(u"\u061f") > -1:
            print "question mark found" + result_urdu.group(1)
        else:
            updated_string = remove_characters_from_hindi(result_hindi)
            processed_hindi_output_file.write(updated_string)
            processed_hindi_output_file.write("\n")
            
            if result_urdu.group(1).find(u"\u067f") > -1:
                print "\ncheck locations ::"
                print result_hindi.group(1)
                print result_urdu.group(1)
                #print result_hindi.group(1)
                changed_urdu_string = find_location(result_urdu.group(1), result_hindi.group(1))
                print 'changed_urdu_string'
                print changed_urdu_string
            
                processed_urdu_output_file.write(changed_urdu_string)
                processed_urdu_output_file.write("\n")
            else:
                processed_urdu_output_file.write(result_urdu.group(1))
                processed_urdu_output_file.write("\n")
        

def remove_characters_from_hindi(result_hindi):
    
    updated_string = result_hindi.group(1)
    if updated_string.find(u"\u096e") > -1: 
        print result_hindi.group(1)
        updated_string = updated_string.replace(u"\u096e",'')
    return updated_string

def find_location(s, y):
    
    left_location_hindi = -1
    left_location_urdu = -1
    
    right_location_hindi = -1
    right_location_urdu = -1
    
    if (y.find(u"\u091f")==-1) or (y.find(u"\u0920")== -1): left_location_hindi = max(y.find(u"\u091f"), y.find(u"\u0920"))
    else: left_location_hindi = min(y.find(u"\u091f"), y.find(u"\u0920"))
    
    right_location_hindi = max(y.rfind(u"\u091f"), y.rfind(u"\u0920"))
    left_location_urdu = s.find(u"\u067f")
    right_location_urdu = s.rfind(u"\u067f")
    #= u"\u0679"    #= u"\u0679"
    if (left_location_hindi != -1) & (left_location_urdu != -1):
        if y[left_location_hindi] == u"\u091f": s = s.replace(u"\u067f",u"\u0679") 
        else:   s = s.replace(u"\u067f",u"\u062a")
    
    if (right_location_hindi != -1) & (right_location_urdu != -1):
        if y[right_location_hindi] == u"\u091f": s = s.replace(u"\u067f",u"\u0679") 
        else:   s = s.replace(u"\u067f",u"\u062a") 
             
#     print "changed s::"
#     print s
    return s
        
        
process_platt_dictionary()
