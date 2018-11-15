trunk_template = ['switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk allowed vlan']

fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'},
'trunk':{'0/1':['add','10','20'],'0/2':['only','11','30'],'0/4':['del','17']} }

for intf, vlan in fast_int['trunk'].items():
     print('interface FastEthernet' + intf)
     for command in trunk_template:
         if command.endswith('allowed vlan'):
             if 'add' in vlan[0]:
                 vlan.pop(0)
                 vlan.insert(0,'add ')
                 vlan = ','.join([str(vlans) for vlans in vlan])
                 a = vlan.find(',')
                 vlan = list(vlan)
                 vlan.pop(a)
                 vlan = ''.join([str(vlans) for vlans in vlan])
                 print(' {} {}'.format(command, vlan))
             elif 'only' in vlan[0]:
                 vlan.pop(0)
                 vlan = ','.join([str(vlans) for vlans in vlan])
                 print(' {} {}'.format(command, vlan))
             elif 'del' in vlan[0]:
                 vlan.pop(0)
                 vlan.insert(0,'remove ')
                 vlan = ','.join([str(vlans) for vlans in vlan])
                 a = vlan.find(',')
                 vlan = list(vlan)
                 vlan.pop(a)
                 vlan = ''.join([str(vlans) for vlans in vlan
                 print(' {} {}'.format(command, vlan))
             else:
                 print('NE TE COMANDY')
         else:
             print(' {}'.format(command))

