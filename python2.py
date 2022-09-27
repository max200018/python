
s=input().split()
arr=list(map(int,s))
a=int(input())
b=int(input())
c=int(input())
cnt=0
for i in range(len(arr)):
  for j in range(i+1,len(arr)):
    for k in range(j+1,len(arr)):
      if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
        cnt+=1
print(cnt)
