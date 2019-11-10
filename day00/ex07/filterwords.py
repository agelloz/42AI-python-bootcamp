import sys
import string
import re

if (len(sys.argv) != 3 or sys.argv[1].isdigit() is True or sys.argv[2].isdigit() is False):
    print("ERROR")
    exit()
punctuation_re = re.compile('[' + string.punctuation + ']')
text = punctuation_re.sub('', sys.argv[1])
wlist = text.split()
try:
    n = int(sys.argv[2])
except ValueError:
    print("ERROR")
    exit()
to_delete = []
for word in wlist:
    if (len(word) < n):
        to_delete.append(word)
for i in to_delete:
    wlist.remove(i)
print(wlist)
