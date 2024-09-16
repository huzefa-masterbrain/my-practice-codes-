my_list=[1,2,3,4,5,6,7,8,9,10]
from random import shuffle
shuffle(my_list)
print(my_list)

def shuffle_list(item):
    shuffle(item)
    return item
result=shuffle_list(my_list)
print(result)