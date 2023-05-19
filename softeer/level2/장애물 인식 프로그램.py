n=int(input())
MAP=[]
result=0
count=[]

def find(x,y): #재귀적으로 1인 배열들을 찾아준다 (BFS방식)
  if x>=n or y>=n or x<=-1 or y<=-1: #주어진 범위 넘어가면 return false
    return False
  elif MAP[x][y]==1:  #1일때 count해주고 그 배열값은 0으로 바꾼후(다음에 또 검출되면 안되니까) 재귀적으로 상하좌우 find해준다 
    count.append(1)
    MAP[x][y]=0
    find(x-1,y)
    find(x,y-1)
    find(x+1,y)
    find(x,y+1)
    return True
  return False


for i in range(n):
  MAP.append(list(map(int,input())))  #MAP 리스트 안에 리스트 형태로 지도 저장

result_num=[]
for i in range(n):
  for j in range(n):  
    if find(i,j)==True:    #해당 리스트 값이 1일때 총 결과 값 1올려주고 find 함수에서 얻은 count수를 result_num에 추가해준 후 count 리스트를 clear해준다 
      result+=1
      result_num.append(len(count))
      count=[]
    
print(result)           #결과값 출력 후 1의 개수를 오름차순으로 놓은 후 순서대로 출력해준다 
result_num.sort()     
for i in result_num:
  print(i)
