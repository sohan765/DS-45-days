def merge(A,B):
    (C,m,n) = ([],len(A),len(B))
    (i,j)= (0,0)
    while i+j<m+n:
        if i==m:
            C.append(B[j])
            j = j+1
        elif j==n:
            C.append(A[i])
            i = i+1
        elif A[i]<=B[j]:
            C.append(A[i])
            i= i+1
        elif A[i]>B[j]:
            C.append(B[j])
            j= j+1
    return(C)
def mergesort(A,left,right):
    if right - left <= 1:
        return(A[left:right])
    if right - left>1:
        mid = (left+ right)//2
        L = mergesort(A,left,mid)
        R = mergesort(A,mid,right)
    return(merge(L,R))


A = list(range(0,100,2)) + list(range(1,100,2))
list(range(1,100,2))
# len(A)== 50
# len(B)== 37
# #print(A,B)
# p =merge(A,B)

print(A)
B = mergesort(A,0,len(A))
print(B)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


def is_palindrome(string):
    stack = Stack()
    
    # Push all characters onto the stack
    for char in string:
        stack.push(char)
    
    reversed_string = ""
    
    # Pop all characters to build reversed string
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    # Check if original and reversed strings are the same
    return string == reversed_string


# Example usage
text = input("Enter a string: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")
