# 내가 처음짠 코드(출력값은 나오지만 시간이 over된다)
K,P,N=map(int,input().split())
for i in range(N):
  K*=P
result=K%1000000007
print(result)

# pow()함수 사용해서 재구현-> 속도가 훨씬 빨라짐
K,P,N=map(int,input().split())

# %1000000007을 두번 더한 이유는 [1000000007*1000000007] 보다 큰값이 나오면 나머지를 또구해야하기때문 
print(K*pow(P,N,1000000007)%1000000007%1000000007)
