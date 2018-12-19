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
					n1 = []
					k = False
				else:
					continue
			elif line.startswith(' '):
				if line[1] == ' ':
					n1.append(line.rstrip())
					k = True
					k7[m] = n1
				else:
					m = line.rstrip()
					n.append(line.rstrip())
					k = False
					k7 = {Key: [] for Key in n}
			else:
				pass
			if k == True:
				result_command[glob] = k7
			else:
				result_command[glob] = n
	return result_command

get_int_vlan_map('config_r1.txt')

print(result_command)
