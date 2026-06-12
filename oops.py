# INHERITANCE
class Address:
    def __init__(self,city,state):
        self.city = city
        self.state = state
    def location(self):
        return f"my location is {self.city} in {self.state} "
class User(Address):
    def __init__(self,age,name,city,state):
        super().__init__(city,state)
        self.age = age
        self.name = name
  
     
        
    def Username(self):
        print(f"my name is {self.name} and my age is {self.age}")
u = User(89,"sohan","jaipur","Rajasthan")
u.Username()
print(u.location())

 # Encapusulaction
class balance:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
    def withdrawal(self,amount):
        if amount<=self.__balance:
            self.__balance -= amount
            print(f"Withdrawal amount : {amount}")
        else:
            print("unsufficient balance")
    def show_balance(self):
        print(f"the balance in your account is {self.__balance}")
acc = balance("sohan",10000)
acc.deposit(1200)
acc.show_balance()
acc.withdrawal(1000)
acc.show_balance()
print(acc.name)
print(acc.__balance) # gives an error

#polymorphism

class CreditCard:
    def pay(self,amount):
        print(f"paid {amount} using credit card ")
class UPI:
    def pay(self,amount):
        print(f"paid {amount} using UPI ")   
class Cash:
    def pay(self,amount):
        print(f"paid {amount} using cash payment ")
def make_payment(payment_method,amount):
    payment_method.pay(amount)
c1 = CreditCard()
u1 = UPI()
cash1 = Cash()
make_payment(c1,1000)
make_payment(u1,2000)
make_payment(cash1,200)

# CLASS VARIABLE
class Student:
    count = 0
    def __init__(self,name):
        self.name = name 
        Student.count += 1
    def show(self):
        print(f"the name of student is : {self.name}")
s1 = Student("sohan")
s2 = Student("shlok")
s3 = Student("pankaj")
s1.show()
s2.show()
s3.show()
print(f"Constructor called {Student.count} times")

# method overriding

class Notification:
    def send(self):
        print("Sending notification")
class Email(Notification):
    def send(self):
        print("Email Notification")
class Sms(Notification):
    def send(self):
        print("SMS notification")
e = Email()
s = Sms()
e.send()
s.send()