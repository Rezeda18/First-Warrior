k1 = input("Введите пароль ")

if len(k1)<5:
    print("Пароль слишком короткий")
else:
    k2 = input("Введите еще раз чтобы подтвердить ")
    if k2 != k1:
        print("Неправильное подтверждение")
    else:
        print("Пароль записан")