result_access = {}
result_trunk = {}

def get_int_vlan_map(cfg):
	with open(cfg) as f:
		for line in f:
			if 'Ethernet' in line:
				intf = line.rstrip()
			elif 'mode access' in line:
				n = 1
				result_access[intf] = n
			elif 'access vlan' in line:
				a = line
				a = a.split()
				for line2 in a:
					if line2.isdigit():
						n = int(line2)
					else:
						continue
				result_access[intf] = n
			elif 'trunk allowed' in line:
				a = line
				a = a.split()
				for line2 in a:
					if line2[1][-1].isdigit():
						n1 = line2.split(',')
						n2 = []
						for line3 in n1:
							k = int(line3)
							n2.append(k)
					else:
						continue
				result_trunk[intf] = n2
			else:
				continue
	return result_access
	return result_trunk

get_int_vlan_map('config_sw2-home9.txt')

print(result_access)
print(result_trunk)
