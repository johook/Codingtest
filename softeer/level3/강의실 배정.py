# 초기 식
import sys
n=int(sys.stdin.readline())
lec=[]
for i in range(n):
  lec.append(list(map(int,input().split())))

# 중요 key가 x인데 x[1] 즉 강의 끝나는 시간 기준으로 sorting한다
# 그런데 이 sort함수에서 시간이 오래걸려서 heap정렬로 변환
lec=sorted(lec,key=lambda x : x[1])

cnt=0
now=0

# sorting된 리스트 가지고 강의 끝난시간보다 다음 강의 시작시간이 더 작으면
# count늘리지않는다
for start,end in lec:
    if now<=start:
        cnt+=1
        now=end 
print(cnt)



# 고친 식

import sys
import heapq

n=int(sys.stdin.readline())
lec=[]
for i in range(n):
  start,end=list(map(int,sys.stdin.readline().split()))    #start, end 입력 받고
  heapq.heappush(lec, (end,start))                         #heappush를 통해 end 기준으로 정렬한다

cnt=0
now=0   
                                                           # lec(end, start)라서 lec[0][1]이면 시작시간이고 lec[0]이면 종료시간
while lec:                                                 # lec리스트의 lec[0][1](시작시간)보다 now(종료시간)가 작으면 heap에 있는 0번째 요소를 pop하면서 now로 재설정
    if lec[0][1]>=now:                                     # 그렇지 않으면(시작 시간이 이전 종료시간보다 작을때) 그냥 heap에 있는 요소 pop
        now=heapq.heappop(lec)[0]
        cnt+=1
        continue
    heapq.heappop(lec)

print(cnt)
