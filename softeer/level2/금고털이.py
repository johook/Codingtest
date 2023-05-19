W,N=map(int,input().split()) #map함수는 input형태를 앞에있는 파라미터화(함수화) 시켜준다 int로 input을 받겠다 
MP=[]
total=0
for i in range(N):
  mp=list(map(int,input().split())) #값을 아예 list로 받아서 
  MP.append(mp) #MP라는 list안에 list로 append를 한다 

MP.sort(key=lambda x:x[1],reverse=True) 
#key =lambda x:x[1] 이 뜻은 MP안에 있는 list 중에 1번쨰 리스트에 있는 값을 기준으로 sort해주겠다는 뜻

for m,p in MP:
  if(W<m):
    total+=W*p
    break
  else:
    total+=m*p
    W-=m
print(total)
