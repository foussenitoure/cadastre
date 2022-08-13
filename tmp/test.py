import random
import datetime

# age = int(input())
# if (age > 0 and age < 11):
#       print("child")
#
# elif(age >= 12 and age< 17):
#       print("Teen")
#
# else:
#     (age >= 18 and age< 65)
#     print("Adult")

def string(strr):
    lst = []
    for x in strr.split():
        lst.append(int(x))
        print(lst)
string("0 1 2 3 4 5 6 7 8 9")