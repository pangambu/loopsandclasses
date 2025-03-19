import random
import time

mylist =  list("ABCDEFGH")
a = random.choices(mylist, k=3)
print(a)


random.shuffle(mylist)
print(mylist)