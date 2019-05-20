import sys
import os
import time

def remove_special(word):
	characters = ["\xe2\x80\x9d","\xe2\x80\x9c","?","(",")","!",".",",","\r","\n",";","*","_"]
	for character in characters:
		word = word.replace(character,"")

	return word.lower()


start_time = time.time()
try:
	filename = sys.argv[1]
except Exception:
	exit("No file args")

if not os.path.isfile(bigfile):
	print("file not exist")
else:
	bigfile = open(filename)
	print("reading file...")
end_time = time.time()
load_time = end_time - start_time

dic_word = {}
count = 0

start_time = time.time()
for line in bigfile:
	line = line.replace("--"," ")
	words = line.split(" ")
	for word in words:
		word = remove_special(word)
		dic_word[word] = dic_word.get(word,0)+1
		count += 1

end_time = time.time()
running_time = end_time - start_time

print("Dic Words: ",pal_dict)
print("Total Words:",count)
print("Total Unique Words:",len(pal_dict))
print("Loading Time: ",load_time)
print("Running Time: ",running_time)
