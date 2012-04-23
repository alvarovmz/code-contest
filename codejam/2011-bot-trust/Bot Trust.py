#!/usr/bin/env python
#
#  Google Code Jam
#  ===============
#
#  Alvaro Vila Martinez - @alvarovmz
#  <alvarovmz@gmail.com>
#

def solve(line):

	secs = 0
	pos_1 = 1
	pos_2 = 1

	while (line):
		time = 0
		actual = line[0]

		while (actual == line[0]):
			actual = line.pop(0)
			button = int(line.pop(0))
			# Robot 1
			time += abs(pos_1-button)
			pos_1 = button
			time += 1
			if not line:
				break

		try:
			next = line[0]
			button = int(line[1])
			move = abs(pos_2-button)

			if time > move:
				pos_2=button
			else:
				if button > pos_2:
					pos_2 +=time
				else:
					pos_2 -= time
		except:
			pass

		secs += time
		a = pos_1
		pos_1= pos_2
		pos_2=a

	return secs

################################

f = open("test", "r")
f.readline()
i = 1
for line in f.readlines():
	n = solve(line[:-1].split(' ')[1:])
	print "Case #%d: %d"%(i,n)
	i+=1
