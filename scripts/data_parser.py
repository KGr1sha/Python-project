import pandas as pd
import os


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

DATA_DIR = os.path.join('..', 'data') 

def parse_data():
    data = pd.read_csv(os.path.join(DATA_DIR, 'Titanic Dataset.csv'))
    tickets = data[['ticket', 'pclass', 'fare', 'cabin']].copy()
    people = data[['name', 'sex', 'age', 'survived', 'sibsp', 'parch', 'ticket']].copy()

    tickets.to_csv(os.path.join(DATA_DIR, 'tickets.csv'), index=False)
    people.to_csv(os.path.join(DATA_DIR, 'people.csv'), index=False)


if __name__ == "__main__":
    parse_data()

