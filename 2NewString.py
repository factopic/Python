string=input("Enter string:")
count=0
for i in string:
      count=count+1
new=string[0:2]+string[count-2:count]
new=string[0:2]+string[count-3:count]
print("Newly formed string is:")
print(new)



"
'Case 1:
'Enter string:Hello world
'Newly formed string is:
'Held
 
'Case 2:
'Enter string:Checking
'Newly formed string is:
'Chng

"

Case 3:
'Enter string:Checking
'Newly formed string is:
'Chng

"
Case 4:
'Enter string:Checking
'Newly formed string is:
'Chng

"
