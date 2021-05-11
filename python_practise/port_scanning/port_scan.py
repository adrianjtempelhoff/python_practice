#!/usr/bin/python
import sys
import socket
g=sys.argv[1]
i=0
for port in range(1,1024):
  #print "scanning port %s bytes" % str(port)
  try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=s.connect((g,port))
    print "open " + str(port)
    s.close()
  except:
    i=i+1
    #print "closed"


