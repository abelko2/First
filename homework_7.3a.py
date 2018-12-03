k = []
with open ('CAM_table.txt') as f:
	for line in f:
		try:
			d = line.split()
			d1 = d[0]
			a = d1.isdigit()
		except IndexError:
			continue
		if a == True:
			k.append(line)
		else:
			continue
	k.sort()
	for line2 in k:
		d = line2.split('\n')
		d = str(d)
		d = d.split()
		d4 = d[4]
		d4 = d4[0:-2]
		print('{}  {}  {}'.format(d[1],d[2],d4))
	k=[]

