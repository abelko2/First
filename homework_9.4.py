result_command = {}

def ignore_command(command, ignore):
	return any(word in command for word in ignore)

def get_int_vlan_map(cfg):
	ignore = ['duplex', 'alias', 'Current configuration']
	with open(cfg) as f:
		for line in f:
			if line.startswith('!'):
				continue
			elif ignore_command(line, ignore) == True:
				continue
			elif not line.startswith(' '):
				if line.rstrip():
					glob = line.rstrip()
					n = []
				else:
					continue
			elif line.startswith(' '):
				n.append(line.rstrip())
			else:
				pass
			result_command[glob] = n
	return result_command

get_int_vlan_map('config_sw1-home9.txt')

print(result_command)
