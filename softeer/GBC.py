N,M=map(int,input().split())

length=[];velocity=[] 
L=[];V=[] 

#제한 구간 및 속도/실제 구간 및 속도를 입력받음
for i in range(N):
  x,y=map(int,input().split())
  length.append(x);velocity.append(y)
for i in range(M):
  X,Y=map(int,input().split())
  L.append(X);V.append(Y)

MAX=0
i=0;j=0
"""
제한구간과 실제 구간을 비교해서 
제한구간이 더 길면 제한구간에 실제구간 빼준 길이 넣어주고
실제구간이 더 길면 실제구간에 제한구간 빼준 길이 넣어준다.

그 구간동안 실제속도-제한속도>0 이고 MAX값보다 크다면 MAX값 갱신 
"""


while(True):
  if(i==N or j==M):
    break
  if(length[i]<L[j]):
    L[j]=L[j]-length[i]
    if(V[j]-velocity[i]>0):
      if(MAX<(V[j]-velocity[i])):
        MAX=V[j]-velocity[i]
    i+=1
  elif(length[i]>L[j]):
    length[i]=length[i]-L[j]
    if(V[j]-velocity[i]>0):
      if(MAX<(V[j]-velocity[i])):
        MAX=V[j]-velocity[i]
    j+=1
  elif(length[i]==L[j]):
    if(V[j]-velocity[i]>0):
      if(MAX<(V[j]-velocity[i])):
        MAX=V[j]-velocity[i]
    i+=1;j+=1

print(MAX)
