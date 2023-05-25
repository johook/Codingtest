n, m = map(int,input().split())
N=[] ; M=[]
time=[]

for i in range(n):
    N.append(input())
    time.append([1,1,1,1,1,1,1,1,1])

for i in range(m):
  M.append(input().split())
N.sort()
for i in range(n):
  for j in range(m):
    if(M[j][0]==N[i]):
      time[i][(int(M[j][1])-9):(int(M[j][2])-9)]=[0]*((int(M[j][2])-9)-(int(M[j][1])-9))
print(time)
def possible(arr):
  output=[]
  start=None
  for i in range(len(arr)):
    if arr[i]==1: #리스트가 1이면 시작시간을 정한다 
      if start is None:
        start=f"{i+9:02d}"
    else:  #리스트가 0인데 시작시간이있으면 
      if start is not None:
        end=i+9
        output.append(f"{start}-{end}")
        start=None
  if start is not None:
        end = len(arr) + 9
        output.append(f"{start}-{end} ")

  return "\n".join(output)

for i in range(n):
  print("Room %s:"%N[i])



  if all(v==0 for v in time[i]):
    print("Not available")
    print("-----")
  else:
    print(f"{possible(time[i]).count('-')} available:")
    print(f"{possible(time[i])}")
    if(i!=(n-1)):
      print("-----")
