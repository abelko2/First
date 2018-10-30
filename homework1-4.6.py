In [2]: ospf_route = 'O  10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

In [6]: str =ospf_route.split()

In [7]: str
Out[7]: 
['O',
 '10.0.24.0/24',
 '[110/41]',
 'via',
 '10.0.13.3,',
 '3d18h,',
 'FastEthernet0/0']

In [10]: a1 = str[1]

In [12]: a2 = str[2]
In [23]: a20 = a2[1:7]

In [25]: a3 = str[4]
In [39]: a30 = a3[:-1]

In [27]: a4 = str[5]
In [41]: a40 = a4[:-1]

In [29]: a5 = str[6]

In [34]: t1 = '''
    ...: Protocol:              OSPF
    ...: Prefix:                {}
    ...: AD/Metric:             {}   
    ...: Next-Hop:              {}
    ...: Last update:           {}
    ...: Outbound Interface:    {} 
    ...: '''

In [43]: print(t1.format(a1,a20,a30,a40,a5))

Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41   
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0
