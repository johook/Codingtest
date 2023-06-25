import sys

k,p,n=map(int,input().split())

"""
cal(2,10) = cal(2,5)*cal(2,5)
cal(2,5) = cal(2,2)*cal(2,2)*2
cal이 지수를 나타내는 함수라고 생각하면됌
일반적인 **은 시간초과로 안된다 
시간초과가 나면 재귀적용법을 생각해보자
"""
def cal(x,y):
    if y==1:
        return x
    elif y%2==0:
        a=cal(x,(y/2))
        return a*a % 1000000007
    else:
        b=cal(x,(y-1)/2)
        return b*b*x % 1000000007


virus= cal(p,10*n)*k
print(virus%1000000007)
