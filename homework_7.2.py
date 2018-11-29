from sys import argv
config = argv[1]
with open (config) as f:
	for line in f:
		if line.startswith('!'):
			continue
		else:
			print(line)

