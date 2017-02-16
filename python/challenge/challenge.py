from string import maketrans   

import urllib
import re
# Required to call maketrans function.
 

value = 63579
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
val = urllib.urlopen(url+str(value))
found = re.findall("[0-9]+",val.read())
while len(found) > 0:
    
    print value
    val = urllib.urlopen(url+str(value))
    result = val.read()
    print result
    if len(re.findall("[0-9]+",result)) >0:
        value = re.findall("[0-9]+",result)[0]
    if value == str(16044):
        value = int(value)/2
    print url+str(value)

