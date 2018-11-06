london_co = {
'r1' : {
'location': '21 New Globe Walk',
'vendor': 'Cisco',
'model': '4451',
'ios': '15.4',
'ip': '10.255.0.1'
},
'r2' : {
'location': '21 New Globe Walk',
'vendor': 'Cisco',
'model': '4451',
'ios': '15.4',
'ip': '10.255.0.2'
},
'sw1' : {
'location': '21 New Globe Walk',
'vendor': 'Cisco',
'model': '3850',
'ios': '3.6.XE',
'ip': '10.255.0.101',
'vlans': '10,20,30',
'routing': True
}
}
r1 = input ('Enter device name: ')
b = str(london_co[r1].keys ())
b1 = b[11:-2]
k1 = london_co[r1]
r2 = input('Enter parameter name ({} )'.format(b1))
r2 = r2.lower()
print(k1.get(r2, 'Takogo parametra net'))
