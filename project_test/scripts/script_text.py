import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from configparser import ConfigParser

current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_dir = current_dir
if scripts_dir not in sys.path:
    sys.path.append(scripts_dir)


config = ConfigParser()
config.read(os.path.join(current_dir, '..', 'config.ini'))

# Construct the paths to the data files
titanic_data_path = config.get('settings', 'titanic_dataset', fallback='../data/Titanic_Dataset.csv')
people_data_path = config.get('settings', 'people_dataset', fallback='../data/people.csv')
tickets_data_path = config.get('settings', 'tickets_dataset', fallback='../data/tickets.csv')

full_titanic_data_path = os.path.abspath(os.path.join(current_dir, titanic_data_path))
full_people_data_path = os.path.abspath(os.path.join(current_dir, people_data_path))
full_tickets_data_path = os.path.abspath(os.path.join(current_dir, tickets_data_path))


df = pd.read_csv(full_titanic_data_path)
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


print('Текстовый отчет №1')
print('Функция генерации отчетов о распределении возраста пассажиров в диапазоне от 20 до 30 лет')
print(age_distribution(df, 20, 30))
print()

print('Текстовый отчет №2')
print('Функция генерации отчетов о выживаемости пассажиров в зависимости от пола (female)')
print(gender_survival(df, 'female'))
print()

print('Текстовый отчет №3')
print(generate_survival_report(os.path.join("..", "data", "Titanic_Dataset.csv")))
print('Билеты выживших пассажиров')

print('Текстовый отчет №4')
create_survival_pivot_table(os.path.join("..", "data", "Titanic_Dataset.csv"))
