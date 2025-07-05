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

```