type()  # тип переменной

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
