print 'Enter Conversion from and to '
print 'cm	- centimeter'
print 'm	- meter'
print 'km	- kilometer'
print 'foot	- foot' 

v1 = raw_input('enter value to:')
v2 = raw_input('enter value from:')

a1 = 0
a2 = 0
res = 0

if v1 == 'cm':
	a1 = input('enter cm = ' )
elif v1 == 'm':
	a1 = input('enter m = ' )
elif v1 == 'km':
	a1 = input('enter km = ' )
elif v1 == 'foot':
	a1 = input('enter foot = ' )
else:
	print('invalid input')


if v1 == 'cm' and v2 == 'cm':
	res = a1		
	print (res)

elif v1 == 'm' and v2 == 'm':
	res = a1 
	print (res)

elif v1 == 'km' and v2 == 'km':
	res = a1
	print (res)

elif v1 == 'foot' and v2 == 'foot':
	res = a1
	print (res)

#----------------------------------------

elif v1 == 'cm' and v2 == 'm':
	res = a1/100
	print (res)

elif v1 == 'cm' and v2 == 'km':
	res = a1/(100*1000)
	print (res)

elif v1 == 'cm' and v2 == 'foot':
	res = a1/32.48
	print (res)

#----------------------------------------

elif v1 == 'm' and v2 == 'cm':
	res = a1 * 100
	print (res)
elif v1 == 'm' and v2 == 'km':
	res = a1 / 1000
	print (res)
elif v1 == 'm' and v2 == 'foot':
	res = a1 / 0.3048
	print (res)

#---------------------------------------

elif v1 == 'km' and v2 == 'cm':
	print (res)
	res = a1 *(100 * 1000)
elif v1 == 'km' and v2 == 'm':
	res = a1 * 1000
	print (res)
elif v1 == 'km' and v2 == 'foot':
	res = a1 * 3280.84
	print (res)
#----------------------------------------

elif v1 == 'foot' and v2 == 'cm':
	res = a1 *30.48
	print (res)
elif v1 == 'foot' and v2 == 'm':
	res = a1 * 0.3048
	print (res)
elif v1 == 'foot' and v2 == 'km':
	res = a1 * 0.0003048
	print (res)
#---------------------------------------

else:
	print('invalid :')


