x=(input())
y=int(input())
z=[]
for i in range(len(x)):
    y1=x[i:]+x[:i]
    z.append(y1)
z1=[]
for i in z:
    y2=i[0]+i[:0:-1]
    z1.append(y2)
for i in z1:
    z.append(i)
k=sorted(z)
print(k)

'''x=input()
y=x[0]+x[:0:-1]
print(y)'''

'''k=[]
for i in range(len(z)):
    y2=z[i:]+z[:i]
    k.append(y2)
z1=[]
for i in k:
    for j in i:
        z1.append(j)
l=sorted(z1)
print(l)
print(l[y])'''
'''import numpy
n=int(input())
z=[]
while(n>1):
    rem=n%10
    div=n/10
    n=(pow(10,len-1))*rem+div
    z.append(n)
print(z)'''
    
