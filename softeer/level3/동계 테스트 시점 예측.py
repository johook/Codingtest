import sys
from collections import deque


n,m=map(int,input().split())
cnt=0
ma=[]
for i in range(n):
  ma.append(list(map(int,input().split())))
visit=[[0]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs():
    queue=deque()
    # 0,0부터 탐색을 시작한다, 0,0은 처음이기 때문에 visit을 1로 해준다
    queue.append((0,0))
    visit[0][0]=1

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            # 얼음이 있는 곳은 visit을 1증가시키고, 얼음이 없는 곳은 방문한적이 없다면 큐에 append하고 visit을 1로 바꾼다(다음번에 또 실행되지않기위해서)
            if 0<=nx<n and 0<=ny<m:
                if ma[nx][ny]==1:
                    visit[nx][ny]+=1
                elif visit[nx][ny]==0:
                    queue.append([nx,ny])
                    visit[nx][ny]=1
    # 2번이상 방문한 곳은 얼음에서 물로 바꿔준다(1->0)
    for x in range(n):
        for y in range(m):
            if visit[x][y]>=2:
                ma[x][y]=0

while 1:
    if ma.count([0]*m)==n:
        break
    visit=[[0]*m for _ in range(n)]  # 한번 실행될때마다 visit을 초기화해준다
    bfs()
    cnt+=1
    
print(cnt)
