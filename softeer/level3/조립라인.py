import sys
n=int(input())
time=[]

for i in range(n-1):
    time.append(list(map(int,input().split())))
f_time=list(map(int,input().split()))

# 현재 A와 B의 조립라인에서의 시간
A,B=0,0
# 처음부터 지금까지의 A와 B의 시간
una,unb=0,0

for i in range(n-1):
    if i==n-1:
        break
    # A의 조립라인에서와서 A의 조립라인을 가던지
    # B의 조립라인에서와서 B에서A로 시간을 더하던지
    A=min(time[i][0]+una, time[i][1]+time[i][3]+unb)

    # B의 조립라인에서와서 B의 조립라인을 가던지
    # A의 조립라인에서와서 A에서B로 시간을 더하던지
    B=min(time[i][1]+unb,time[i][0]+time[i][2]+una)
    una=A
    unb=B

# 마지막 A와 B의 작업시간을 더해준다
una+=f_time[0]
unb+=f_time[1]

# 두 경우중에 더 작은 경우를 출력
print(min(una,unb))
