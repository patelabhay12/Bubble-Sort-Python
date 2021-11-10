A=[]
n=int(input("Enter Size of the list :"))
for i in range(n):
    val=int(input("Enter your number :"))
    A.append(val)
def Bubble_Sort(A):
    l=len(A)
    for i in range(l):
        for j in range(l-(i+1)):
            if(A[j]>A[j+1]):
                A[j],A[j+1]=A[j+1],A[j]

Bubble_Sort(A)
print(A)
                
