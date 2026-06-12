d = {"name":"hello","age":20}
print(d.keys())
print(d.values())
for i in d.keys():
    print("key=",i)
    print("values=",d[i])
d={
  "Message": "Number of Post office(s) found: 6",
  "Status": "Success",
  "PostOffice": [
    {
      "Name": "Achrol",
      "Description": "",
      "BranchType": "Sub Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Jaitpura Khinchi",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Kali Pahadi",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Kant",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Labana",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Rajpurawas Tala",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    }
  ]
}
print(d["Message"])
print(d["Status"])
print("Name is :")
for i in d["PostOffice"]:
  print(i["Name"])
print("the Taluk is:")
for i in d["PostOffice"]:
  print(i["Taluk"])
print("the circle is :")
for i in d["PostOffice"]:
  print(i["Circle"])
print("the district is :")
for i in d["PostOffice"]:
  print(i["District"])
print("the division is :")
for i in d["PostOffice"]:
  print(i["Division"])
print("the Region is :")
for i in d["PostOffice"]:
  print(i["Region"])
print("the state is :")
for i in d["PostOffice"]:
  print(i["State"])
print("the Country is :")
for i in d["PostOffice"]:
  print(i["Country"])
print("\n")

dict = {"address":{"address1":{"city":"kukas","district":"jaipur"},
                   "address2":{"city":"andheri","district":"mumbai"}}}
for i in dict["address"]["address1"]:
    print(i)
    print(dict["address"]["address1"][i])
for i in dict["address"]["address2"]:
    print(i)
    print(dict["address"]["address2"][i])
print(dict["address"]["address1"]["city"])
print(dict["address"]["address1"]["district"])
print(dict["address"]["address2"]["city"])
print(dict["address"]["address2"]["district"])

l = [10,20,30,["hello","hello1","hello2",[True,False]]]

print(l)

print(l[3][0:4])
print(l[3][3][0:2])
import random

num = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Enter a number between 1 and 100: "))

    if guess == num:
        tries += 1
        print("You guessed the correct number!")
        print("Total tries:", tries)
        break

    elif guess > num:
        tries += 1
        print("The number is too high")

    elif guess < num:
        tries += 1
        print("The number is too low")
    else:
        tries += 1
        print("try again")
def square(x):
    return x*x
l = [10,20,30]
l1 = list(map(square,l))
print(l1)

l = ["spple","banana","mangia"]
l1 = []
for i in l:
    if "a" == i[-1]:
        l1.appned(i)
print(l1)