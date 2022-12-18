type()  # тип переменной
input() # ввод строки

# базовые операции
5 * 2
6 / 2
5 // 2  # деление нацело
5 % 2  # остаток от деления
9 ** 0.5  # конень квадратный

# ----------------------------

# Порядок вычисления булевых операторов
# операторы and, or, not

1. Скобки
2. not
3. and
4. or

5 >= 1  # больше, либо равно
1 <= 5  # меньше либо равно
10 != 20  # не равно
'el' != 'Anton'

# ---------------------------------------------------------------------

# Списки
my_list = [1, 2, 3, 5, 9, 12]

# len оператор возвращающий длину(списка)
len(my_list)

# сложение списков
new_list = my_list + ['a', 'b', 'c', 'd']

# добавление в конец списка
new_list.append('g')

# удалить и вывести элемент
print(new_list.pop())  # удалить последний элемент
print(new_list.pop(1))  # удалить 2 элемент списка

# удаление по символу
print(new_list)
new_list.remove('a')  # удалить символ a
new_list.remove(12)  # удалить число 12

# ----------------------------------------------------------------------
# Кортеж / Tuple


# можно складывать
my_tuple + (5, 6)

# создать кортеж с 1 элементом
new_tuple = (1,)

my_tuple[2]  # 3 элемент кортежа

# ----------------------------------------------------------------------

# Set / Множества
a = {2, 'a', 3.14}  # создание множества с элементами
b = set()  # создание пустого множества

a.add(3)  # добавить элемент в множество
a.remove(3.14)  # удалить элемент 3.14

''''
в set можно добавлять только неизменяемые объекты

+ пересечение множеств `a.intersection(b)`
+ объединение `a.union(b)`
+ симметрическую разность `a.symmetric_difference`

''''

a = {'a', (1, 2), 3}
b = {3, (1, 2), 'union'}

a.intersection(b)  # те элементы которые пересекаются
a.union(b)  # общие уникальные элементы обоих множеств
a.symmetric_difference(b)  # не пересекающиеся элементы множества

# вычитание множеств
print(a - b)  # те элементы которые есть в a, но их нет в b # {'a'}
print(b - a)  # те элементы которые есть в b, но их нет в a # {'union'}


# ----------------------------------------------------------------------
# Словари / dict
# ключ: значение
name_to_number = {
    'Антон': '9187592724',
    'Никита': '495123456'
}
print(name_to_number)

# получаем значение по ключу
name_to_number['Антон']

# безопасное получение данных по ключу (например , если такого элемента нет)
print(name_to_number.get('Никита'))
print(name_to_number.get('Ники'))  # ключ не найден, выводим 'None'

# можно вывести определенный текст, если элемент не найден
print(name_to_number.get('Мария', 'not found'))

# добавление по ключу
name_to_number['Владимир'] = '+7 8685 100'


# используем оператор in ,чтобы проверить есть ли такой ключ
print('Владимир' in name_to_number)

# редактирование элемента словаря по ключу
name_to_number['Никита'] = '+7812123456'


# ----------------------------------------------------------------------
# Условия и циклы

# цикл for

for a in [9, 16, 25, 36, 49]:
    print('считаем в цикле for')
    print(a ** 0.5 + 1)  # корень из элемента a + 1
print('Пишем после цикла')

# range  - генерирует числа от 0 до n-1 (start, stop, step)
print(*range(0, 11))
# ----------
print('генерируем четные числа')
even_numbers = []
# -------------
for i in range(0, 20, 2):
    even_numbers.append(i)
print(even_numbers)
# -------------

# f-string - возможность подстановки выражения в строку
for i in range(1, 11):
    print(f'Квадрат {i} = {i * i} ')

# ----------------------------------------------------------------------
# Цикл WHILE
# работает до тех пор, пока верно утверждение

print('Считаем, сколько раз число делится на 2')
number = 34624
while number % 2 == 0:  # пока условие истинно - выполняется цикл
    print(f'{number} делиться на 2')
    number //= 2  # действие для выхода из цикла , равнозначно number = number // 2
print(number)


# ----------------------------------------------------------------------
## `Условный оператор IF`
# выполняем код в зависимости от условия

number = 4
if number % 2 == 0:
    print('Число четное')
else:
    print('Число нечетное')

# elif (else if)


if name == 'Москва':
    print('Столица России')
elif name == 'Минск':
    print('Столица Белоруссии')
elif name == 'Белград':
    print('Столица Сербии')
else:
    print('Нет в БД')


# ----------------------------------------------------------------------
### `Ключевые слова break, continue`
# Дополнения к for и while: это команды break и continue. 
# Оба дают возможность выйти из цикла раньше задуманного.

#break

words = ['see', 'this', 'long', 'sentence', 'here', 'no-show', 'no-show']

for i in range(len(words)):
    print(words[i])
    if i > 2: # на третьем слове выходим из цикла по break
        break
    # вывод see this long sentence
    
    
# в случае вложенного цикла break выходит только из внетреннего

for i in range(5):
    for j in range(7):
        print(i, j)
        if j > 2:
            break
    print('Увеличиваем i')
    
# continue

# выводит не из всего цикла, а пропускает одну иттерацию

for future in ['make sandwitch', 'make coffee', 'watch TV', 'wash plate']:
    if future == 'make coffee':
        # пропустить 1 иттерацию в цикле
        print('Coffee mashine is broken, skipping :(')
        continue
        # если условие истинно, но continue гарантирует, что дальше цикл выполняться не будет.
    print(f'starting action: {future}')