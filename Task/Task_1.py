# Design the UDF that will perform below
# mentioned string operations for user input string

# Wordwise Reverse for the given string

# 2 characters interchange for the given string


s="this is string example"
v=s
l=s
print(s[::-1])
x=s.split(' ')
y=''
z=""
for i in x:
    y+=i[::-1]
    y+=" "
print(y)
seq=(x)
s="-"
c=s.join(seq)
print(c)
b=v.replace('this is','this was')
print(b)
o=''
for i in l:
    if i=='i':
        i='s'
    elif i=='s':
        i='i'
    o+=i
print(o)
l=l.translate(str.maketrans('i','s'))
print(l)