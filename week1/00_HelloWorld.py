

3*8



x=54
y=7
if x==54:
    y=10
    print(y)


for i in range(1,5):
    x+=1
    print(x, x+y)
    i+=1



def max(x,y):
    if x>=y:
        max=x
    else:
        max=y
    return max


print(max(10,20))


X=[1,2,3,4,5,"peter"]
X[0]

for item in X:
    print(item)



A={'a','b','c','d','e','f','f'}
print(A)



for item in A:
    print(item)
type(A)


B={'a','b','g'}



print(A-B)



print(A&B)


c=(1,2,3)


print(A|B)



print(A^B)

print(len(A))


print ('a' in A)


print ('z' in A)



sum=0
for i in range(1,10):
    sum+=1/(2*i)
    print(sum)


sum=0
for i in range(1,10):
    sum+=1/(pow(i,2))
    print(sum)


import matplotlib as pl
import pandas as  pd
import plotly as ply


import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("A subset of array a = ", a[2:5])


addTwo = lambda x: x * 2
  
print("Array after addition function: ", addTwo(a))

Amat = np.array([[1.1, 2, 3], [3, 4, 5]]) 
print(Amat)

Amat.shape

Bmat=Amat.reshape(3,2)
Amat.transpose