# First application from Udemy megacourse

import json
from difflib import get_close_matches 

data = json.load(open("data.json"))

def translate(word):
    if type(word) != str:
        word = str(word)

    if word in data:
        return data[word]
    elif word.title() in data: 
        return data[word.title()] # for proper nouns
    elif word.lower() in data:
        return data[word.lower()]
    elif word.upper() in data: 
        return data[word.upper()] # for acronyms
    elif len(get_close_matches(word, data.keys())) > 0:
        ans = raw_input("Did you mean {} instead? Y/N: ".format(get_close_matches(word, data.keys())[0]))
        if ans in ['yes', 'y']:
            word = get_close_matches(word, data.keys())[0]
            return data[word.lower()]
        elif ans in ['no', 'n']:
            return 'The word doesn\'t exist. Please double check it.'
        else:
            return "Sorry! Don\'t understand your entry."
    else:
        return 'The word doesn\'t exist. Please double check it!'

word = raw_input('Enter a word: ')

try:
    output = translate(word)
    if type(output) == list:
        for item in output:
            print item
    else:
        print output
except:
    print "Uh oh! Word not found."
