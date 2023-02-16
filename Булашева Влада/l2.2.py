yer = int(input("Введите год:"))
if yer%4==0 and yer%100!=0:
    print("Год ", yer, " - високосный")
else:
    print("Этот год не високосный")
if yer%400==0:
    print("Год ", yer, " - високосный")
