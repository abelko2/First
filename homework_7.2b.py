from sys import argv
config = argv[1]
#Передача через argv в скприпт того, что не будет выводиться в sh_run
ignore = argv[2:]
with open (config) as f, open ('config_sw1_cleared.txt','w') as f1:
	for line in f:
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
				f1.write(line)

