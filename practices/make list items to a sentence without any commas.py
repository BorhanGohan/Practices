#my_method
def concatenate(mylist):
    for i in mylist:
        print(i, end='')
    
concatenate([1,2,3,4,5,6,7,8,9,10])
print()
#w3resources_method
def concatenate(mylist):
    result=''
    for i in mylist:
        result+=str(i)
    return result    
print(concatenate([1,2,3,4,5,6,7,8,9,10]))