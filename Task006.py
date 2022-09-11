def Number():
    while True:
        try:
            num  = int(input('Введите число: '))
            return num
        except(ValueError):
                print('Вы ввели не число!')
numb = Number()

for i in range(numb):
    print((-3)**i, end=', ')