mylist=list(map(int,input().split()))
cout=0
for i in range(len(mylist)):

    cout=mylist.count(mylist[i])
    if (cout==1):
        print(mylist[i]);