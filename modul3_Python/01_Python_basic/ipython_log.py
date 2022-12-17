# IPython log file

print('генерируем четные числа')
even_numbers = []

for i in range(0, 20, 2):
    even_numbers.append(i)
print('генерируем четные числа')
even_numbers = []

for i in range(0, 20, 2):
    even_numbers.append(i)
print(even_numbers)
number  = 34624

while number % 2 == 0:
    print(f'{number % 2} делиться на 2')
    number //= 2
print(number)
number  = 34624

while number % 2 == 0:
    print(f'{number} делиться на 2')
    number //= 2
print(number)
print('Считаем, сколько раз число делится на 2')
number  = 34624
while number % 2 == 0: # пока условие истинно - выполняется цикл
    print(f'{number} делиться на 2')
    number //= 2 # действие для выхода из цикла , равнозначно number = number // 2
print(number)
get_ipython().run_line_magic('time', '')
print('Считаем, сколько раз число делится на 2')
number  = 34624
while number % 2 == 0: # пока условие истинно - выполняется цикл
    print(f'{number} делиться на 2')
    number //= 2 # действие для выхода из цикла , равнозначно number = number // 2
print(number)
get_ipython().run_line_magic('time', '')
get_ipython().run_line_magic('logstart', '')
print('Считаем, сколько раз число делится на 2')
number  = 34624
while number % 2 == 0: # пока условие истинно - выполняется цикл
    print(f'{number} делиться на 2')
    number //= 2 # действие для выхода из цикла , равнозначно number = number // 2
print(number)
get_ipython().run_line_magic('pwd', '')
print('Считаем, сколько раз число делится на 2')
number  = 34624
while number % 2 == 0: # пока условие истинно - выполняется цикл
    print(f'{number} делиться на 2')
    number //= 2 # действие для выхода из цикла , равнозначно number = number // 2
print(number)
get_ipython().run_line_magic('mprun', '')
print('Считаем, сколько раз число делится на 2')
number  = 34624
while number % 2 == 0: # пока условие истинно - выполняется цикл
    print(f'{number} делиться на 2')
    number //= 2 # действие для выхода из цикла , равнозначно number = number // 2
print(number)
get_ipython().run_line_magic('who', '')
print('Считаем, сколько раз число делится на 2')
number  = 34624
while number % 2 == 0: # пока условие истинно - выполняется цикл
    print(f'{number} делиться на 2')
    number //= 2 # действие для выхода из цикла , равнозначно number = number // 2
print(number)
get_ipython().run_line_magic('who', '')
## `Условный оператор IF`
> выполняем код в зависимости от условия
number = 4
if number % 2 == 0:
    print('Число четное')
else:
    print('Число нечетное')
# поищем счета с отрицательным балансом:

accounts_balance = [1482.0, 28182.12, -124.42, 85.3, -23.5, 82]  # входные данные
negative_accounts = []

for balance in accounts_balance:
    if balance < 0:
        print(f'{balance} отрицателен, записываем в ответ')
        negative_accounts.append(balance)
    print(f'закончили обрабатывать {balance}')
# поищем счета с отрицательным балансом:

accounts_balance = [1482.0, 28182.12, -124.42, 85.3, -23.5, 82]  # входные данные
negative_accounts = []

for balance in accounts_balance:
    if balance < 0:
        print(f'{balance} отрицателен, записываем в ответ')
        negative_accounts.append(balance)
    print(f'закончили обрабатывать {balance}')
print(negative_accounts)
# поищем счета с отрицательным балансом:

accounts_balance = [1482.0, 28182.12, -124.42, 85.3, -23.5, 82]  # входные данные
negative_accounts = []

for balance in accounts_balance:
    if balance < 0:
        print(f'{balance} отрицателен, записываем в ответ')
        negative_accounts.append(balance)
    print(f'закончили обрабатывать {balance}')
print(f'отрицательные балансы {negative_accounts}')
name = input('Введите название столицы > ')
if name == 'Москва':
    print('Столица России')
elif name == 'Минск':
    print('Столица Белоруссии')
elif name == 'Белград':
    print('Столица Сербии')
else:
    print('Нет в БД')
name = input('Введите название столицы > ')
if name == 'Москва':
    print('Столица России')
elif name == 'Минск':
    print('Столица Белоруссии')
elif name == 'Белград':
    print('Столица Сербии')
else:
    print('Нет в БД')
name = input('Введите название столицы > ')
if name == 'Москва':
    print('Столица России')
elif name == 'Минск':
    print('Столица Белоруссии')
elif name == 'Белград':
    print('Столица Сербии')
else:
    print('Нет в БД')
words = ['see', 'this', 'long', 'sentence', 'here', 'no-show', 'no-show']

for i in range(len(words)):
    print(words[i])
    if i > 2: # на третьем слове выходим из цикла по break
        break
