test = {'FastEthernet0/12':10,
'FastEthernet0/14':11,
'FastEthernet0/16':17,
'FastEthernet0/17':150}

access_template = ['switchport mode access',
'switchport access vlan',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

result =[]

def open_file(intf,vlan):
	result.append(intf)
	for line in access_template:
		if line.endswith('access vlan'):
			k = line +' ' + str(vlan)
			result.append(k)
		else:
			result.append(line)
	return result

for d in test.items():
	open_file(*d)

print(result)
