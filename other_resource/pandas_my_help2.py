# версия пакета
pd.__version__

#----------------------архивация--------------------------------

!tar -zcvf train.tar.gz train.csv

tar -xvf archive.tar.gz или tar -zxvf archive.tar.gz

#----------------------ИМПОРТ И ЗАГРУЗКА ДАННЫХ--------------------------------

import pandas as pd
# считали данные из файла в DataFrame

df = pd.read_csv('train.csv') 

# можно сразу указать тип колонки 
df = pd.read_csv('train.csv', dtype={'season': int}) 

 
 #загрузить файл excel
df = pd.read_excel("macrofeatures.xlsx", engine="openpyxl")


# установить число колонок
pd.options.display.max_columns = 500

#------------------------------------------------------

 # вывести типы колонок
df.dtypes
 
#вывести подробное инфо о DF, похоже на dtypes
df.info()  
 
 #вывести n первых и последних значений
df.head()



#размерность DF / Проверьте, сколько всего строк и столбцов имеется в датасете.
df.shape  

df.describe() #среднее, медиана и прочие параметры по всем колонкам
### Посмотрим на категориальные колонки
df.describe(include='object')

rows, cols = df.shape
print(f'rows = {rows}, {cols = }')


 #сортировка по кол-ву значений
df['store_and_fwd_flag'].value_counts()


 # перевод в значение времени
df['columns'] = pd.to_datetime(df['columns'])


 #вычитаем разность времени и переводим в секунды
df['trip_duration'] = (df['dropoff_datetime']-df['pickup_datetime']).dt.seconds

### Выделим месяц запуска проекта
data['Срок'] = (data['Дедлайн'] - data['Дата публикации']).dt.days

### Выделим год запуска проекта
data['Год публикации'] = data['Дата публикации'].dt.year
#перевести тип кологки в дата
data['Дата публикации'] = data['Дата публикации'].astype('datetime64[ns]')


 #удаление 1 столбца
df = df.drop(['dropoff_datetime'], axis=1)

#удалить 4 столбца
df = df.drop(['pickup_longitude', 'dropoff_longitude',
                      'pickup_latitude', 'dropoff_latitude'], axis=1)


### удалить столбцы в которых число пропусков превысит 15%

df = df.dropna(thresh=int(len(df) * .85), axis=1)


#----------------------ФИЛЬТРАЦИЯ --------------------------------



#найти все значения "N" и заменить их на 0
df.loc[df['store_and_fwd_flag'] == 'N','store_and_fwd_flag'] = 0

#найти все значения "N" и заменить их на 0 и сохранить в столбце 'таргет1'
df.loc[(df['store_and_fwd_flag'] == 'N'), 'таргет1'] = 0

#------------------------------------------------------
# фильтрации
# по значению
df[(df['workingday'] == 1) & (df['season'] == 1)]

# аналог фильтрации через query
df.query('workingday == 1 and season == 1')

# аналог фильтрации через loc
df.loc[(df.workingday == 1) & (df.season == 1)]

#найти все значения Nan в столбце таргет1 и заполнить их 1
taxiDB['таргет1'] = taxiDB['таргет1'].fillna(1)

#------------------------------------------------------

#------------------ запросы, аналог фильтров или SQL
df.query('borough == \'Queens\' or  borough == \'Manhattan\'')
df.query('pickups < 1000 and borough == \'Manhattan\'')

#сколько раз в данных встречается район Бруклин (Brooklyn)
df.query("borough == 'Brooklyn'").shape[0]

#аналог like в SQL
df.query('pickups < 1000 and pickup_month.str.contains(\'Ja\')')

#------------------ 

'''
Индекс и имена колонок
Индекс – это лэйбл строки в таблице, по умолчанию является её номером. А имена колонок... это имена колонок, то есть лэйблы, по которым мы можем обращаться к каждому из столбцов.
У датафрэйма есть два атрибута – index и columns.  Они позволяют получить доступ к соответствующей информации в виде array (на самом деле не совсем array).
df.index
df.columns
'''

# прямое обращение по индексу через .loc
df.loc[4]
# обратиться к 'temp' индексу элементу предыдущего вывода
df.loc[4]['temp'] 

# слайс для df по index
df[4:5] 

#------------------------------------------------------


# ---- сделать индекс колонкой
taxiDB.set_index('id')



# -------------- apply и lambda --------------------
# отобрать записи, у которых более 20 категорий
data[data.categories.str.split(',').apply(lambda x: len(x) > 20)]



#------------------ Поиск пустых значений ----------------
# isna – это чудо-метод, с помощью которого можно быстро найти пропущенные значения в датафрэйме.
df.isna()
df.isna().sum() # сумма пустых значений
isna().any().any() # поиск пустых значений по всему df


#------------------
# количество уникальных значений
df.App.nunique()

# количество не null
df.Rating.notna().sum()

# убрать дубликаты / сбросить индекс
df.drop_duplicates(subset=['App']).reset_index(drop=True)


# убрать дубликаты / вывести долю
df.drop_duplicates(subset=['app']).type.value_counts(normalize=True)



# найдем заведения Taco Bell или заведения, которые находятся в городе Нью-Йорк.
# При этом обязательно, чтобы в названии меню не было Volcano Taco и Fresco Soft Taco
result = data[( (data['name'] == 'Taco Bell') | (data['city'] == 'New York') ) \
     & ( ~ data['menus.name'].isin(['Volcano Taco', 'Fresco Soft Taco'])  )]




#вывести из столбца df только те элементы которые  = 1
df[df['store_and_fwd_flag'].isin([1])]

#перезаписать колонку в df, оставить только значения  = Y и N
df = [df['store_and_fwd_flag'].isin(['Y', 'N'])]

#переименовать колонку
df = df.rename({'store_and_fwd_flag': 'таргет'}, axis=1)

#удалить дубли в колонках
df = df[['Close_brent', 'dlk_cob_date']].drop_duplicates()

#  удалить дубли в колонке, subset + сброс индексов

unique_playstore = playstore.drop_duplicates(subset=['App']).reset_index(drop=True)


#сортировка по столбцу
data = data.sort_values('Дата публикации')







#----------------Объединение датафрэймов, JOIN

# - вариант 1
data =    (Macro,
         left_on=['Дата публикации'],
         right_on=['dlk_cob_date'],
         how='left')
 
# --- вариант 2 (3 таблицы)
loyalty_df = users_purchases \
    .merge(users_unique_brands, on='user_id') \
    .merge(lovely_brand_purchases_df, on='user_id')


# -------Здесь мы объединяем датафрэйм users_data с датафрэймом users_lovely_brand_data по колонке tc с помощью inner джойна:
user_data.merge(users_lovely_brand_data, how='inner', on='tc')


# ------- concat объеденить несколько df или можно несколько строк с текущего df вырезанных слайсами

s1 = df[:3].copy()
s2 = df[5:8].copy()
s3 = df[15:19].copy()

df_concat = pd.concat([s1, s2, s3])[['App', 'Size', 'Genres', 'Current Ver']] # так же выбираем определенные столбцы

# или




#----------------------------

#------------------распарсить строку на слова и взять последний и записать в столбец
def split_brand(brand_name_data):
    return brand_name_data.split(' ')[-1]

user_df['brand_name'] = user_df.brand_info.apply(split_brand)

#аналог в одну строчку через lambda функции
user_df['brand_name'] = user_df.brand_info.apply(lambda x: x.split(' ')[-1])

#------------------группировка, аггр-я по кол-ву, переименование, запрос


users_purchases = user_df.groupby('user_id', as_index=False) \
    .agg({'brand_name': 'count'}) \
    .rename(columns={'brand_name': 'purchases'}) \
    .query('purchases >= 5')


#------------------ найти уникальные бренды pd.Series.nunique
#--------- nunique – метод, который считает число уникальных значений в колонке.

users_unique_brands = user_df.groupby('user_id', as_index=False) \
    .agg({'brand_name': pd.Series.nunique}) \
    .rename(columns={'brand_name': 'unique_brands'})


#------------------поиск уникальных брендов на пользователя

users_unique_brands = user_df.groupby('user_id', as_index=False) \
    .agg({'brand_name': pd.Series.nunique}) \
    .rename(columns={'brand_name': 'unique_brands'})

#------------------выделение любимого бренда
lovely_brand_purchases_df = user_df.groupby(['user_id', 'brand_name'], as_index=False) \
    .agg({'brand_info': 'count'}) \
    .sort_values(['user_id', 'brand_info'], ascending=[False, False]) \
    .groupby('user_id') \
    .head(1) \
    .rename(columns={'brand_name': 'lovely_brand','brand_info': 'lovely_brand_purchases'})



#idxmin – индекс минимального значения
min_pickups = taxi.groupby('borough').pickups.sum().idxmin()

#idxmax – индекс максимального значения
max_pickups = taxi.groupby('borough').pickups.sum().idxmax()

#------------------ .to_frame()

#вариант с выводом во фрэйм .to_frame()
taxi.groupby(['borough', 'hday'])\
            .pickups.mean()\
            .to_frame() 

#------------------сохранить файл с датой в имени
from datetime import datetime
    today_day = datetime.today().strftime('%Y-%m-%d')
    file_name = 'money_title_{}.csv'
    file_name = file_name.format(today_day)    
    
    if int(money_title.money.sum()) == int(all_money):
        print('OK! File {} is written.'.format(file_name))
        money_title.to_csv(file_name, index=False)
    else:
        print('ERROR!')  
        
    return money_title

#-----OK! File money_title_2020-05-17.csv is written.

#------------------
# преобразовать имена колонок в маленькие буквы
# заменить пробелы на _

#------1 способ
bookings.columns = bookings.columns.str.lower()\
                            .str.replace(' ', '_', regex=True)

#------2 способ
rename_cols = {}
for col in bookings.columns:
    rename_cols[col] = col.replace(' ', '_').lower()

bookings = bookings.rename(columns=rename_cols)


#------------------ аггрегация с помощью pd.Series.mode
bookings.groupby('arrival_date_year', as_index=False)\
        .arrival_date_month.agg(pd.Series.mode)


#------------------ 
# создайте переменную has_kids, которая принимает значение True, 
# если клиент при бронировании указал хотя бы одного ребенка (total_kids), в противном случае – False.

# вариант 1 - с помощью функции
def has_kids(x):
    if x > 0:
        return True
    else:
        return False
    
bookings['has_kids'] = bookings.total_kids.apply(has_kids)

# вариант 2
bookings['has_kids'] = bookings.total_kids.astype(bool)
bookings.has_kids.value_counts()

#------------------ Анонимные функции
# Один из примеров использования лямбда-функции – переименование колонок в датафрэйме. Здесь мы делаем их заглавными и заменяем #  дефисы на нижние подчёркивания.


df = df.rename(columns=lambda c: c.upper().replace('-', '_'))

#------------------ разбить строку на слова

brnad_name = 'MARAVILLA 500 G Store_Brand'
brnad_name.split(' ')[-1] #последнее слово

#--'Store_Brand'


#------------------  разбить текст в колонке на слова и записать последнее в другую колонку
#---------apply – применяет переданную в него функцию ко всем колонкам вызванного датафрэйма. Чтобы применить функцию к одной #--------- колонке датафрэйма, можно выбрать её перед применением apply

def split_brand(brand_name_data):
    return brand_name_data.split(' ')[-1]

user_df['brand_name'] = user_df.brand_info.apply(split_brand)


#------------------ ГРАФИКИ

# --Самый простой способ визуализировать данные – вызвать метод plot у датафрэйма (или его колонки). Например, гистограмма значений в колонке orders :

user_data.orders.plot('hust', bins=15)
#--Здесь bins – это число диапазонов (корзин или бакетов), на которые мы разделяем значения.

#------------------ график с разбиением на категории
ax = sns.distplot(loyalty_df.loyalty_score, kde=False)

# встроенный график pandas
df.plot(
    xlabel='Номер недели',
    ylabel = 'Средняя $t^o$',
    title='Средняя температура еженедельно',
    grid=True,
    figsize=(9,5)
)

# гистограмма /встроенный график pandas
df['temp'].hist(figsize=(9,5), bins=100)


# ------------------ СОХРАНЕНИЕ В ФАЙЛ ------------------

#CSV
#вывести 10 первых значений и сохранить в csv , разделитель ";", не сохранять индексы
lesson5 = taxiDB[:9]
lesson5.to_csv('taxiDB_l5.csv', sep=';', index=False)  


#Excel
!pip install openpyxl
#запись в файл
df.to_excel('rents_by_week.xlsx', engine='openpyxl')

# ------------------ ------------------


# ------------------Сводная таблица pandas ------------------

# пример pd.pivot
pivot_ps = pd.pivot_table(df, index=['category', 'type'], values=['price', 'rating', 'reviews']
# переименовать колонку                        
pivot_ps.rename(columns={'price': 'mean_price', 
                         'rating': 'mean_rating',
                         'reviews': 'mean_reviews'})
# округлить значения в колонке
pivot_ps['mean_price'] = pivot_ps['mean_price'].round(2)
# ------------------ ------------------


# ------------------Работа с таргетом ------------------

# прологарифмировали таргетную переменную и вставили в новый столбец

df = df.assign(log_price_doc = np.log1p(df['price_doc']))

# ------------------Работа с пропусками ------------------

### Посмотрим на некатегориальные колонки и категориальные (записали в переменную)
numeric_columns = df.loc[:,df.dtypes!=np.object_].columns
categorical_columns = df.loc[:,df.dtypes==np.object_].columns

# аналог (передавая необходимый тип данных как аргумент в include, exclude исключить тип)
df.select_dtypes(include=object).columns
df.dtypes[df.select_dtypes(exclude=object).columns]


# заполняем пропуски средним значением (прошли в цикле по каждой колонке , вычислили среднее, и записали в качестве Nan)
for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())



# ### Закодируем колонку с годом через One-Hot

one_hot = pd.get_dummies(df['month'], prefix='month', drop_first=True)
df = pd.concat((df.drop('month', axis=1), one_hot), axis=1)

### ohe, в случае если категорий меньше 5

for col in categorical_columns:
    if col != 'timestamp': 
        if df[col].nunique() < 5:
            one_hot = pd.get_dummies(df[col], prefix=col, drop_first=True)
            df = pd.concat((df.drop(col, axis=1), one_hot), axis=1)

        else:
            mean_target = df.groupby(col)['log_price_doc'].mean()
            df[col] = df[col].map(mean_target)


# ------------------ Квантиль (quantile) - 
# число, которое заданная случайная величина не превышает с фиксированной вероятностью. 
# Например, 0,025-квантиль – число, ниже которого лежит примерно 2,5% выборки


top_quantile = data['log_price_doc'].quantile(0.975)
low_quantile = data['log_price_doc'].quantile(0.025)
