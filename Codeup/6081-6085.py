#6081
n = int(input(), 16)

for i in range(1, 16) :
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
  
#6083
a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
count=0

for i in range(0,a):
  for j in range(0,b):
    for k in range(0,c):
      print(i,j,k)
      count+=1
print(count)

#6084
h,b,c,s=input().split()
h,b,c,s=int(h),int(b),int(c),int(s)
k=h*b*c*s/8/1024/1024
print(round(k,1),"MB")
  
#6085
h,b,c=input().split()
h,b,c=int(h),int(b),int(c)
k=h*b*c/8/1024/1024
print(round(k,3),"MB")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
