trunk_template = ['switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan']

trunk_dict = { 'FastEthernet0/1':[10,20,30],
'FastEthernet0/2':[11,30],
'FastEthernet0/4':[17] }

result = []

def open_file(intf,*vlan):
	result.append(intf)
	for line in trunk_template:
		if line.endswith('allowed vlan'):
			vlan = str(vlan)
			k = line +' ' + vlan[2:-3]
			result.append(k)
		else:
			result.append(line)
	return result

for d in trunk_dict.items():
	open_file(*d)

print(result)
