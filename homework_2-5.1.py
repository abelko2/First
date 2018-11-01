#!/usr/bin/env python

start = input ('Vvedite IP/MASK seti:\n')

print('_'*20)

print('\n')

a1 = start.split('.')

a2 = a1[3].split('/')

ip1 = int(a1[0])

ip2 = int(a1[1])

ip3 = int(a1[2])

ip4 = int(a2[0])

mask = int(a2[1])

q = str('1'*mask)
#Opredeliya skol'ko 1 i 0 v maske
q1 = 32 - mask

q2 = str('0'*q1)

w = q+q2
# Slojenie strok

w1 = int(w[0:8], 2)

w2 = int(w[8:16], 2)

w3 = int(w[16:24], 2)

w4 = int(w[24:32], 2)

t1 = ['Network:\n' '{0:<8} {1:<8} {2:<8} {3:<8}\n' '{0:08b} {1:08b} {2:08b} {3:08b}\n' 'Mask:\n' 
'\n' '/{4:}\n' '{5:<8} {6:<8} {7:<8} {8:<8}\n' '{5:<08b} {6:<08b} {7:<08b} {8:<08b}']

print(((' ').join(t1)).format(ip1,ip2,ip3,ip4,mask,w1,w2,w3,w4))
