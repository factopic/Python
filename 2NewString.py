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
What is PYTHONPATH?
Ans: It is an environment variable which is used when a module is imported. Whenever a module is imported, PYTHONPATH is also looked up to check for the presence of the imported modules in various directories. The interpreter uses it to determine which module to load.



Q17.What is __init__?
Ans: __init__ is a method or constructor in Python. This method is automatically called to allocate memory when a new object/ instance of a class is created. All classes have the __init__ method.
