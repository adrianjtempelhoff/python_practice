#!/usr/bin/python
import sys
from random import randint

a=""
if len(sys.argv) == 2: 
  a=sys.argv[1]
else:
  a=sys.stdin.read()

#
#a=str(a).replace("10", "")
#a=str(a).replace("\n", "")
#a=str(a).split(" ")

#print a


oa=[
"alpha","bravo","charlie","delta","echo",
"foxtrot","golf","hotel","india","juliet",
"kilo","lima","mike","november","oscar","papa",
"quebec","romeo","sierra","tango","uniform","victor",
"whiskey","xray","yankee","zulu",
]


aa=[
"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
]

#print len(oa)
#print len(aa)

#print a[2]
v=""
for i in a:
  #print i
  if i.isalpha():
    if i.islower():
      #e+=str(v[h][a.index(w.lower())]).upper()
      v=v+oa[aa.index(i.upper())].lower() + " "
    else:
      v=v+oa[aa.index(i.upper())].upper() + " "
  else:
    if i == " ":
      v+="_"
    else:
      v+=i + " "

print v.replace(" _", "_")#[:-1]
