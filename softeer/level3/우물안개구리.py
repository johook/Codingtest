import sys
n,m=map(int,input().split())


w=list((input().split()))
lose=[1]*n
cnt=0

for i in range(m):
  a,b=map(int,input().split())
  if int(w[a-1])<int(w[b-1]):
    lose[a-1]=0
  elif int(w[a-1])>int(w[b-1]):
    lose[b-1]=0
  elif int(w[a-1])==int(w[b-1]):
    lose[a-1]=0
    lose[b-1]=0
for i in lose:
  if i== 1:
    cnt+=1

print(cnt)
