A=[]
def BFS(graph,start,visited):
  A.append(start)
  visited[start]=1
  
  while A:
    v=A.pop(0)
    print(v,end=' ')
    for i in graph[v]:
      if not visited[i]:
        A.append(i)
        visited[i]=1

graph = [
	[],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited=[0]*9
BFS(graph,1,visited)
