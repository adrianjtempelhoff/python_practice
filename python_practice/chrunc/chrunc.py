#!/usr/bin/python
# seems to be working :-)
import sys

addit={"symbol":"!@#$%^&*(){}[]|\/.,<>?`~-_=+","number":"0123456789","upper":"ABCDEFGHIJKLMNOPQRSTUVWXYZ","lower":"abcdefghijklmnopqrstuvwxyz"}

words=[str(sys.argv[1]).replace("^", "(symbol)").replace("%", "(number)").replace(",", "(upper)").replace("@", "(lower)")]

for wrd in words:
  for ad in addit:
    if wrd.__contains__("("+ad+")"):
      for s in addit[ad]:
        n=wrd.replace("("+ad+")",s,1)
        words.append(n)
        print n

# usage: python chrunc.py word^%,@
# ^ symbols
# % number
# , uppers
# @ lowers
