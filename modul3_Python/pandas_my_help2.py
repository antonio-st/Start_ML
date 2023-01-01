 
 #загрузить файл excel
 Macro = pd.read_excel("macrofeatures.xlsx", engine="openpyxl")

 # вывести типы колонок
df.dtypes
 
 #вывести n первых и последних значений
taxiDB.head()

#вывести подробное инфо о DF
lesson5.info() 
#размерность DF
data.shape  

df.describe() #среднее, медиана и прочие параметры по всем колонкам

#Проверьте, сколько всего строк и столбцов имеется в датасете.
taxi.shape
rows, cols = taxi.shape
print(f'rows = {rows}, {cols = }')


 #сортировка по кол-ву значений
taxiDB['store_and_fwd_flag'].value_counts()


 # перевод в значение времени
taxiDB['pickup_datetime'] = pd.to_datetime(taxiDB['pickup_datetime'])


 #вычитаем разность времени и переводим в секунды
taxiDB['trip_duration'] = (taxiDB['dropoff_datetime']-taxiDB['pickup_datetime']).dt.seconds

### Выделим месяц запуска проекта
data['Срок'] = (data['Дедлайн'] - data['Дата публикации']).dt.days

### Выделим год запуска проекта
data['Год публикации'] = data['Дата публикации'].dt.year
#перевести тип кологки в дата
data['Дата публикации'] = data['Дата публикации'].astype('datetime64[ns]')


 #удаление 1 столбца
taxiDB = taxiDB.drop(['dropoff_datetime'], axis=1)

#удалить 4 столбца
taxiDB = taxiDB.drop(['pickup_longitude', 'dropoff_longitude',
                      'pickup_latitude', 'dropoff_latitude'], axis=1)



#найти все значения "N" и заменить их на 0
taxiDB.loc[taxiDB['store_and_fwd_flag'] == 'N','store_and_fwd_flag'] = 0

#найти все значения "N" и заменить их на 0 и сохранить в столбце 'таргет1'
taxiDB.loc[(taxiDB['store_and_fwd_flag'] == 'N'), 'таргет1'] = 0

#найти все значения Nan и заполнить их 1
taxiDB['таргет1'] = taxiDB['таргет1'].fillna(1)



#вывести 10 первых значений и сохранить в csv , разделитель ";"
lesson5 = taxiDB[:9]
lesson5.to_csv('taxiDB_l5.csv', sep=';')

#вывести из столбца df только те элементы которые  = 1
taxiDB[taxiDB['store_and_fwd_flag'].isin([1])]

#перезаписать колонку в df, оставить только значения  = Y и N
taxiDB = [taxiDB['store_and_fwd_flag'].isin(['Y', 'N'])]

#переименовать колонку
taxiDB = taxiDB.rename({'store_and_fwd_flag': 'таргет'}, axis=1)

#удалить дубли в колонках
Macro = Macro[['Close_brent', 'dlk_cob_date']].drop_duplicates()

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


#------------------ запросы, аналог фильтров или SQL
taxi.query('borough == \'Queens\' or  borough == \'Manhattan\'')
taxi.query('pickups < 1000 and borough == \'Manhattan\'')

#сколько раз в данных встречается район Бруклин (Brooklyn)
taxi.query("borough == 'Brooklyn'").shape[0]

#аналог like в SQL
taxi.query('pickups < 1000 and pickup_month.str.contains(\'Ja\')')

#------------------ 

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


#------------------ найти уникальные бренды pd.Series.nunique
#--------- nunique – метод, который считает число уникальных значений в колонке.

users_unique_brands = user_df.groupby('user_id', as_index=False) \
    .agg({'brand_name': pd.Series.nunique}) \
    .rename(columns={'brand_name': 'unique_brands'})


'''
Индекс и имена колонок

Индекс – это лэйбл строки в таблице, по умолчанию является её номером. А имена колонок... это имена колонок, то есть лэйблы, по которым мы можем обращаться к каждому из столбцов.

У датафрэйма есть два атрибута – index и columns.  Они позволяют получить доступ к соответствующей информации в виде array (на самом деле не совсем array).

df.index
df.columns

'''

#------------------ Поиск пустых значений
#---- isna – это чудо-метод, с помощью которого можно быстро найти пропущенные значения в датафрэйме.
df.isna()
df.isna().sum() # сумма пустых значений

