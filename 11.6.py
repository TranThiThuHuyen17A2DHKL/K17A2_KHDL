list=[1.8796,1.8796,1.8288,1.8288,1.8542,1.7526,1.7526,1.8034,1.9304,1.8034]
# in ra 3 chiều cao đầu tiên ,3 chiêuf cao cuối cùng
print(list[0:3])
print(list[-3:])
#in ra chiều cao trung bình,chiều cao lớn nhất, chiều cao nhỏ nhất
print("chiều cao lớn nhất là: ",max(list))
print("chiều cao nhỏ nhất là: ",min(list))
n=sum(list)/len(list)
print("chiều cao trung bình là: ",round(n,3))
# sắp xếp tăng dần
list.sort()
print("sắp xếp theo chiều tăng dần: ",list)
# sắp xếo giảm dần
list.sort()
list.reverse()
print("sắp xếp theo chiều giảm dần: ",list)