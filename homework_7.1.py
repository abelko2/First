with open ('ospf2.txt','r') as f:
	f=f.read().rstrip()
	
str =f.split()

a1 = str[3]

a2 = str[4]
a20 = a2[1:7]

a3 = str[6]
a30 = a3[:-1]

a4 = str[7]
a40 = a4[:-1]

a5 = str[8]
a50 = a5[:-1]

t1 = '''
Protocol:              OSPF
Prefix:                {}
AD/Metric:             {}   
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {} 
'''

print(t1.format(a1,a20,a30,a40,a50))
