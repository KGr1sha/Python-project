import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file_path = 'data/Titanic Dataset.csv'
df = pd.read_csv(file_path)
df = df.drop(df.columns[0], axis=1)


def age_distribution(df: pd.DataFrame, min_age: int, max_age: int) -> pd.DataFrame:
    """
    Функция генерации отчетов о распределении возраста пассажиров.

    Parameters
    ----------
    df : pd.DataFrame
        Исходная таблица с данными о пассажирах.
    min_age : int
        Минимальный возраст.
    max_age : int
        Максимальный возраст.

    Returns
    -------
    pd.DataFrame
        Отчет о распределении возраста пассажиров в заданном диапазоне.
    """
    filtered_df = df[(df['age'] >= min_age) & (df['age'] <= max_age)][['name', 'sex', 'age', 'survived']]
    return filtered_df


def overall_survival_rate(df: pd.DataFrame) -> float:
    """
    Функция для вычисления общего процента выживших пассажиров.

    Parameters
    ----------
    df : pd.DataFrame
        Исходная таблица с данными о пассажирах.

    Returns
    -------
    float
        Общий процент выживших пассажиров.
    """
    survival_rates = df.groupby('sex')['survived'].mean()
    overall_survival_rate = survival_rates.mean() * 100
    return overall_survival_rate


def gender_survival(df: pd.DataFrame, gender: str) -> pd.DataFrame:
    """
    Функция генерации отчетов о выживаемости пассажиров в зависимости от пола.

    Parameters
    ----------
    df : pd.DataFrame
        Исходная таблица с данными о пассажирах.
    gender : str
        Пол пассажира.

    Returns
    -------
    pd.DataFrame
        Отчет о выживаемости пассажиров указанного пола.
    """
    filtered_df = df[df['sex'] == gender][['name', 'sex', 'age', 'survived']]
    return filtered_df


def survival_rate_by_age(df: pd.DataFrame, min_age: int, max_age: int) -> float:
    """
    Функция для вычисления процента выживших пассажиров в заданном диапазоне возраста.

    Parameters
    ----------
    df : pd.DataFrame
        Исходная таблица с данными о пассажирах.
    min_age : int
        Минимальный возраст.
    max_age : int
        Максимальный возраст.

    Returns
    -------
    float
        Процент выживших пассажиров в заданном диапазоне возраста.
    """
    total_passengers = len(df[(df['age'] >= min_age) & (df['age'] <= max_age)])
    survived_passengers = len(df[(df['age'] >= min_age) & (df['age'] <= max_age) & (df['survived'] == 1)])
    survival_rate = (survived_passengers / total_passengers) * 100 if total_passengers > 0 else 0
    return survival_rate


def survival_rate_by_gender(df: pd.DataFrame, gender: str) -> float:
    """
    Функция для вычисления процента выживших пассажиров в зависимости от пола.

    Parameters
    ----------
    df : pd.DataFrame
        Исходная таблица с данными о пассажирах.
    gender : str
        Пол пассажира.

    Returns
    -------
    float
        Процент выживших пассажиров указанного пола.
    """
    total_passengers = len(df[df['sex'] == gender])
    survived_passengers = len(df[(df['sex'] == gender) & (df['survived'] == 1)])
    survival_rate = (survived_passengers / total_passengers) * 100 if total_passengers > 0 else 0
    return survival_rate


def generate_survival_report(file_path: str) -> pd.DataFrame:
    """
    Функция генерации отчета о выживаемости пассажиров Титаника.

    Parameters
    ----------
    file_path : str
        Путь к файлу с данными.

    Returns
    -------
    pd.DataFrame
        Отчет о выживаемости пассажиров.
    """
    df = pd.read_csv(file_path)
    df_males = df[df['sex'] == 'male']
    survival_rate_males = df_males['survived'].mean() * 100
    print(f"Процент выживших мужчин: {survival_rate_males:.2f}%")
    df = pd.read_csv(file_path)
    df_males = df[df['sex'] == 'female']
    survival_rate_males = df_males['survived'].mean() * 100
    print(f"Процент выживших дам: {survival_rate_males:.2f}%")
    return df


def create_survival_pivot_table(file_path: str) -> pd.DataFrame:
    """
    Функция создания Pivot Table для анализа выживаемости пассажиров Титаника.

    Parameters
    ----------
    file_path : str
        Путь к файлу с данными.

    Returns
    -------
    pd.DataFrame
        Pivot Table для анализа выживаемости пассажиров.
    """
    df = pd.read_csv(file_path)
    pivot_table = df.pivot_table(index='sex', columns='survived', aggfunc='size', fill_value=0)
    pivot_table.rename(columns={1: 'Выжили', 0: 'Не выжили'}, inplace=True)
    print("Pivot Table для анализа выживаемости пассажиров по полу:")
    print(pivot_table)
    return pivot_table


def save_to_file(data, filename):
    with open(filename, 'w') as f:
        f.write(str(data))

print('Текстовый отчет №1')
print('\nФункция генерации отчетов о распределении возраста пассажиров в диапазоне от 20 до 30 лет')
report1 = age_distribution(df, 20, 30)
save_to_file(report1, 'report1.txt')
print(report1)

print('\nТекстовый отчет №2')
print('\nФункция генерации отчетов о выживаемости пассажиров в зависимости от пола (female)')
report2 = gender_survival(df, 'female')
save_to_file(report2, 'report2.txt')
print(report2)

print('\nТекстовый отчет №3')
print('\nБилеты выживших пассажиров')
report3 = generate_survival_report('data/people.csv')
save_to_file(report3, 'report3.txt')
print(report3)

print('\nТекстовый отчет №4')
pivot_table = create_survival_pivot_table('data/people.csv')
save_to_file(pivot_table, 'report4.txt')
