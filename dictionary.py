

import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def dictionary(dict):
    dict = dict.lower()
    if dict in data:
        return data[dict]
    elif len(get_close_matches(dict , data.keys())) > 0:
        x = input('Did you mean to say %s instead? enter y if yes or n if no: ' % get_close_matches(dict , data.keys())[0])
        if x == 'y':
            return data[get_close_matches(dict , data.keys())[0]]
        elif x == 'n':
            return 'Sorry Dear , We didnot understand a word you said.'

    else:
        return 'Sorry Dear, Please double-check your word, as the word you specified doesnot exist.'


word = input("Enter word: ")

console = dictionary(word)

if type(console) == list:
    for item in console:
        print(item)
else:
    print(console)

