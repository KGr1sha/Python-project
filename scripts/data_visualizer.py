import pandas as pd
import matplotlib.pyplot as plt
import os


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

SAVE_DIR = os.path.join('..', 'graphs') 
DATASET_PATH = os.path.join('..', 'data', 'Titanic Dataset.csv') 

data = pd.read_csv(DATASET_PATH)

def show_survival_by_gender():
    plt.figure(figsize=(12, 8))
    data.groupby('sex')['survived'].count().plot(kind='bar', color='red')
    plt.xlabel('Sex')
    plt.ylabel('Survived')
    plt.title('Survival by Gender')
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(SAVE_DIR, 'clustered_bar_plot.png'))
    plt.show()


def show_age_distribution_by_survival():
    plt.figure(figsize=(12, 8))
    plt.hist([data[data['survived'] == 0]['age'], data[data['survived'] == 1]['age']], bins=10, alpha=0.5, label=['Not Survived', 'Survived'], color=['red', 'green'])
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Histogram of Scores. Age Distribution by Survival')
    plt.legend()
    plt.savefig(os.path.join(SAVE_DIR, 'categorized_histogram_quant_qual.png'))
    plt.show()


def show_boxplot_fare_by_survival():
    data.boxplot(column='fare', by='survived', figsize=(16,8))
    plt.xlabel('Survived', fontsize=12)
    plt.ylabel('Fare', fontsize=12)
    plt.title('Boxplot of Fare Distribution by Survival', fontsize=12)
    plt.xticks(ticks=[1, 2], labels=['Not Survived', 'Survived'])
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.savefig(os.path.join(SAVE_DIR, 'categorized_boxplot_fare.png'))
    plt.show()


def show_boxplot_age_by_survival():
    data.boxplot(column='fare', by='survived', figsize=(16,8))
    plt.xlabel('Survived', fontsize=12)
    plt.ylabel('Fare', fontsize=12)
    plt.title('Boxplot of Fare Distribution by Survival', fontsize=12)
    plt.xticks(ticks=[1, 2], labels=['Not Survived', 'Survived'])
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.savefig(os.path.join(SAVE_DIR, 'categorized_boxplot_age.png'))
    plt.show()


def show_scatter_fare_age():
    plt.figure(figsize=(16, 8))
    colors = pd.factorize(data['survived'])[0]
    plt.scatter(data['fare'], data['age'], c=colors, cmap='viridis', alpha=0.6)
    plt.xlabel('Fare')
    plt.ylabel('Age')
    plt.title('Categorized Scatterplot: Fare vs Age by Survived')
    plt.colorbar(label='Survived')
    plt.savefig(os.path.join(SAVE_DIR, 'scatterplot_fare_age_survived'))
    plt.show()


if __name__ == '__main__':
    show_survival_by_gender()
    show_age_distribution_by_survival()
    show_boxplot_fare_by_survival()
    show_boxplot_age_by_survival()
    show_scatter_fare_age()

