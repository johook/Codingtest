m, n, K = map(int,input().split())

if m>n: #입력이 key값보다 짧다면 secret이 될 수 가없기때문에 정상적인 식권 발급
  print("normal")
  exit()

M="".join(input().split())  #key값을 M이라는 변수에 string으로 받는다
N="".join(input().split())  #입력값을 N이라는 변수에 string으로 받는다

if M in N:                  #key값이 입력값속에 속해있다면 secret 아니라면 normal을 출력
  print("secret")
else:
  print("normal")
