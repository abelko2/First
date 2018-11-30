from sys import argv
config = argv[1]
#Передача через argv в скприпт того, что не будет выводиться в sh_run
ignore = argv[2:]
with open (config) as f:
	for line in f:
		if line.startswith('!'):
			continue
		else:
			for line2 in ignore:
				a = line2 in line
				if a == True:
					break
				else:
					continue
			else:
				if a == True:
					continue
				else:
					print(line)

