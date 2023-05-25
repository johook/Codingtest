import sys
#제약조건이 노드개수가 100,000개까지 있을 수 있는데
#DFS에서 사용하는 재귀함수의 recurssionlimit default값이 1,000이다
#따라서 setrecursionlimit을 사용해서 1,000,000의 재귀 제한으로 늘려준다
sys.setrecursionlimit(10**6) 

#입력조건들을 입력받는다
N,M=map(int,input().split())
adj=[[]for _ in range(N+1)]
adjR=[[]for _ in range(N+1)]
for _ in range(M):
  x,y=map(int,input().split())
  adj[x].append(y) #나가는 간선
  adjR[y].append(x) #들어오는 간선 

S,T=map(int,input().split())

#DFS사용해서 탐색을한다
def DFS(graph,start,visited):
  if visited[start]==1:
    return
  visited[start]=1
  for i in graph[start]:
    DFS(graph,i,visited)
  return

#출발점, 끝점에서 나가는 간선(adj)과 출발점 끝점으로 들어오는 간선(adjR)에 대한 리스트를 만들어준다 
fromS = [0]*(N+1)
fromS[T]=1
DFS(adj,S,fromS)

fromT = [0]*(N+1)
fromT[S]=1
DFS(adj,T,fromT)

toS = [0]*(N+1)
DFS(adjR,S,toS)

toT = [0]*(N+1)
DFS(adjR,T,toT)

#리스트에 j번째 항목이 모두 1이라면
#출발점과 끝점에서 j번째 항목으로 가는 간선 + j번째 항목에서 출발점 끝점으로 가는 간선 모두있는 것이기때문에 
#count를 1씩 올려준다
count=0
for j in range(1,N+1):
  if fromS[j] and fromT[j] and toS[j] and toT[j]:
    count+=1
print(count-2) #중간에 있는 점만 세야하는데 출발점, 끝점까지 세기때문에 2 빼준다
