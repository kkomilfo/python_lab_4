import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def read_csv_file(filename):
    try:
        data = pd.read_csv(filename, encoding='utf-8')
        print("Ok")
        return data
    except FileNotFoundError:
        print("Повідомлення про відсутність, або проблеми при відкритті файлу CSV.")
        return None

def plot_gender_distribution(data):
    gender_count = data['Стать'].value_counts()

    print("Кількість чоловіків:", gender_count.get("Чоловік", 0))
    print("Кількість жінок:", gender_count.get("Жінка", 0))

    gender_count.plot(kind='bar', color=['blue', 'pink'], title='Розподіл за статтю')
    plt.xlabel('Стать')
    plt.ylabel('Кількість')
    plt.xticks(rotation=0)
    plt.savefig('gender_distribution.png')
    plt.close()

def plot_age_category_distribution(data):
    age_categories = {
        'younger_18': data[data['Вік'] < 18],
        '18-45': data[(data['Вік'] >= 18) & (data['Вік'] <= 45)],
        '45-70': data[(data['Вік'] > 45) & (data['Вік'] <= 70)],
        'older_70': data[data['Вік'] > 70]
    }

    category_counts = {key: len(df) for key, df in age_categories.items()}

    print("Кількість молодших 18:", category_counts['younger_18'])
    print("Кількість 18-45:", category_counts['18-45'])
    print("Кількість 45-70:", category_counts['45-70'])
    print("Кількість старших 70:", category_counts['older_70'])

    plt.bar(category_counts.keys(), category_counts.values(), color='green')
    plt.title('Розподіл за віковими категоріями')
    plt.xlabel('Вікові категорії')
    plt.ylabel('Кількість')
    plt.savefig('age_category_distribution.png')
    plt.close()


def plot_gender_age_category_distribution(data):
    age_categories = {
        'younger_18': data[data['Вік'] < 18],
        '18-45': data[(data['Вік'] >= 18) & (data['Вік'] <= 45)],
        '45-70': data[(data['Вік'] > 45) & (data['Вік'] <= 70)],
        'older_70': data[data['Вік'] > 70]
    }

    for category, df in age_categories.items():
        gender_count = df['Стать'].value_counts()
        print(f"Розподіл за статтю для {category}:")
        print(gender_count)

        gender_count.plot(kind='bar', title=f'Розподіл за статтю для категорії {category}', color=['blue', 'pink'])
        plt.xlabel('Стать')
        plt.ylabel('Кількість')
        plt.xticks(rotation=0)
        plt.savefig(f'gender_distribution_{category}.png')
        plt.close()


def main():
    csv_filename = 'employees_large_with_patronymics.csv'


    if not os.path.exists(csv_filename):
        print("Повідомлення про відсутність, або проблеми при відкритті файлу CSV.")
        return


    data = read_csv_file(csv_filename)
    if data is None:
        return


    data['Дата народження'] = pd.to_datetime(data['Дата народження'], errors='coerce')
    data['Вік'] = data['Дата народження'].apply(lambda dob: calculate_age(dob) if not pd.isnull(dob) else None)


    plot_gender_distribution(data)

    plot_age_category_distribution(data)

    plot_gender_age_category_distribution(data)

if __name__ == '__main__':
    main()
