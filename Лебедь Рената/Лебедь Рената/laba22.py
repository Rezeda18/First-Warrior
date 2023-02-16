a = int(input("Введите номер места"))
if a%2==0 and a<=36:
    print('Вверхнее место')
elif  a%2!=0 and a<=35:
    print('Нижнее место')
elif a%2!=0 and a>=37 and a<=54:
    print('Верхнее боковое место')
elif a%2==0 and a>=37 and a<=54:
    print('Нижнее боковое место')
else:
    print('Вы ошиблись')