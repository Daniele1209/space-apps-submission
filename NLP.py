import spacy
import copy
import os
from textblob import TextBlob
import csv


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
    for key in key_list.copy():
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


def correct_spelling(word):
    word = TextBlob(word)
    result = word.correct()
    return result


if __name__ == '__main__':
    entries = os.listdir('Data/TextFiles')
    nlp = spacy.load("Models/en_core_sci_lg-0.5.1/en_core_sci_lg/en_core_sci_lg-0.5.1")
    for file in entries:
        text = open('Data/TextFiles/' + file, 'r')
        file_cont = text.read()
        doc = nlp(file_cont)
        list_of_keys = convert_list(doc.ents)
        final_list = clean_keys(list_of_keys)
        # keep unique values
        final_list = list(set(final_list))
        with open('keywords.csv', 'a', newline='', encoding='utf-8') as keywords_file:
            writer = csv.writer(keywords_file)
            for item in final_list:
                item = correct_spelling(item)
                writer.writerow([file.replace('txt', 'pdf'), item])

