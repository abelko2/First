vlan = input('Vvedite nomer vlan:\n')
with open ('CAM_table.txt') as f:
	for line in f:
		try:
			d = line.split()
			d1 = d[0]
			a = d1.isdigit()
		except IndexError:
			continue
		if a == True:
			if d1 == vlan:
				print('{}  {}  {}'.format(d[0],d[1],d[3]))
			else:
				continue
		else:
			continue
