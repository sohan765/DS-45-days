# to print a list into a single line 

marks = [1,2,3,4,5,34,78]

subject = ["AEM","OOP","SE","TC","DSA","DE"]
def print_list(list):
   for item in list:
       print(item,end="")
print(marks)
print()
print(subject)
print()        
num = int(input("enter a number"))
fact = 1
for i in range(1,num+1):
    fact *= i
print(fact)
def cal_inr(usd_val):
    inr_val = usd_val*83
    print("usd_val","USD =",inr_val,"INR")
cal_inr(345)    



n = int(input("enter a number"))
def sum(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")
print(sum) 



# recursion
def print_list(list, i=0):
    if(i == len(list)):
        return
    print(list[i])
    print(list,i)

student = ["sohan ","shlok"]
print_list(student) 

# FILE HANDLING IN PYTHON HOW TO OPEN READ AND WRITE CLODE IN A FILE

f = open("demo.txt","w")
data = f.write()
print(data)
print(type(data))
f.close()

f= open("demo.txt","r")
data = f.read(3)
print(data)
line1 = f.readline()
print(line1)
line2  = f.readline()
print(line2)
f.close() 

#f= open("demo.txt","w")
#f.write("my first job get into in a good company")
f= open("demo.txt","r+")
f.write("vghkjab")
f.close()


with open("demo.txt","r") as f:
    data = f.read()
    print(data)
with open("demo.txt","w") as f:
    f.write("my name is sohan patel ")
    
with open("demo.txt","r") as f:
  data = f.read()

new_data = data.replace("java","python")
print(new_data)
     
with open("demo.txt","w") as f:
   f.write(new_data)
 # to search a value which is lies or not in a file
word = "hy"
with open("demo.txt","r") as f:
    data = f.read()
    if(data.find(word) !=-1):
        print("found")
    else:
        print("not found")

def check():
    word = "python"
    data = True
    line_no = 1
    with open("demo.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
        
        return -1

print(check()) 

count = 0
with open("demo.txt","r" ) as f:
    data = f.read()
    nums = data.split(",")
    for i in nums:
        if( int(i)%2 == 0):
            count += 1

print(count)  
class Student:
    # defult constuctor
    def __init__(self):
        pass
    # parameterized constucrtor
    def __init__(self,name,marks):
        self.name = name
        self.marks =marks
        print("adding a new student data")

s1 = Student("sohan",98)
print(s1.name,s1.marks)
s2 = Student("pankaj",33)
print(s2.name,s2.marks)
s3 = Student("shlok",56)
print(s3.name,s3.marks)
s4 = Student("rishi",34)
print(s4.name,s4.marks)