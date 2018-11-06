access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']
trunk_template = ['switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk allowed vlan {}']
i1 = input ('Enter interface mode (access/trunk):\n')
i2 = input ('Enter interface type and number:\n')
itog = ['access','trunk']
itog = {key:[] for key in itog}
itog['access'] = 'Enter VLAN number:'
itog['trunk'] = 'Enter allowed VLANs:'
i3 = input ('{}\n'.format(itog[i1]))
v1 = ','.join(access_template)
v2 = ','.join(trunk_template)
access_template = v1.replace(',', '\n')
trunk_template = v2.replace(',', '\n')
itog['access'] = access_template
itog['trunk'] = trunk_template
a = itog[i1].format(i3)
k = '''
\ninterface {}
{}
'''
print(k.format(i2,a))
