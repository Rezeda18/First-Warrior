c1 = input('1 цвет ')
c2 = input('2 цвет ')

q = 'желтый'
w = 'красный'
e = 'синий'

if (c1 == w or c2 == w) and (c1 == e or c2 == e):
    print('фиолетовый')
if (c1 == w or c2 == w) and (c1 == q or c2 == q):
    print('оранжевый')
if (c1 == e or c2 == e) and (c1 == q or c2 == q):
    print('зеленый')