# 1. 순열 이용해서 그리디 문제 풀때 (level3_택배마스터 광우)
import sys
from itertools import permutations

"""
rails 리스트를 n개의 숫자만큼 순열의 경우의 수를 만든다
예를 들어 리스트에 ['A','B','C']가 있고 n = 2일 경우
(A,B),(A,C),(B,A),(B,C),(C,A),(C,B)가 나온다.
"""
for i in permutations(rails,n):
  answer=min(answer,calculate(list(i)))
print(answer)
# 추가로 조합(combinations)도 있다

# 2. sorted() 함수 (level3_강의실 배정)
score=sorted(score)                   # 오름차순으로 정렬
score=sorted(score,reverse=True)      # 내림차순으로 정렬
lec=sorted(lec,key=lambda x : x[1])   # 리스트가 있을 때 [0,1] 1번째 요소를 바탕으로 sorting
lec=sorted(lec,key=lambda x: x[1],reverse=True)


