#!/usr/bin/python
import sys
from random import randint

a=""
if len(sys.argv) == 2: 
  a=sys.argv[1]
else:
  a=sys.stdin.read()

#print a
#a+="\n"
#a=str(a).replace(" ", "")
#a=str(a).replace("_", "   ")
a=a+"_"
a=str(a).split("_")


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
  for ii in i.split(" "):
    #print ii
    if ii.isalpha():
      if ii.islower():
        v=v+aa[oa.index(ii)].lower()
      else:
        v=v+aa[oa.index(ii.lower())].upper()
    else:
      v+=ii
  v+=" "
print v
