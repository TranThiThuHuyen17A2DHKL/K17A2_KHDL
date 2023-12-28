def hoan_hao(n,s):
    if n<=0:
        return False
    s=0
    for i in range(1,n-1):
        if n%i==0: 
            s+=i
            return s==n
        


# kiểm tra số hoàn hảo
so=int(input('nhập số n: '))
if so==1:
    print("1 là số hoàn hảo")    
elif hoan_hao(so) :
       print(so,"là số hoàn hảo")
else:
     print(so,"không phải là số hoàn hảo")       
    



