#countdown
def countdown(num):
    new = []
    for x in range(num,-1,-1):
        new.append(x)
    return new
print(countdown(12))
#Print and Return
def print_and_return(a,b):
    print(a)
    return(b)
print(print_and_return(3,567))
#first plus length
def first_plus_length(alist=[]):
    varone = alist[0]
    print(alist[0])
    print (len(alist))
    varone += (len(alist))
    return varone
print(first_plus_length([1,2,3,4,5]))

#values greater than second
def new_list(first=[]):
    sec_list = []
    if len(first)< 2:
        return False
    for num in range(len(first)):
        if (first[1] < (first[num])):
            sec_list.append(first[num])
    return sec_list
print(new_list([2,3,2,7,8,7,6,5]))

#this length, that value
def lengthvalue(size,value):
    that = []
    for num in range(size):
        that.append(value)
    return that
print(lengthvalue(4,7))
print(lengthvalue(6,2))