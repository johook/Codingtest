import sys
from itertools import permutations      #순열 구현하기 위해 permutations import

n,m,k=map(int,input().split())
rails=list(map(int,input().split()))
answer=99999 #임의의 큰 수로 설정

def calculate(current):                 #각각의 순열에 리스트에 대해서 값들을 계산
  total=0
  weight=current[0]
  idx,cnt=0,0

"""
count가 k값보다 작을 동안 다음 weight를 갱신해주고 
현재 weight와 다음 weight가 택배바구니 무게보다 무거우면 total에 옮겨주고 count를 하나 늘린다
현재 weight와 다음 weight가 택배바구니 무게보다 가벼우면 현재 weight에 다음 weight를 넣어주고 다음 반복문에서 다음 weight를 설정받는다
idx는 반복문이 한번끝날때(즉 하나의 레일을 넘어갈때) 1씩 증가시켜주고
cnt는 현재무게와 다음무게가 택배바구니 무게보다 무거워서 다음 택배바구니를 가져와야할때 count를 늘린다
"""
  while cnt<k:
    next_weight=current[(idx+1)%n]
    if weight+next_weight>m:
        total+=weight
        weight=next_weight
        cnt+=1
    else:
        weight+=next_weight
    idx+=1
  return total

for i in permutations(rails,n):          # 입력받은 수들을 순열로 구현
  answer=min(answer,calculate(list(i)))  # answer의 값과 calculate함수에서 리턴받은 값을 비교 후 작은 값을 answer에 저장
print(answer)                            # 가장 최소의 answer 값을 출력
