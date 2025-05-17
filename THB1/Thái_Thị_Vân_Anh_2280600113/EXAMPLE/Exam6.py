#Câu lệnh điều kiện
x = 10
if x > 5: 
    print("x lớn hơn 5")
elif x == 5:
    print("x bằng 5")
else:
    print("x nhỏ hơn 5")

#vòng lặp for
fruits = ["apple", "banana", "cherry"] 
for fruit in fruits:
    print(fruit)

#vòng lặp While
count = 0
while count < 5:
    print(count)
    count +=1

#break
#tìm số chia hết cho 5 đầu  tiên trong khoảng từ 1 đến 100
for i in range(1, 1001):
    if i % 5 == 0:
        print("số chia hết cho 5 đầu iên là:", i)
        break 

#continue
#in các số chẵn từ 1 đến 10 và bỏ qua các số lẻ
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)
    
#pass
# kiểm tra điều kiện, nếu đúng thực hiện, néu sai thì không làm gì
x = 5
if x > 10:
    print("x lớn hơn 10")
else:
    pass

