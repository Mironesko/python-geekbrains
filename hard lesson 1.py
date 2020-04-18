
name = input('Введите ваше Имя: ')
age = int(input('Введите ваш возраст: '))
weight = int(input('ВВедите ваш вес '))

if age <= 30 and 50 <= weight >= 120:
    print('Вы вы отличной форме ', name, age)
elif age > 40 and (weight < 50 or weight > 120):
    print('Вам бы к врачу')
elif age > 30 and (weight < 50 or weight > 120):
    print('Вам бы спортом заняться')
else:
    print(' я работаю только по определенным данным')