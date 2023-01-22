## 5 урок : библиотека Pandas
---

> Основные характеристики библиотеки
> Чтение файла
- pd.read_csv
  
> Беглый взгляд на данные
- .head() .tail()
- .describe()
- .columns
- .dtypes .info()
> Простые фильтрации
- По значению df[df['columns'] == 0]
> Логическое 'И' 
- df[(df['columns'] == 1) & (df['columns'] == 1)]
- доступ к строке с индексом df.loc[0] df.loc[0]["temp"]
> Логическое ИЛИ
- df[(df['columns'] < 50) | (df['columns'] > 30.)]
> Логическое НЕ
- df[~(df['columns'] == 1)]
> Функции-фильтры
- .isna() 
  - (df[df['columns'].isna()])
- .any()
- isin()
  - df[df['columns'].isin([1, 3, 4])]
> Series

> Index
- .loc
  - df.loc[4]
  - df.loc[4]['columns']
  - df_dt.loc['index', 'columns']
  - Перезапись DataFrame с .loc
    - df.loc['index', 'columns'] = 7.0 
- колонка - индекс
  - df_dt = df.copy().set_index('index')
- .iloc
  - df.iloc[4]
  - df_dt.iloc[4]['columns']
  - df.iloc[3:7]
- сброс индексов
  - df.reset_index(inplace=True) *изменяет df* 
  - df.reset_index(inplace=True)

> Группировка

- .groupby
  - df.groupby('columns', as_index=False).agg({'columns2': 'mean'})
  - по 2 параметрам: df.groupby(['columns1', 'columns2']).mean()
  - только для одной колонки: df.groupby(['columns1', 'columns2'],as_index=False)['columns3'].mean()

> Время и даты
- pd.datetime
  - преобразование даты :
    -  pd.to_datetime(df['columns'])
  - фильтрация по элементам
    - df.loc[df.columns.dt.month == 5]
  - группировка по дате
    - df.groupby(df['datetime'].dt.month).agg({'columns': 'mean','columns2': 'min'})
- .sample
  - state.sample(10, random_state=28)
  
> Визуализация
- Линия и точки по данным
  - 
  ```python
  
  .plot(xlabel='',
    ylabel = '',
    title='',
    grid=True,
    figsize=(16,9))
    ```
- Гистограммы
  - .hist(figsize=(9,5), bins=100)

> Точная настройка через matplotlib
- import matplotlib.pyplot as plt
- 
    ```python
    fig, ax = plt.subplots(1, 1, figsize=(9,5))
    ax.plot(rents_by_week)
    ax.scatter(
        rents_by_week.index,
        rents_by_week.iloc[:,0]
    )
    ax.set_title=''
    ax.set_xlabel=''
    ax.set_ylabel = ''
    ax.grid(True)
    fig.show()
    ```

> Сохранение данных
- CSV
  - to_csv('name.csv', sep=';')
- Excel (openpyxl)
  - to_excel('name.xlsx', engine='openpyxl') 