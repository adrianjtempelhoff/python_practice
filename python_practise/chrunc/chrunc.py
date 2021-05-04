#!/usr/bin/python

import sys
import time

baseword=""

symbols="!@#$%^&*(){}[]|\/.,<>?`~-_=+"
numbers="0123456789"
uppers="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers="abcdefghijklmnopqrstuvwxyz"

tmp=sys.argv[1]
print tmp

tmp=tmp.replace("^", "(symbol)")
tmp=tmp.replace("%", "(number)")
tmp=tmp.replace(",", "(upper)")
tmp=tmp.replace("@", "(lower)")
print tmp

words=[]

temp1=""#"word^%,@"
temp2=tmp#"word(symbol)(symbol)(number)(upper)(lower)"

#words.append("testing one added")
words.append(temp2)

scount=temp2.count("(symbol)")
ncount=temp2.count("(number)")
ucount=temp2.count("(upper)")
lcount=temp2.count("(lower)")

def do_symbols():
  for wrd in words:
    #print wrd
    if wrd.__contains__("(symbol)"):
      for sym in symbols:
        n=wrd.replace("(symbol)",sym,1)
        words.append(n)

def do_numbers():
  for wrd in words:
    #print wrd
    if wrd.__contains__("(number)"):
      for num in numbers:
        n=wrd.replace("(number)",num,1)
        words.append(n)

def do_uppers():
  for wrd in words:
    #print wrd
    if wrd.__contains__("(upper)"):
      for upp in uppers:
        n=wrd.replace("(upper)",upp,1)
        words.append(n)

def do_lowers():
  for wrd in words:
    #print wrd
    if wrd.__contains__("(lower)"):
      for low in lowers:
        n=wrd.replace("(lower)",low,1)
        words.append(n)
  

if scount > 0:
  do_symbols()

if ncount > 0:
  do_numbers()

if ucount > 0:
  do_uppers()

if lcount > 0:
  do_lowers()
#print words

#for jj in range(0,scount):
#  do_symbols()

#print words

for wrd in words:
  print wrd

# this seems to be working

# usage: python chrunc.py word^%,@
# ^ symbols
# % number
# , uppers
# @ lowers
