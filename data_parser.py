import pandas as pd
import os

# Определение абсолютного пути к текущему файлу и директории
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Путь к каталогу с данными
DATA_DIR = os.path.join('..', 'data')


def parse_data() -> None:
    """
    Функция для парсинга данных о пассажирах Титаника и сохранения их в отдельные CSV-файлы.

    Функция считывает исходный набор данных, разделяет его на два DataFrame: один с информацией о билетах,
    классе, стоимости и кабине, другой - с информацией о людях. Затем каждый DataFrame сохраняется в отдельный CSV-файл.
    """
    # Считывание исходных данных
    data = pd.read_csv(os.path.join(DATA_DIR, 'data/Titanic Dataset.csv'))

    # Создание DataFrame с информацией о билетах
    tickets = data[['ticket', 'pclass', 'fare', 'cabin']].copy()

    # Создание DataFrame с информацией о людях
    people = data[['name', 'sex', 'age', 'survived', 'sibsp', 'parch', 'ticket']].copy()

    # Сохранение DataFrame в CSV-файлы
    tickets.to_csv(os.path.join(DATA_DIR, 'data/tickets.csv'), index=False)
    people.to_csv(os.path.join(DATA_DIR, 'data/people.csv'), index=False)


if __name__ == "__main__":
    parse_data()
