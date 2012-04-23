#!/usr/bin/env python
#
#  Google Code Jam
#  ===============
#
#  Alvaro Vila Martinez - @alvarovmz
#  <alvarovmz@gmail.com>
#

import sys


N = int(sys.stdin.readline().strip())
for f in range(1, N+1):
    print 'Case #%d:' % f,

    input  = map (int, sys.stdin.readline()[:-1].split(' '))

    l=[]
    for i in xrange(input[0], input[1]+1):
        number = str(i)
        p = [int(x) for x in number if x>= number[0]]
        for j in p:
            n = int(number[j:]+number[:j])
            if (i < n and input[0]<=n and n<=input[1]):
                l.append((i,n))
            
    print len(set(l))  
