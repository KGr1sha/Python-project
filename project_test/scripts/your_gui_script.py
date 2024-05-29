import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from configparser import ConfigParser
import pandas as pd
import os
import sys

# Add the scripts directory to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_dir = current_dir
if scripts_dir not in sys.path:
    sys.path.append(scripts_dir)





# Load configuration
config = ConfigParser()
config.read(os.path.join(current_dir, '..', 'config.ini'))

# Construct the paths to the data files
titanic_data_path = config.get('settings', 'titanic_dataset', fallback='../data/Titanic_Dataset.csv')
people_data_path = config.get('settings', 'people_dataset', fallback='../data/people.csv')
tickets_data_path = config.get('settings', 'tickets_dataset', fallback='../data/tickets.csv')

full_titanic_data_path = os.path.abspath(os.path.join(current_dir, titanic_data_path))
full_people_data_path = os.path.abspath(os.path.join(current_dir, people_data_path))
full_tickets_data_path = os.path.abspath(os.path.join(current_dir, tickets_data_path))


print("Full Titanic Data Path:", full_titanic_data_path)
print("Full People Data Path:", full_people_data_path)
print("Full Tickets Data Path:", full_tickets_data_path)




# Load data
try:
    if not os.path.isfile(full_titanic_data_path):
        raise FileNotFoundError(f"File not found: {full_titanic_data_path}")
    if not os.path.isfile(full_people_data_path):
        raise FileNotFoundError(f"File not found: {full_people_data_path}")
    if not os.path.isfile(full_tickets_data_path):
        raise FileNotFoundError(f"File not found: {full_tickets_data_path}")

    df_titanic = pd.read_csv(full_titanic_data_path)
    df_people = pd.read_csv(full_people_data_path)
    df_tickets = pd.read_csv(full_tickets_data_path)
except FileNotFoundError as e:
    messagebox.showerror("Error", str(e))
    df_titanic = pd.DataFrame()  # Empty dataframe as a placeholder
    df_people = pd.DataFrame()  # Empty dataframe as a placeholder
    df_tickets = pd.DataFrame()  # Empty dataframe as a placeholder

# Import functions from other scripts
from script_text import age_distribution, overall_survival_rate, gender_survival, survival_rate_by_age
from script_graphics import show_survival_by_gender, show_age_distribution_by_survival, show_boxplot_fare_by_survival, show_boxplot_age_by_survival

class TitanicApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Информационно-Аналитическое Приложение")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        offset_x = int(screen_width/4)
        offset_y = int(screen_height/4)
        self.geometry(f"{int(screen_width/2)}x{int(screen_height/2)}+{offset_x}+{offset_y}")

        # Create Widgets
        self.create_widgets()

    def create_widgets(self):
        # Example Label
        self.label = ttk.Label(self, text="Выберите опцию:")
        self.label.pack(pady=10)

        # Button to show survival by gender
        self.survival_gender_button = ttk.Button(self, text="Показать выживаемость по полу", command=self.show_survival_by_gender)
        self.survival_gender_button.pack(pady=10)

        # Button to show age distribution by survival
        self.age_distribution_button = ttk.Button(self, text="Показать распределение возраста по выживаемости", command=self.show_age_distribution_by_survival)
        self.age_distribution_button.pack(pady=10)

        # Button to show overall survival rate
        self.overall_survival_button = ttk.Button(self, text="Показать общий уровень выживаемости", command=self.show_overall_survival_rate)
        self.overall_survival_button.pack(pady=10)

        # Input for age range and button to show survival rate by age
        self.age_range_label = ttk.Label(self, text="Введите возрастной диапазон (мин и макс):")
        self.age_range_label.pack(pady=10)

        self.age_min_entry = ttk.Entry(self)
        self.age_min_entry.pack(pady=5)
        self.age_max_entry = ttk.Entry(self)
        self.age_max_entry.pack(pady=5)

        self.survival_by_age_button = ttk.Button(self, text="Показать уровень выживаемости по возрасту", command=self.show_survival_by_age)
        self.survival_by_age_button.pack(pady=10)

    def show_survival_by_gender(self):
        try:
            show_survival_by_gender()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def show_age_distribution_by_survival(self):
        try:
            show_age_distribution_by_survival()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def show_overall_survival_rate(self):
        try:
            rate = overall_survival_rate(df_titanic)
            messagebox.showinfo("Overall Survival Rate", f"The overall survival rate is {rate:.2f}%")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def show_survival_by_age(self):
        try:
            age_min = int(self.age_min_entry.get())
            age_max = int(self.age_max_entry.get())
            rate = survival_rate_by_age(df_titanic, age_min, age_max)
            messagebox.showinfo("Survival Rate by Age", f"The survival rate for ages {age_min}-{age_max} is {rate:.2f}%")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid integers for age range.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Run the Application
if __name__ == "__main__":
    app = TitanicApp()
    app.mainloop()
