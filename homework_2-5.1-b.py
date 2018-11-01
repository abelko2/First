#!/usr/bin/env python
from sys import argv

start2 = argv[1:]

start = start2[0]

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

e = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(ip1,ip2,ip3,ip4)

esrez = e[0:mask]

eitog = esrez + q2

e1 = int(eitog[0:8], 2)

e2 = int(eitog[8:16], 2)

e3 = int(eitog[16:24], 2)

e4 = int(eitog[24:32], 2)


t1 = ['-'*20 +'\n'*2 +'Network:\n' '{0:<8} {1:<8} {2:<8} {3:<8}\n' '{0:08b} {1:08b} {2:08b} {3:08b}\n' 'Mask:\n' 
'\n' '/{4:}\n' '{5:<8} {6:<8} {7:<8} {8:<8}\n' '{5:<08b} {6:<08b} {7:<08b} {8:<08b}']

print(((' ').join(t1)).format(e1,e2,e3,e4,mask,w1,w2,w3,w4))
