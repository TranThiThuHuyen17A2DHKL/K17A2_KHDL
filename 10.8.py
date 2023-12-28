import calendar
nam=int(input("nhập năm: "))
thang=int (input("nhập tháng: "))
ngay=int(input("nhập ngày: "))
print("ngày tháng vừa nhập: ",ngay,thang,nam)
# kiểm tra năm nhuận
print(calendar.isleap(nam))
# tháng có bao nhiêu ngày
print(calendar.monthcalendar(nam,thang))
# ngày vào thứ mấy
print( calendar.weekday(nam,thang,ngay))
