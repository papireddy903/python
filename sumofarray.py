a=[]
sum=0
n=int(input("Number of elements in array:"))
for i in range(0,n):
   l=int(input())
   a.append(l)
   sum=sum+l
print(a)
print('sum of array is ',sum)