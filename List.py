thislist = ["apple", "banana", "cherry"]
print(thislist[1])


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

  
  thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


"The union() method returns a new set with all items from both sets:"

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)



def myfunc():
  x = 300
  print(x)

myfunc()
