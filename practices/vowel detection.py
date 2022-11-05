# def v_identify(user, vowel):
#     for i in vowel:
#         if user==i:
#             return 'vowel'
#     else:    
#         return 'not vowel'    
# user=input('Enter a letter:')
# print(v_identify(user, ['a','e','i','o','u']))


n = input('Apa enter a letter:')
mylist = ['a','e','i','o','u']
flag = False
for i in mylist:
    if n==i:
        flag=True
if flag==True:
    print('vowel')
else:
    print('not')