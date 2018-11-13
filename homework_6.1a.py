# -*- coding: utf-8 -*-

a = input('Vvedite IP address: ')

prov1 = a.count('.')

a1 = a.split('.')
try:
	k =0
	b1 = int(a1[0])
	b2 = int(a1[1])
	b3 = int(a1[2])
	b4 = int(a1[3])
	if b1 >=0:
	    if b1 <=255:
	        pass
	    else:
	        k+=1
	else:
	    k+=1
	if b2 >=0:
	    if b2 <=255:
	        pass
	    else:
	        k+=1
	else:
	    k+=1
	if b3 >=0:
	    if b3 <=255:
	        pass
	    else:
	        k+=1
	else:
	    k+=1
	if b4 >=0:
	    if b4 <=255:
	        pass
	    else:
	        k+=1
	else:
	    k+=1
	while k>=0:
		if prov1 ==4:
		    pass
		elif k>0:
		     print('Incorrect IPv4 address')
		     break
		elif b1==255:
		    if b2==255:
		         if b3==255:
		             if b4==255:
		                 print('local broadcast')
		             else:
		                 print('unused')
		                 break
		         else:
		                 print('unused')
		                 break
		    else:
		                 print('unused')
		                 break
		elif b1 >239:
		    print('unused')
		    break
		elif b1>=224:
		     print('multicast')
		     break
		elif b1>=1:
		    print('unicast')
		    break
		elif b1==0:
		    if b2==0:
		         if b3==0:
		             if b4==0:
		                 print('unassigned')
		                 break
		             else:
		                 print('unused')
		                 break
		         else:
		                 print('unused')
		                 break
		    else:
		                 print('unused')
		                 break
		else:
		     print('Incorrect IPv4 address')
		     break
except (ValueError,NameError):
        print('Incorrect IPv4 address')

