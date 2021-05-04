#!/usr/bin/python

print "viginair cypher"

a=["a","b","c","d","e","f","g","h","i","j","k","l","m",
   "n","o","p","q","r","s","t","u","v","w","x","y","z"]
t=""
c=0
for i in a:
  print i
  for ii in a[c:]:
    t+=ii
  for ii in a[:c]:
    t+=ii
  print t
  t=""
  c+=1
