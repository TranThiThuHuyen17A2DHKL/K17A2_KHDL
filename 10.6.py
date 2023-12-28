a=int(input("nhập số a: "))
b=int(input("nhập số b: "))
c=int (input("nhập số c: "))
if a==0:
    print("phương trình có nghiệm x= ",-c/b)
else:
    delta=b**2-(4*a*c)    
    if delta==0:
        print("phương trình có nghiệm duy nhất= ",-b/2*a)
    elif delta>0:
        print ("phương trình có nghiệm x1= ",(-b-delta)**0,5/2*a)
        print ("phương trình có nghiệm x2= ",(-b+delta)**0,5/2*a)   
    else:
        print("phương trình vô nghiệm")    