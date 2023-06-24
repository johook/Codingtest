import sys

n,k=map(int,input().split())
visit=[]
s=[]
visit.extend(input())

# 먼저 부품은 0으로 로봇을 p로 설정하여 부품을 집을때마다 부품을 1로 증가시킨다
for i in visit:
  if i=='H':
    s.append(0)
  if i=='P':
    s.append('P')
    
# 라인의 길이동안 반복하여 로봇이면 좌우로 k만큼 떨어진 곳을 지정해서 왼쪽부터 부품이 0인지 확인한다
# 0이면 1로 바꾸고 break하여 반복문을 탈출한다
for i in range(n):
  if s[i]=='P':
    if i<k and n-i-1>=k:
      for j in range(0,i+k+1):
        if s[j]==0:
          s[j]=1
          break
    elif i>=k and n-i-1<k:
      for j in range(i-k,n):
        if s[j]==0:
          s[j]=1
          break
    elif i<k and n-i-1<k:
      for j in range(0,n):
        if s[j]==0:
          s[j]=1
          break
    else:
      for j in range(i-k,i+k+1):
        if s[j]==0:
          s[j]=1
          break
count=0

# 끝난 후에 리스트안에 1인 부품(로봇에 의해 집어진 부품)의 개수를 세고 출력한다
for i in s:
  if i==1:
    count+=1
print(count)
