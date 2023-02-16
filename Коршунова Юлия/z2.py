n = int(input("Номер? "))

if n % 2 == 0 and n in range(1, 37):
    print('Верх')
if n % 2 != 0 and n in range(1, 37):
    print('Низ')

if n % 2 == 0 and n in range(37, 55):
    print('Верх боковушки')
if n % 2 != 0 and n in range(37, 55):
    print('Низ боковушки')

if n >54:
    print('Неправильный номер')