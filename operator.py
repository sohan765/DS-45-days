# hello this code is for checking even or odd
num1 = int(input("enter the value of num1 "))
num2 = 2
if num1 % num2 == 0:
    print("number is even ,thank you")
else:
    print("number is odd")

String = input("enter a string :")
print(int(len(String)))
print(String.endswith("an"))
print( String.replace("s","m"))
print(String.lower())
print(String.upper())
print(String.title())# convert into title case
print(String.swapcase())
print(String.capitalize())
num1 = 20
num2 = 10
print(num1 != num2)



a =20
b= 30
a += 1
print(a)
a -= 1
print(a)
a *=20
print(a)
a /=10
print(a)
a //= 2
print(a)

# in case of number 
# positive and negative true 
#  0 == False
# "hello " --> True 
# " " ---> False
print(a and b) # print value of b if it is true 
print(b and a) # print value of a if it is true 
print(a or b) # print value of a if it is true 


l =     [12,34,3,829,292,78]
largest = l[0]
index = 0
for i in range(len(l)):
    if l[i] > largest :
        largest = l[i]
        index= i
print(f"the largest number is :{largest} in index is {index}")