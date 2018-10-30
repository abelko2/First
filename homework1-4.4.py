command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

c1 = command1[30:]
c2 = command2[30:]
sp1 = c1.split(',')

sp2 = c2.split(',')

set1 = set(sp1)

set2 = set(sp2)

itog = set1.intersection(set2)
itog1 = [int(vlan) for vlan in itog if vlan.isdigit()]

itog1.sort()

print(itog1)




