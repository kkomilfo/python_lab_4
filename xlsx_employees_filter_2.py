import pandas as pd
from datetime import datetime
import os

def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def read_csv_file(filename):
    try:
        data = pd.read_csv(filename, encoding='utf-8')
        return data
    except FileNotFoundError:
        print("Повідомлення про відсутність, або проблеми при відкритті файлу CSV.")
        return None

def create_xlsx_file(csv_filename, xlsx_filename):
    try:
        data = read_csv_file(csv_filename)
        if data is None:
            return


        # data['Дата народження'] = pd.to_datetime(data['Дата народження'], errors='coerce')

        data['Вік'] = data['Дата народження'].apply(lambda dob: calculate_age(dob) if not pd.isnull(dob) else None)

        age_ranges = {
            'younger_18': data[data['Вік'] < 18],
            '18-45': data[(data['Вік'] >= 18) & (data['Вік'] <= 45)],
            '45-70': data[(data['Вік'] > 45) & (data['Вік'] <= 70)],
            'older_70': data[data['Вік'] > 70]
        }

        with pd.ExcelWriter(xlsx_filename, engine='openpyxl') as writer:
            data.to_excel(writer, sheet_name='all', index=False, columns=["Прізвище", "Ім’я", "По батькові", "Дата народження", "Вік"])

            for sheet_name, age_data in age_ranges.items():
                age_data.to_excel(writer, sheet_name=sheet_name, index=False, columns=["Прізвище", "Ім’я", "По батькові", "Дата народження", "Вік"])

        print("Ok")
    except Exception as e:
        print(f"Повідомлення про неможливість створення XLSX файлу: {str(e)}")

def main():
    csv_filename = 'employees_large_with_patronymics.csv'
    xlsx_filename = 'employees_age_groups.xlsx'

    if not os.path.exists(csv_filename):
        print("Повідомлення про відсутність, або проблеми при відкритті файлу CSV.")
        return

    create_xlsx_file(csv_filename, xlsx_filename)

if __name__ == '__main__':
    main()
