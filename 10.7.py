s="a 2 3 4 5 cat tiger"
s_sub="3"
s_find="tiger"
s_replace="dog"
# in chuỗi s;
print (s)
#loại bỏ khoảng trắng ở dầu cuối:
print(s.strip())
#in chuỗi với ký tự đầu cuối viết hoa:
print(s.capitalize())
# đếm và in số lần chuỗi con s_sub :
print(s.count("3"))
# tìm kiếm và thay thế:
print(s.find(s_find,0,30))
print(s.replace("cat","dog",))




