
a = 5
b = 25
c = a + b
text = "Addition of a , b: {} "
print(text.format(c))
text1 = "a : {},"
text2 = " b : {},"
text3 = " a + b = {}"
print(text1.format(a) + text2.format(b) + text3.format(c))
textn = "a: {}, b: {}, a+b: {}"
print( textn.format(a,b,c) )