test = {'FastEthernet0/12':10,
'FastEthernet0/14':11,
'FastEthernet0/16':17,
'FastEthernet0/17':150}

access_template = ['switchport mode access',
'switchport access vlan',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

port_security = ['switchport port-security maximum 2',
'switchport port-security violation restrict',
'switchport port-security']

result ={}

def open_file(intf,vlan,psecurity = False):
	result2 = []
	n = ''
	result[intf] = ''
	for line in access_template:
		if line.endswith('access vlan'):
			k = line +' ' + str(vlan)
			result2.append(k)
		else:
			result2.append(line)
	if psecurity == True:
		for line in port_security:
			result2.append(line)
			n = ','.join(result2)
			result[intf] = n
	else:
		n = ','.join(result2)
		result[intf] = n
	return result


for d in test.items():
	open_file(*d,psecurity = True)

print(result)
