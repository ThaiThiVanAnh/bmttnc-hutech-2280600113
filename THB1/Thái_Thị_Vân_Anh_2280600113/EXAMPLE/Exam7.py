#khai báo chuôi xtrong python
#sử dụng dấu ngoặc đơn
string_single_quotes = 'Đây là một chuỗi sử dụng dấu ngoặc đơn.'
#sử dụng dấu ngoặc kép
string_single_quotes = "Đây là một chuôic sử dụng dấu ngoặc kép."
#Sử dụng dấu ngoặc ba
string_single_quotes = '''Đây là một chuôic sử dụng dấu ngoặc ba,
có thể trải dài 
qua nhiều dòng.'''

#Truy cập ký tự trong chuỗi
my_string = "Hello, Van Anh!"
print(my_string[0]) # KQ: "H"
print(my_string[8]) #KQ: "a"

#Cắt chuỗi
my_string = "Hello, Van Anh!"
print(my_string[3:]) # Lấy từ ký tự thứ 3 đến hết KQ: "lo, Van Anh!"
print(my_string[:8]) # Lấy từ đầu đến ký tự thứ 7 KQ: "Hello, V"
print(my_string[2:6]) # Lấy từ ký tự thứ 2 đến ký tự thứ 5 KQ: "llo,"

#Ghép chuỗi
string1 = "Hello"
string2 = "Van Anh"
concatenated_string = string1 + " " + string2 #KQ: 'Hello Van Anh'

# Độ dài chuỗi
my_string = "Hello, Van Anh!"
length = len(my_string) #KQ: 15

#Hàm dùng để xử lý chuỗi
my_string = "   Hello, Van Anh!   "
print(my_string.strip()) # loại bỏ khoảng trắng

my_string = "Hello, Van Anh!"
print(my_string.split(",")) #phân tách chuỗi

my_string = "Hello, Van Anh!"
print(my_string.replace("Hello", "Hi")) # Thay thế chuỗi

#khai báo hàm
def my_fuction(parameter1, parameter2):
    #khối mã của hàm
    #thực hiện các hoạt động dựa trên tham số được truyền vàp
    result = parameter1 + parameter2
    return result

#Gọi hàm
result = my_fuction(10, 20) #Gọi hàm và lưu kq vào biến result
print(result)

#Khai báo và gọi hàm
#Định nghĩa hàm tính tổng
def calclate_sum(a, b):
    result = a + b
    return result
#Gọi hàm và lưu kq vào biến
sum_result = calclate_sum(10, 20)
#in kq
print("tổng hai số là:", sum_result)

#khai báo hàm không có giá trị trả về
#hàm không có tgia strij trả về, chỉ in ra thông báo
def greet(name):
    print("Xin chào,", name)
#gọi hàm
greet ("Van Anh")
