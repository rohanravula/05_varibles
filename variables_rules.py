"""rules of variavles"""
"boolian (bool) in bool if the answer is right it shows True if it wrong it shows False"
# print(type(True))
# print(type(False))

# print(2<8)
# print(33>2)
# print(8<3)
# print(dir(str))

'''rules for naming the variables'''
# a=10
# number=13
# _=22
# print(number) #13
# print(a) #10
# print(_) #22
# print(b) #if something variable is not mention then the output comems as "Name Error: name 'b' is not defined"

# _com8=4
# _rt_=67
# # 6y=6 #if we try to print this output it shows syntax error coz a variable cannot start with number.
# # a b=68 # if we try to print this output it shows syntax error coz a vatiable cannot have space betweem them.
# c_t=8
# # u,5.p=8 #if we try to print this output it shows syntax erroe coz a variable cannot use any other special symbole exaept under score(_)

# abcdefghijklmnopqrstuvwxyz=75 #there is no fixed size in naming the variables


# A=8
# B=12
# print(A) #8
# print(B) #12
#hence now if we print A the answer should be 12, if we print B the answer should be 8
# C=A
# A=B
# B=C 
# print(B)
# print(A) 
#this menthod is know as swapping this is used in other languages

# x=4 ; y=10
# # print(x) ; print(y)
# x,y=y,x
# print(x)
# print(y)
# #this method is used in python it is shortcut way 

'''isidentifer method'''
print('abc'.isidentifier())
print('a b c'.isidentifier())
print('_'.isidentifier())
print('a_b'.isidentifier())
print('a7b_'.isidentifier())
print('a3b_7'.isidentifier())
print('8ab_7'.isidentifier())
