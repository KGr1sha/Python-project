import requests
import csv


def get_vacancies():
    url = 'https://api.hh.ru/vacancies'
    params = {
        'text': 'python разработчик',
        'area': '1',
        'period': '30',
        'per_page': '100'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Ошибка при выполнении запроса:", response.status_code)
        return None


def extract_salary(vacancy):
    salary_data = vacancy.get('salary')
    if salary_data:
        if salary_data.get('from') and salary_data.get('to'):
            return f"{salary_data['from']} - {salary_data['to']} {salary_data['currency']}"
        elif salary_data.get('from'):
            return f"от {salary_data['from']} {salary_data['currency']}"
        elif salary_data.get('to'):
            return f"до {salary_data['to']} {salary_data['currency']}"
    return 'Не указано'


def save_to_csv(vacancies, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Название', 'Компания', 'Зарплата', 'Ссылка'])
        writer.writeheader()
        for vacancy in vacancies:
            writer.writerow({
                'Название': vacancy['name'],
                'Компания': vacancy['employer']['name'],
                'Зарплата': extract_salary(vacancy),
                'Ссылка': vacancy['alternate_url']
            })


if __name__ == '__main__':
    vacancies_data = get_vacancies()
    
    if vacancies_data:
        save_to_csv(vacancies_data['items'], 'vacancies.csv')
        print("Данные успешно сохранены в файл vacancies.csv")
    else:
        print("Не удалось получить данные о вакансиях.")
