#khai báo array
from array import array
#khai báo một mảng số nguyên
int_array = array('1', [1, 2, 3, 4, 5])
#khai báo một mảng số thực
float_array =array('f', [3.14, 2.5, 6.7])
print(int_array[0]) # truy cập phần tử đầu tiên của mảng số nguyên
print(float_array[2]) # Truy cập phần tử thứ 3 của mảng số thực
int_array[2] = 10 # cập nhật giá trị của phần tử thứ 3 trong mảng số nguyên
int_array.append(6) #thêm phần tử 6 vào cuối mảng số nguyên
float_array.remove(6.7) # Xoá phần tử 6.7 ra khỏi mảng số thực

#khai báo một ds
#ds số nguyên
my_list = [1, 2, 3, 4, 5]
#ds chuỗi
names = ["Van", "Anh", "ne"]
#ds kêt hợp kiểu dữ liệu
mixes_list = [10, "hello", 3,14, True]

print(my_list[0]) #truy cập phần tử đầu tiên 
print(names[2]) #truy cập phần tử thứ 3

my_list[1] = 20 #thay đổi gia strij của phần tử thứ 2
print(my_list)

names.append("Anh") # thêm phần tử vào cuối ds
print(names)

del my_list[2] #xoá phần tử thứ 3 khỏi ds
print(my_list)

