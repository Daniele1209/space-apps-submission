import spacy
import copy

def list_to_string(list):
    out_string = ''
    for item in list:
        out_string = out_string + str(item) + ' '
    return out_string

def convert_list(key_list):
    list_of_keys = []
    for key in key_list:
        list_of_keys.append(str(key))
    return list_of_keys

def clean_keys(key_list):
    # list_copy = copy.deepcopy(key_list)
    for key in key_list:
        if key in ['', '\n', '\t'] or key is None:
            key_list.remove(key)
        elif '\n' in key:
            key_list.remove(key)
        elif len(key) <= 3:
            key_list.remove(key)
        else:
            split_key = key.split(' ')
            for word in split_key:
                if len(word) <= 2:
                    key_list.remove(key)
                    break
    # for key in key_list:
    # print(key_list)
    return key_list

if __name__ == '__main__':
    nlp = spacy.load("Models/en_core_sci_lg-0.5.1/en_core_sci_lg/en_core_sci_lg-0.5.1")
    text = open('Data/TextFiles/19900018794.txt', 'r')
    file_cont = text.read()
    doc = nlp(file_cont)
    list_of_keys = convert_list(doc.ents)
    final_list = clean_keys(list_of_keys)

    string_input = list_to_string(final_list)
    sec_doc = nlp(string_input)

    print(sec_doc.ents)