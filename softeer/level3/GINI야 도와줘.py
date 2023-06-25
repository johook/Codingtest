import sys 
from collections import deque

R,C=map(int,input().split())
M=[[] for _ in range(R)]
for i in range(R):
  M[i].extend(input())
X=0;Y=0
for i in range(R):
  for j in range(C):
    if M[i][j]=='W':
      X=i;Y=j
dx=[-1,1,0,0]
dy=[0,0,-1,1]

visit=[[1]* C for _ in range(R)]

"""
*을 발견하고 그 상하좌우에 .이 있다면 *로 번지게 한다
제약조건은 
1. 범위를 벗어나면 안되고 
2. 원래는 .인데 이전에 *때문에 번진 *은 rain이라는 리스트를 두고 연속적으로 번지지 않게한다
"""
def rainshower():
    rain=[[0]* C for _ in range(R)]
    for a in range(R):
        for b in range(C):
            if M[a][b]=='*' and rain[a][b]==0:
                for k in range(4):
                    na=a+dx[k]
                    nb=b+dy[k]
                    if 0<=na<R and 0<=nb<C:
                        if M[na][nb]=='.':
                            M[na][nb]='*'
                            rain[na][nb]+=1
def bfs(x,y):
  cnt=1
  scnt=0
  queue=deque()
  queue.append((x,y,cnt))
  while queue:
    # 예를들어 오른쪽 왼쪽으로 W가 이동했을때 큐에는 두개의 값이 들어간다 따라서 원래는 한번만 번져야하는 비가 두번번질수있기때문에 조건을 걸어준다
    if cnt>scnt:
        scnt=cnt
        rainshower()
        
    x,y,cnt=queue.popleft()
    cnt+=1
    
    # 이동할수있는 범위를 상하좌우로 두고 그 안에있을때 .이고 방문한적이 없다면 큐에 그 위치(이동할장소)를 append한다
    # 이동할때마다 visit리스트 값을 1씩 증가시키고 마지막H에 도착했을때 그값을 리턴한다
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      #print(nx,ny)
      if 0<=nx<R and 0<=ny<C:
        if M[nx][ny]=='.' and visit[nx][ny]==1:
            visit[nx][ny]+=visit[x][y]
            queue.append((nx,ny,cnt))
      if 0<=nx<R and 0<=ny<C:
        if M[nx][ny]=='H':
            visit[nx][ny]+=visit[x][y]
            return (visit[nx][ny]-1)
  return "FAIL"

print(bfs(X,Y))
