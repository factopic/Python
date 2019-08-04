#--------------------------------------------1 List email

emails=['me@gmail.com','you@hotmail.com','they@gmail.com']
for items in emails:
	if 'hotmail' in items:
		print(items)


print('-------------------------------------')
#--------------------------------------------2 List int

myList = [1,2,3.45,5]
for i in myList:
	print(i)


print('-------------------------------------')
#--------------------------------------------3 List Str



xtr= 'BAnAnA'
for j in xtr:
	print j



print('-------------------------------------')
#--------------------------------------------4 List Str



fruit = ['apple','banana','pine','orange','pine']

for i in fruit:
	print(i)



print('-------------------------------------')
#--------------------------------------------5 if



for i in fruit:
	if i == 'pine':
		print i


print('-------------------------------------')
#--------------------------------------------6 break
# pine is printing 

for x in fruit:
	print x
	if x == 'pine':
		break



print('-------------------------------------')
#--------------------------------------------6 continue
# banana is not printing because if comes before print

for i in fruit:
	
	if i == 'banana':
		continue
	print i

print('-------------------------------------')
#--------------------------------------------7



"""
output
you@hotmail.com
1
2
3.45
5


make sure in if statement items

"""