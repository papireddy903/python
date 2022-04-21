mylist=list(map(int,input().split()))
length=len(mylist)
temp=0
temp=mylist[length-1]
mylist[length-1]=mylist[0]
mylist[0]=temp

print(mylist)