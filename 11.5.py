a=[]
while True:
    b=int(input("nhập b: "))
    a.append(b)
    c=int(input("Tiếp tục nhập giá trị? 1:Có 0:Không"))
    if c==1:
        continue
    else :
        break
print("list: ",a)    
def kiem_tra_so_nguyen_to(x):
 if x<2:
    return False
 else:
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
         return False
    return True
d=[]
e=[]
f=[]
for i in a:
    if kiem_tra_so_nguyen_to(i):
        d.append(i)
    if i<0:
        e.append(i)
    if i>0:
        f.append(i)
if len(d)!=0:
    print('các số nguyên tố trong list:',d)
else:
    print('không có số nguyên tố trong list')
if len(e)!=0:
    print('các phần tử âm trong list:',e)
    print('trung bình cộng các số âm:',sum(e)/len(e))
else:
    print('không có phần tử âm trong list')
if len(f)!=0:
    print('các phần tử dương trong list:',f)
    print('trung bình cộng các số dương:',sum(f)/len(f))
else:
    print('không có phần tử dương trong list')
# tìm giá trị lớn nhất,lớn nhất    
print(" giá trị lớn nhất: ",max(a))    
print("gía trị nhỏ nhất: ",min(a))
# giá trị tăng dần
a.sort
print("giá trị tăng dần: ",a)
