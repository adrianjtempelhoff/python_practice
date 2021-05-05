#!/usr/bin/python3

import os

# colored text and background 
def prRed(skk): print("\033[91m ### {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m   # {}\033[00m" .format(skk)) 
#def prYellow(skk): print("\033[93m #{}\033[00m" .format(skk)) 
#def prLightPurple(skk): print("\033[94m #{}\033[00m" .format(skk)) 
#def prPurple(skk): print("\033[95m #{}\033[00m" .format(skk)) 
#def prCyan(skk): print("\033[96m #{}\033[00m" .format(skk)) 
#def prLightGray(skk): print("\033[97m #{}\033[00m" .format(skk)) 
#def prBlack(skk): print("\033[98m #{}\033[00m" .format(skk)) 

def chck(res):
  if str(res) != "32512":
    return "exists"
  else:
    return "doesn't exist"

def kchc(dep):
  res=os.system(str(dep) + " --version > /dev/null 2>&1")
  #print(dep)
  return chck(res)

print("This python script checking if the required programs are installed.")

dependent=["ls","lasdfs", "ptrace", "ltrace"]
#results=[]

for dep in dependent:
  r=kchc(dep)
  if r != "exists":
    prRed(dep + " does not exist")
  else:
    prGreen(dep + " exists")

