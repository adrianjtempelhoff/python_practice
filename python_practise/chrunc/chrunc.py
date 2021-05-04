#!/usr/bin/python

# this is in the process of being refactored
# seems to be working :-)

import sys

addit={"symbols":"!@#$%^&*(){}[]|\/.,<>?`~-_=+","numbers":"0123456789","uppers":"ABCDEFGHIJKLMNOPQRSTUVWXYZ","lowers":"abcdefghijklmnopqrstuvwxyz"}
tmp=str(sys.argv[1]).replace("^", "(symbol)").replace("%", "(number)").replace(",", "(upper)").replace("@", "(lower)")
temp2=tmp
words=[]
words.append(temp2)
cnt=temp2.count("(symbol)")+temp2.count("(number)")+temp2.count("(upper)")+temp2.count("(lower)")

if cnt > 0:
  for wrd in words:
    if wrd.__contains__("(symbol)"):
      for sym in addit["symbols"]:
        n=wrd.replace("(symbol)",sym,1)
        words.append(n)
    elif wrd.__contains__("(number)"):
      for sym in addit["numbers"]:
        n=wrd.replace("(number)",sym,1)
        words.append(n)
    elif wrd.__contains__("(upper)"):
      for sym in addit["uppers"]:
        n=wrd.replace("(upper)",sym,1)
        words.append(n)
    elif wrd.__contains__("(lower)"):
      for sym in addit["lowers"]:
        n=wrd.replace("(lower)",sym,1)
        words.append(n)

for wrd in words:
  print wrd

# usage: python chrunc.py word^%,@
# ^ symbols
# % number
# , uppers
# @ lowers
