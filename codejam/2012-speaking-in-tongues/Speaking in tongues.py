#!/usr/bin/env python
#
#  Google Code Jam
#  ===============
#
#  Alvaro Vila Martinez - @alvarovmz
#  <alvarovmz@gmail.com>
#

import sys

trans = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's',\
         'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u',\
         'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n',\
         'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a',\
         'x': 'm', 'z' : 'q', 'q':'z'}



N = int(sys.stdin.readline().strip())
for f in range(1, N+1):
    print 'Case #%d:' % f,

    w  = list(sys.stdin.readline().rstrip('\n'))
    out = ''
    for i in range(0, len(w)):
        out += trans[w[i]]
    print out
 
