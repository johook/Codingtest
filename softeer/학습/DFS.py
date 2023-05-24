def DFS(graph,start,visited):
  visited[start]=1
  print(start)

  for i in graph[start]:
    if not visited[i]:
      DFS(graph,i,visited)

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


visited = [0] * 9

DFS(graph, 1, visited)
