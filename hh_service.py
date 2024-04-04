import requests
import csv

params = {
        'text': 'Fortnite balls',
        'area': '1',
        'period': '30',
        'per_page': '100'
    }

def get_vacancies(tag: str):
    url = 'https://api.hh.ru/vacancies'
    params['text'] = f"NAME:{tag}"
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Ошибка при выполнении запроса:", response.status_code)
        return None

def extract_salary(vacancy):
    salary_data = vacancy.get('salary')
    if salary_data:
        lower_bound = salary_data.get('from')
        upper_bound = salary_data.get('to')
        currency = salary_data.get('currency')
        return lower_bound, upper_bound, currency
    return None, None, None

def save_to_csv(vacancies, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Тэг', 'Название', 'Нижняя граница зарплаты', 'Верхняя граница зарплаты', 'Валюта'])
        writer.writeheader()
        for vacancy in vacancies:
            lower_bound, upper_bound, currency = extract_salary(vacancy)
            writer.writerow({
                'Название': vacancy['name'],
                'Нижняя граница зарплаты': lower_bound,
                'Верхняя граница зарплаты': upper_bound,
                'Валюта': currency,
                'Тэг': params['text'][5:]
            })

with open('tags.txt', 'r') as tags_file:

    with open('vacancies2.csv', 'w') as _:
        pass

    for tag in [line.rstrip('\n') for line in tags_file]:
        print(tag)
        vacancies_data = get_vacancies(tag)

        if vacancies_data:
            save_to_csv(vacancies_data['items'], 'vacancies2.csv')
            print("Данные успешно сохранены в файл vacancies2.csv")
        else:
            print("Не удалось получить данные о вакансиях.")


