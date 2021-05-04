#!/usr/bin/python

import sys

lowers="abcdefghijklmnopqrstuvwxyz"
uppers="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="~`!@#$%^&*()_+-=[]\{}|;':\",./<>?"

inp=sys.argv[1] # "," # "word@,%^"

pt=[]
sp=list(inp)
sp.reverse()

for i in sp:
  if i == "@":
    pt.append(0)
  elif i == ",":
    pt.append(0)
  elif i == "%":
    pt.append(0)
  elif i == "^":
    pt.append(0)
  else:
    pt.append("-")

print pt
print sp

position=0

opt=""

while position < len(sp):
  #print position
  if pt[position] != '-':
    #print sp[position]
    lng=0
    chrs=""
    if sp[position] == "@":
      lng=len(lowers)
      chrs=lowers
    elif sp[position] == ",":
      lng=len(uppers)
      chrs=uppers
    elif sp[position] == "%":
      lng=len(numbers)
      chrs=numbers
    elif sp[position] == "^":
      lng=len(symbols)
      chrs=symbols
    while pt[position] < lng:
      opt += chrs[pt[position]]
      pt[position]+=1
      #break
  else:
    opt+=sp[position]
  if position == len(sp):
    position=0
    opt=""
  else:
    position+=1
    print opt
