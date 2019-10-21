s1 = input("Enter the String")
word = input("Enter String to be search")
for i in s1:
    for j in word:
        if i == j:
            print("true")
        else :
            print(0)