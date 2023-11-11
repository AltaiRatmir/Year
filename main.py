import calendar

years = ['Год Крысы', 'Год Быка', 'Год Тигра', 'Год Кролика', 'Год Дракона', 'Год Змеи',
         'Год Лошади', 'Год Козы', 'Год Обезьяны', 'Год Петуха', 'Год Собаки', 'Год Кабана']

def main_fun():
    year = int(input('Введите год: '))
    print(years[abs(year - 1936) % 12], end='. ')
    if calendar.isleap(year):
        print('Год високосный.')
    else:
        print('Год не високосный.')

main_fun()

while input('Для завершение работы программы, введите <n>: ').lower() != 'n':
    main_fun()