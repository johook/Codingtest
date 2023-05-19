#6031
n=int(input()) #유니코드 숫자를 문자로 변환해줌 
print(chr(n))

#6032
n=int(input())
print(-n)

#6033
c=input()
print(chr(ord(c)+1))

#6034
a,b=input().split()
print(int(a)-int(b))

#6035
a,b=input().split()
print(float(a)*float(b))

#6036
a,b=input().split()
b=int(b)
print(a*b)

#6037
a=int(input())
b=input()
print(b*a)

#6038
a,b=input().split()
a,b=int(a),int(b)
print(a**b)


#6039
a,b=input().split()
print(float(a)**float(b))

#6040
a,b=input().split()
print(int(a)//int(b))

#6042
a=float(input())
print(format(a,".2f")) #format함수는 반올림해준다 

#6043
a,b=input().split()
print(format(float(a)/float(b),".3f"))

#6048
a=int(input())
print(a<<1) #비트연산자 a<<1은 2배 a>>1 1/2배 

#6052
a,b=input().split()
a=int(a); b=int(b)
if a<b:
  print("True") 
else:
  print("False")  

#6053
a=int(input())
print(not bool(a))

#6059
a=5
print(~a)

#6062
a=int(input())
print(~a)

#6063
a,b=input().split()
a=int(a);b=int(b)
print(a^b)

#6065
a,b=input().split()
a,b=int(a),int(b)
if a>=b:
  print(a)
else:
  print(b)

#6066
a,b,c=input().split()
a,b,c=int(a),int(b),int(c)

if a%2==0:
  print(a)
if b%2==0:
  print(b)
if c%2==0:
  print(c)

#6067
a,b,c=input().split()
a,b,c=int(a),int(b),int(c)

if a%2==0:
    print("even")
else:
    print("odd")

if b%2==0:
    print("even")
else:
    print("odd")
  
if c%2==0:
    print("even")
else:
    print("odd")

#6068
a=int(input())

if a<0:
  if a%2==0:
    print("A")
  else:
    print("B")
if a>0:
  if a%2==0:
    print("C")
  else:
    print("D")

#6072
a=int(input())
if 90<=a<=100:
  print("A")
elif 70<=a<=89:
  print("B")
elif 40<=a<=69:
  print("C")
elif 0<=a<=39:
  print("D")
  
#6073
a=1
while(a!=0):
  a=int(input())
  if a!=0:
    print(a)
  
#6074
a=int(input())
while(a>0):
  print(a)
  a=a-1
  
#6075
a=int(input())
while(a>0):
  print(a-1)
  a=a-1
  
#6076
a=int(input())
for i in range(0,a+1):
  print(i)
  
#6077
a=int(input())
b=0
while(a>0):
  if a%2==0:
    b=b+a
  a=a-1
print(b)
  
#6078
a=input()
while(a!='q'):
  print(a)
  a=input()
print(a) 
  
#6079
a=int(input())
b=0
i=0
while(b<a):
  i=i+1
  b=b+i
print(i)
  
#6080
a,b=input().split()
a,b=int(a),int(b)

for i in range(1,a+1):
  for j in range(1,b+1):
    print(i,j)
  
  
  
  
  
  
  
  
  
  
  






