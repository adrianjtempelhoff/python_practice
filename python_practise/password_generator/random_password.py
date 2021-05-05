#!/usr/bin/python

from random import randint

a="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c="~!@#$%^&*()_+-=[]\{}|;:,./<>?" #"~!@#$%^&*()_+-=[]\{}|;':\",./<>?"

tmp=""
for i in range(0,30):
  t=randint(0,2)
  #print t
  if t == 0:
    tmp+=a[randint(0,len(a)-1)]
  elif t == 1:
    tmp+=b[randint(0,len(b)-1)]
  else:
    tmp+=c[randint(0,len(c)-1)]

print tmp
