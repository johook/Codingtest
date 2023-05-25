total=0
for i in range(5):

  go,leave=input().split()
  go_h,go_m=go.split(':')
  leave_h,leave_m=leave.split(':')
  go_h,go_m,leave_h,leave_m=int(go_h),int(go_m),int(leave_h),int(leave_m)

  daytime=(leave_h-go_h)*60+(leave_m-go_m)
  total+=daytime
print(total)
