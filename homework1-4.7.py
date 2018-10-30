n [1]: MAC = 'AAAA:BBBB:CCCC'

In [2]: m = list(MAC)

In [3]: m.remove(':')

In [4]: m.remove(':')

In [5]: x = [int(vlan, 16) for vlan in m]

In [9]: x
Out[9]: [10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12]

In [10]: x0 = x[0]

In [11]: x1 = x[1]

In [12]: x2 = x[2]

In [13]: x3 = x[3]

In [14]: x4 = x[4]

In [17]: x5 = x[5]

In [18]: x6 = x[6]

In [21]: x7 = x[7]

In [22]: x8 = x[8]

In [23]: x9 = x[9]

In [24]: x10 = x[10]

In [25]: x11 = x[11]

In [28]: itog = '{:b}{:b} {:b}{:b} {:b}{:b} {:b}{:b} {:b}{:b} {:b}{:b}'.format(x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10
    ...: ,x11)

In [29]: 

In [29]: itog
Out[29]: '10101010 10101010 10111011 10111011 11001100 11001100'

