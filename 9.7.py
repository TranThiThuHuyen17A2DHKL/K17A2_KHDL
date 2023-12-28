def phan_nguyen_phep_chia (a,b):
    if b==0:
        print("Lỗi: Không thể chia cho 0 ")
        return None
    else:
        return a//b
        
# nhập số và kiểm tra
a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
ket_qua=phan_nguyen_phep_chia(a,b)
if ket_qua is not None:
    print(f"Phần nguyên của a chia b là:{ket_qua}")
    
    
