#!/usr/bin/python3
#alphabet
a=["a","b","c","d","e","f","g","h","i","j","k","l","m",
   "n","o","p","q","r","s","t","u","v","w","x","y","z"]
#setup variables
v,e,n,c=[],"",[],0
#create the rotation alphabets for each letter
for i in a:
  #the begining part
  for ii in a[c:]:
    #add to n
    n+=ii
  #the remaining part
  for ii in a[:c]:
    #add to n
    n+=ii
  #increment c by 1
  c+=1
  #add n to v
  v+=[n]
  #clear n
  n=[]
#the message to encode/decode
d=input("message: ")
#go through each rotation
for h in range(0,len(v)):
  #go through each letter of the message
  for w in d:
    if w.isalpha():
      #the character substitute
      e+=str(v[h][a.index(w)])
    else:
      e+=w
  #display the variation of message
  print(e + " : " + str(h) + "|" + str((h-26)*-1))
  #clear e
  e=""
