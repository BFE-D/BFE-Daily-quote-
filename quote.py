#!/usr/bin/env python3
import json
from pathlib import Path
import sys
import random
quote = []
try:
 var1 = sys.argv[1]
except:
 print("Usage: \nquote.py LANGUAGE \n \nCurrently supported languages: \nEnglish (100%) \nSpanish (50%) \nFrench (7%) \nPolish (3%)")
 exit()
f = open("lang/Bfed_" + var1 + ".json")
data = json.load(f)
for i in data:
    quote.append(str(data[i]))
print(quote[random.randint(0, len(quote))].replace("[LINEBREAK]", "\n").replace("[QUOTES]", "\""))
f.close()

