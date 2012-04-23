#!/usr/bin/env python
#
#  Google Code Jam
#  ===============
#
#  Alvaro Vila Martinez - @alvarovmz
#  <alvarovmz@gmail.com>
#

def solve(line):

	r=0
	value=0
	line.sort()

	for i in line:
		r ^= i
		value += i

	if r==0:
		return value-line[0]
	else:
		return "NO"

################################

f = open("test", "r")
f.readline()
i = 1
j = 1

for line in f.readlines():
	if j == 1:
		j=0
		continue
	n = solve(map (int, line[:-1].split(' ')))
	j=1
	print "Case #%d: %s"%(i,str(n))
	i+=1
