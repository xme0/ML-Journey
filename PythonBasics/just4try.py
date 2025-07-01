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