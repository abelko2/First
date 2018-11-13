# -*- coding: utf-8 -*-

a = input('Vvedite IP address: ')

a1 = a.split('.')

b1 = int(a1[0])

b2 = int(a1[1])

b3 = int(a1[2])

b4 = int(a1[3])

if b1==255:
    if b2==255:
         if b3==255:
             if b4==255:
                 print('local broadcast')
             else:
                 print('unused')
         else:
                 print('unused')
    else:
                 print('unused')
elif b1 >239:
    print('unused')
elif b1>=224:
     print('multicast')
elif b1>=1:
    print('unicast')
elif b1==0:
    if b2==0:
         if b3==0:
             if b4==0:
                 print('unassigned')
             else:
                 print('unused')
         else:
                 print('unused')
    else:
                 print('unused')
else:
     print('unused')
