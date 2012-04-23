#!/usr/bin/env python
#
#  Google Code Jam
#  ===============
#
#  Alvaro Vila Martinez - @alvarovmz
#  <alvarovmz@gmail.com>
#

import sys, math


N = int(sys.stdin.readline().strip())
for f in range(1, N+1):
    print 'Case #%d:' % f,

    input  = map (int, sys.stdin.readline()[:-1].split(' '))

    ok = 0
    surp = input[1]

    for i in xrange(3, 3+ input[0]):
        if (math.ceil(input[i]/3.0) >= input[2]):
            ok+=1
        elif (input[i] > 1) and ((input[i]%3) != 1) and (surp > 0) and ((math.ceil(input[i]/3.0))+1 >=input[2]):
            surp-=1
            ok +=1
            
    print ok
