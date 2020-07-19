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


Q12.What is type conversion in Python?
Ans: Type conversion refers to the conversion of one data type iinto another.

int() – converts any data type into integer type

float() – converts any data type into float type

ord() – converts characters into integer

hex() – converts integers to hexadecimal

oct() – converts integer to octal

tuple() – This function is used to convert to a tuple.

set() – This function returns the type after converting to set.

list() – This function is used to convert any data type to a list type.

dict() – This function is used to convert a tuple of order (key,value) into a dictionary.

str() – Used to convert integer into a string.

complex(real,imag) – This functionconverts real numbers to complex(real,imag) number.





Q22. How can you randomize the items of a list in place in Python?
Ans: Consider the example shown below:

1
2
3
4
from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)
The output of the following code is as below.

['Flying', 'Keep', 'Blue', 'High', 'The', 'Flag']



