N=int(input())

square_num=1*4**N             #사각형은 4의제곱으로 증가한다 why? 한 변당 2배로 늘어나기 때문
x=(square_num)**(1/2)         # 한 변의 사각형개수 -1 이 한변의 점의 개수
point=(x+1)**2                # 한변의 점의 개수의 제곱    
print(int(point))          
