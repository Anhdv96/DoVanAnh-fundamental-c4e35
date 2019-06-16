#Bài 1:
#Để phân biệt các dạng biến nhờ dấu ngoặc kép
#Để đặt tên biến hợp lệ thì sẽ bắt đầu bằng chữ số nguyên hoăc các ký tự thường cái bằng chuỗi là các chuỗi kí tự thì phải đặt trong dấu ngoặc kép, trong khi số nguyên thì không 
#Nếu tạo một biến không hợp lệ thì sẽ bị báo lỗi syntaxError (từng đơn lẻ kí tự có thể dùng ‘’ nhưng dùng cá chuỗi kí tự nên để dạng “”) sẽ chánh sai sót
#Ví dụ sai như
#Đặt tên biến trùng từ khóa của python như def, if, while
#Kí tự đặc biệt: %ba
#Bắt đầu đặt tên biến bằng dấu gạch dưới: _n 

#Bài 2:
r = int(input("radius r:"))
print("area = " ,3.14*r*r)

#Bài 3:
c = int(input('temperature in Celsius: '))
f = c*1.8+32
print(c,'(C) = ',f,'(F)')
