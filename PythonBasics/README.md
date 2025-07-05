# Python Basics
## Math Operators
From highest to lowest precedence:
|Operators|Operation|Example|
|-|-|-|
|**|Exponent|2 ** 3 = 8|
|%|Modulus/Remainder|10 % 3 = 1|
|//|Integer division (Floor division)|10 // 3 = 3|
|/|Division|10 / 3 = 3.333335|
|*|Multiplication|10 * 3 = 30|
|-|Subtraction|10 - 3 = 7|
|+|Addition|10 + 3 = 13|

## Comments
### Inline comment :
```python
# this is a comment
```
### Multiline comment:
```python
# multiline
# comment
```
anther way :
```python
"""
multiline
comment
"""
```
use this with care. python will still create  a string object,even if unused.
## Control Flow
###  If/Else
```python
num = 1
if num == 1 :
    print(num) # 1
elif num == 2 :
    print(num)
else:
    print(num)
```
### Switch-Case 
```python
num = 1 
match num:
    case 1:
       print(num) 
    case 2 :
        print(num)
    case _:#default case
        print(num)
```
### While Loop
```python
num = int(input("enter number :"))
while num != 0:
    if num == 1 :
        print(1)
    
    elif num == 2 : 
        print(2)  
    
    else :
        print(3)
    
    num = int(input("enter number :"))
```
### For loop
```python
num = int(input("enter number :"))
for num in [1,2,3]:#num in range(1,4)
    if num == 1 :
        print(1)
    
    elif num == 2 : 
        print(2)  
    
    else :
        print(3)
    
    num = int(input("enter number :"))
```

## Data structures
### Lists
```python
names = ['Lois Griffin','Peter Griffin','Stewie Griffin']
# index        0       ,       1       ,       2
print(names[0])#Lois Griffin
print(names[1])#Peter Griffin
print(names[2])#Stewie Griffin
# print(names[3])  error
print(names[-1])#Stewie Griffin
print(names[-2])#Peter Griffin
print(names[-3])#Lois Griffin
#print(names[-4]) error

print(names[0:3])#['Lois Griffin', 'Peter Griffin', 'Stewie Griffin']
print(names[2:3])#['Stewie Griffin']
print(names[0:-1])#['Lois Griffin', 'Peter Griffin']
print(names[:2])#['Lois Griffin', 'Peter Griffin']
print(names[1:])#['Peter Griffin', 'Stewie Griffin']
print(names[:])#['Lois Griffin', 'Peter Griffin', 'Stewie Griffin']

print(len(names))#3

# add
names.append("Brian Griffin")
```


## The end keyword
The keyword argument end can be used to avoid the newline after the output, or end the output with a different string:
```python
phrase = ['the','end','keyword']

# without end
for word in phrase:
    print(word)
    # the
    # end
    # keyword
# with out 
for word in phrase:
    print(word, end=' ')
    #the end keyword
```
## The sep keyword
The keyword sep specify how to separate the objects, if there is more than one:
```python
# without sep
print('the','sep','keyword')
#the sep keyword
# with sep
print('the','sep','keyword', sep=',')
#the,sep,keyword
```