mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
count = str(mac).count(',')+1
a=0
while a<count:
	b = mac.pop(a)
	b = b.replace(':','.')
	mac.insert(a,b)
	a+=1
print(mac)
