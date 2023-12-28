def duong_tu_am(year) :
    int(input("Nhập năm dương lịch: "))
    can=["Canh","Tân","Nhâm","Quý","Giáp","Ất","Bính","Đinh","Mậu","Kỳ"]
    chi=["Thân","Dậu","Tuất","Hợi","Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi"]
    chi=can+chi
    if year%10 :
        print("can : ")
    elif year%12:
        print("chi: ")
    
    2017