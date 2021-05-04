#!/usr/bin/python

print "vigenere cypher"

a=["a","b","c","d","e","f","g","h","i","j","k","l","m",
   "n","o","p","q","r","s","t","u","v","w","x","y","z"]
v=[]
n=[]
t=""
c=0
for i in a:
  #print i
  for ii in a[c:]:
    t+=ii
    n+=ii
  for ii in a[:c]:
    t+=ii
    n+=ii
  #print t
  v+=[n]
  n=[]
  t=""
  c+=1

#print v

print v[0]

print v[13]

print v[25]


rot=input("what rotation(0-25): ")

print v[rot]

emsg=""

dmsg=raw_input("message: ") #"hack"

print "the message: " + dmsg

for w in dmsg:
  #print "the letter: " + w
  f=a.index(w)
  #print "the index: " + str(f)
  #print "the encoded letter: " + str(v[rot][f])
  emsg+=str(v[rot][f])
  #print "\n"

print emsg
#emsg=""

#for h in range(0,len(v)):
#  for w in dmsg:
#    f=a.index(w)
#    emsg+=str(v[h][f])
#  print emsg + " : " + str(h)
#  emsg=""




