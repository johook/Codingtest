import sys
n,k=map(int,input().split())
score=list(map(int,input().split()))
gap=[]
for i in range(k):
    gap.append(list(map(int,input().split())))
#score=sorted(score,reverse=True) 이건 성적순으로 sorting한 것

for s,f in gap:
    total=0
    for i in range(s-1,f):
        total+=score[i]
    total=total/(f-s+1)
    print(f"{total:.2f}") # 이 형식대로 하면 자릿수조절과 반올림을 한번에 할 수 있다.
