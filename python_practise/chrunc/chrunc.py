#!/usr/bin/python

import sys
import time

starttime=time.time()

print "chrunc.py is a remake of crunch, wordlist generator"

print "and a poor one at that, you might want to consider using the original"

baseword=""

pattern=[]

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
usrinp=list(tmp)
print usrinp
usrinp2=usrinp


#length of usrinpt to keep track of position in arrays of patterns added
pointer=[]

words=[]

for i in usrinp: # for i in range(0,len(usrinp)-1):
  if i == "(symbol)":#"^":
    #print "symbol"
    pointer.append(0)
  elif i == "(number)":#"%":
    #print "number"
    pointer.append(0)
  elif i == "(uppper)":#",":
    #print "upper"
    pointer.append(0)
  elif i == "(lower)":#"@":
    #print "lower"
    pointer.append(0)
  else:
    #print i    
    pointer.append("-")

pointer2=pointer

# show the list of counters, or pointers
#for point in pointer:
#  print point

usrinp.reverse()
pointer.reverse()

for i in range(0,len(usrinp)):
  #print i
  k=usrinp[i]
  if k == "(symbol)":#"^":
    #print "symbol"
    #print symbols[pointer[i]]
    pointer[i]+=1
  elif k == "(number)":#"%":
    #print "number"
    #print numbers[pointer[i]]
    pointer[i]+=1
  elif k == "(upper)":#",":
    #print "upper"
    #print uppers[pointer[i]]
    pointer[i]+=1
  elif k == "(lower)":#"@":
    #print "lower"
    #print lowers[pointer[i]]
    pointer[i]+=1
  #print k

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

def ggg(bww):
  for q in bww:
    if q == "(symbol)": #"^":
      for i in symbols:
        words.append(bww.replace("^", i, 1))
    elif q == "(number)": #"%":
      for i in numbers:
        words.append(bww.replace("%", i, 1))
    elif q == "(upper)": #",":
      for i in uppers:
        words.append(bww.replace(",", i, 1))
    elif q == "(lower)": #"@":
      for i in lowers:
        words.append(bww.replace("@", i, 1))


#bw=sys.argv[1]#"baseword^"

#cnt=bw.count("^") + bw.count("%") + bw.count(",") + bw.count("@")

#bw=list(bw)
#bw.reverse()
#bw2=""
#for i in bw:
#  bw2+=i

#for q in bw:
#  if q == "(symbmol)": #"^":
#    for i in symbols:
#      print bw.replace("^", i, 1)
#  elif q == "(number)": #"%":
#    for i in numbers:
#      print bw.replace("%", i, 1)
#  elif q == "(upper)": #",":
#    for i in uppers:
#      print bw.replace(",", i, 1)
#  elif q == "(lower)": #"@":
#    for i in lowers:
#      print bw.replace("@", i, 1)
    

# hahahahaha theres a logic error is this code that when you use symbols it goes into and endless
# loop continually replacing the marker symbol with symbols lol


ggg(bw) # ggg(bw2)

for w in words:
  print w
#  #w2=list(w)
#  #w2.reverse()
#  #ww2=""
#  #for i2 in w2:
#  #  ww2+=i2
#  #print ww2
  if cnt >= 2:
    ggg(w)



endtime=time.time()

runtime=endtime-starttime

print "endtime  : "+str(endtime)

print "starttime: "+str(starttime)

print "runtime  : "+str(runtime)




