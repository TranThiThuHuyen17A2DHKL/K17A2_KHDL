r=int (input("nhập ban kính: "))
a=int(input("nhập chiều dài: "))
b=int(input("nhập chiều rộng: "))
import math
p=lambda r:2*3.14*r
s=lambda r: 3.14*(r**2)
P=lambda a,b:(a+b)*2
S=lambda a,b:a*b
print("chu vi hình tròn ",p(r))
print("diện tích hình tròn ",s(r))
print("chu vi hình chữ nhật ",P(a,b))
print("diện tích hình chữ nhật ",S(a,b))