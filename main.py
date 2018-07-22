import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def dictionary(w):
	if w in data:
		return data[w]
	elif len(get_close_matches(w, data.keys()))>0:
		inp = input("Did you mean \"%s\" (y/n)?" % get_close_matches(w, data.keys())[0])
		if(inp=='y' or inp=='Y'):
			return data[get_close_matches(w, data.keys())[0]]
	else:
		return "Doesn't exist mate!"

word = input("Enter your word? ")
print(dictionary(word.lower()))