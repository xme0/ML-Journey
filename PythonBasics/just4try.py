print(2 ** 3) # 8 -> exponent ex
print(10 % 3) # 1 -> modulus ex
print(10 // 3) # 3 -> integer division ex (out is integer)
print(10 / 3) # 3.33333335 -> division ex (out is float)
print(10 * 3) # 30 -> multiplication ex
print(10 - 3) # 7 -> subtraction ex
print(10 + 3)# 13 -> addition ex

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
print(' ')
# without sep
print('the','sep','keyword')
#the sep keyword
# with sep
print('the','sep','keyword', sep=',')
#the,sep,keyword

# print(type(input("s : ")))

# num = int(input("enter number :"))
# while num in range(1,4):
#     if num == 1 :
#         print(1)
    
#     elif num == 2 : 
#         print(2)  
    
#     else :
#         print(3)
    
#     num = int(input("enter number :"))
    
    
    
# num = 1
# if num == 1 :
#     print(num) # 1
# elif num == 2 :
#     print(num)
# else:
#     print(num)
# num = 1 
# match num:
#     case 1:
#        print(num) 
#     case 2 :
#         print(num)
#     case _:#default case
#         print(num)




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