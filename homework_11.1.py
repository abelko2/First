result = {}
def parse_cdp_neighbors(cdp):
	find = cdp.find('>')
	devitog = cdp[0:find]
	dev = []
	dev.append(devitog)
	find = cdp.find('Platform')
	cdp = cdp[find+19:]
	cdp1 = cdp.split()
	cdp1.append('Skol`ko_vsego')
	index = cdp1.index('Skol`ko_vsego')
	cdp1.remove('Skol`ko_vsego')
	i = 9
	b = 1
	dobivaem_dev = 0
	hostcdp = []
	intdev = []
	intcdp = []
	hostcdp.append(cdp1[0])
	while i<index:
		k = cdp1[i]
		k1 = list(k)
		for line in k1:
			if line.isalpha():
				n = k1.index(line)
				break
			else:
				continue
		intcdp1 = k[0:n]
		intcdp2 = cdp1[i-1]
		intcdpitog = intcdp2 + intcdp1
		intcdp.append(intcdpitog)
		hostcdp.append(k[n:])
		intdev1 = cdp1[b]
		intdev2 = cdp1[b+1]
		intdevitog = intdev1 + intdev2
		intdev.append(intdevitog)
		b += 9
		i += 9
		dobivaem_dev += 1
	while dobivaem_dev>0:
		dev.append(dev[0])
		dobivaem_dev -=1
	r_key = list(zip(dev,intdev))
	r_value = list(zip(hostcdp,intcdp))
	for line in r_key:
		result[line] = ()
		for line2 in r_value:
			result[line] = line2
			r_value.remove(line2)
			break
	return result

parse_cdp_neighbors('SW1>show cdp neighborsCapability Codes: R - Router, T - Trans Bridge, B - Source Route BridgeS - Switch, H - Host, I - IGMP, r - Repeater, P - PhoneDevice ID    Local Intrfce   Holdtme     Capability       Platform    Port IDR1           Eth 0/1         122           R S I           2811       Eth 0/0R2           Eth 0/2         143           R S I           2811       Eth 0/0R3           Eth 0/3         151           R S I           2811       Eth 0/0')
print (result)
