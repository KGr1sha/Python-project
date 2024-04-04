import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


# Установка размера шрифта для всех элементов графика
plt.rc('font', size=7) # Установка размера шрифта в 10
# Чтение данных из файла CSV
df = pd.read_csv('vacancies2.csv', delimiter=',', encoding='utf-8')

# Замена NaN в 'Верхняя граница зарплаты' на значения из 'Нижняя граница зарплаты'
df['Верхняя граница зарплаты'] = df['Верхняя граница зарплаты'].fillna(df['Нижняя граница зарплаты'])

# Удаление строк, где обе границы зарплаты отсутствуют
df = df.dropna(subset=['Верхняя граница зарплаты'])

# Создание столбчатой диаграммы
plt.figure(figsize=(5, 5))
plt.bar(df['Название'], df['Верхняя граница зарплаты'])

def ruble_formatter(x, pos):
    return f'{x} руб.'

formatter = FuncFormatter(ruble_formatter)

# Применение форматирования к оси Y
plt.gca().yaxis.set_major_formatter(formatter)

# Поворот меток оси X на 45 градусов
plt.xticks(rotation=60, ha='right')
# Увеличение размера шрифта для меток осей
plt.xlabel('Вакансия', fontsize=14) # Увеличение размера шрифта для метки оси X
plt.ylabel('Верхняя граница зарплаты', fontsize=14) # Увеличение размера шрифта для метки оси Y

# Показать график
plt.show()
