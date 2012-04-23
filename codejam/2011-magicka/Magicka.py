#!/usr/bin/env python
#
#  Google Code Jam
#  ===============
#
#  Alvaro Vila Martinez - @alvarovmz
#  <alvarovmz@gmail.com>
#

def solve(comb_dict,  opp, invok):
	
#	print "Comb	-> ", comb_dict
#	print "Opp 	-> ", opp
#	print "Invok 	-> ", invok

	final = ""
	final += invok.pop(0)

	while(invok):
		final+=invok.pop(0)
		try: # Combined
			new = comb_dict[final[-2:]]
			final = final[:-2]
			final += new
		except: # Opposed
			for i in opp:
				if (i[0] in final) and (i[1] in final):
					final = "" 

	return final

##################

f = open("test", "r")

f.readline()

case = 1

for i in f.readlines():	
	i = i[:-1].split(' ')
	n_comb = int(i.pop(0))
	comb = i[:n_comb]
	i = i[n_comb:]
	n_opp=int(i.pop(0))
	opp = i[:n_opp]
	i = i[n_opp:]
	invok = i[1]
	comb_dict={}

	for i in comb:
		a = i[:2]
		comb_dict[a] = i[2]
		comb_dict[a[::-1]] = i[2]

	if invok:
		solution =  solve(comb_dict,  opp, list(invok))
		print "Case #%d: %s" % (case, list(solution).__str__().replace('\'',''))
		case +=1



