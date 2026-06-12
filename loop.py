for i in range(1,21):
    if i == 15:
        print("the break statement is executed")
        break
    print(i)
else:
    print("the loop is break in this point")

#print tables
n = int(input("enter the value of tab;e you want to print into the screen "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")

#sum of n numbers
sum=0
n = int(input("enter a number :"))
for i in range(n):
    sum += i
print(f"the sum of n number is : {sum}")

#factorial of a number

def fact(n):
    fact=1
    for i in range(n,1,-1):
        fact = fact*i
    return fact
    
print(fact(5))
#to print sum of even and odd number range separetely
n = int(input("enter a value "))
even = 0
odd = 0
for i in range(0,n+1,2):
    even = even + i
print(even)
for i in range(1,n,2):
    odd = odd + i
print(odd)

#prime number 
n = int(input("enter a number :"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count +=1
if count == 2:
    print("number is prime")
else:
    print("number is not prime")
#reverse string using loop 
name = "sohan patel"
new = ""
for i in range(len(name)-1,-1,-1):
    new += name[i]
print(f"the reverse string is : {new}")