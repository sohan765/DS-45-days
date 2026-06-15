student = {
"name" : "sohan",
"age": 23,
"subjects":{
    "phy": 34,
    "chem" :345

}
}
print(student.get("name"))
print(student.update(age= 43))
collection = set()
set2 = {1,3,2,89,34}
collection.add(1)
collection.add(2)
collection.add("sohan")
print(collection)
def addToList(a): 
	a += [10] 
b = [10, 20, 30, 40] 
addToList(b) 
print (len(b)) 

l = [1,2,3,4,5]
def findpos(l,v):
    (found,i) = (False,0)
    while i<len(l):
        if not found and l[i]==v:
            (found,i)==(True,i)
             
            return i
        
        if not found:
            pos = -1

            i=i+1
            
           

print(findpos([1,2,3,4,5],4))

def findpos(l,v):
    (pos, i) =(-1,0)
    for x in range(len(l)):
        if x == v:
            pos = i
            return i
            break
        i = i+1
print(findpos([1,2,3,4,5],3))