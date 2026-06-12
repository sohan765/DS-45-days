def hello():
    print("hello good morning everyone")
hello()
def student(*a):
    print(a)
    print(type(a))
student(1,2,3,4,4,5,6)
def marks(l):
    for i in range(len(l)):
        print(l[i])
marks([10,20,30,40,50])
def hello(l):
    for i in range(len(l[0])):
        print(l[0][i])
hello(["hello","address"])

# lamda function
add = lambda x:x # [lambda argument : expression]
print(add(100))

sum = lambda x,y : x+y
print(sum(20,30))
sum1 = lambda *x:[print(i) for i in x]
sum1(1,2,3,4,5,6)

a = lambda x:[print(i) for i in x]
l = [20,30,40,20,60]
a(l)
nums = [1, 2, 3, 4, 5]

for_each = lambda lst: [print(x) for x in lst]

for_each(nums)
print([i for i in range(6)]) # single line loop
l = [1,2,3,4,5,6]
print([l[i] for i in range(len(l))])

l1 = [10,20,[30,40,50,60]]
print([l1[2][i] for i in range(len(l1[2]))])

import random

num = random.randint(1,100)
tries =0
while True:
    guess = int(input("enter a number for the guessing in range between 1 to 100 "))
    if guess == num :
        tries+=1
        print("you guess correct number")
        break
    elif guess>num:
        trries +=1
        print("tne number is too low")
    elif guess<num:
        print("number is too high")
        tries += 1
    else :
        print("guess is incorrect")

