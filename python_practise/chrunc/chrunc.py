#!/usr/bin/python

import sys

lowers="abcdefghijklmnopqrstuvwxyz"
uppers="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="~`!@#$%^&*()_+-=[]\{}|;':\",./<>?"

inp="a%%"
#inp="a%%"

words=[]

#if i == "@":   # lowers
#elif i == ",": # uppers
#elif i == "%": # numbers
#elif i == "^": # symbols
#else:


#bw="baseword"
#for i in range(0,10):
#  print bw + str(i)
#bw="baseword%"
#for i in numbers:
#  print bw.replace("%", i)
#bw="baseword^"
#for i in symbols:
#  print bw.replace("^", i)
#bw="baseword,"
#for i in uppers:
#  print bw.replace(",", i)
#bw="baseword@"
#for i in lowers:
#  print bw.replace("@", i)


def this_plus_this(dis1, dis2):
  return dis1 + dis2

c=inp.count("%")


a="a"

tpo=""
temp=""

for j in range(0,c): 
  tpo=""
  for i in numbers:
    temp=str(i)
    tpo+=this_plus_this(a,str(i))
    print tpo
    tpo=this_plus_this(tpo,temp)






#for j in range(0,c):
#  opt=""
#  for i in numbers:
#    opt+=str(i)
#  print "a"+opt
  


#for i in numbers:
#  print i


#for w in words:
#  print w
