import csv
import random
from faker import Faker

fake = Faker('uk_UA')

patronymics = {
    "male": ["Олександрович", "Іванович", "Сергійович", "Михайлович", "Андрійович",
             "Петрович", "Васильович", "Дмитрович", "Юрійович", "Володимирович",
             "Романович", "Борисович", "Максимович", "Євгенович", "Арсенович",
             "Олегович", "Ілліч", "Леонідович", "Тарасович", "Федорович"],

    "female": ["Олександрівна", "Іванівна", "Сергіївна", "Михайлівна", "Андріївна",
               "Петрівна", "Василівна", "Дмитрівна", "Юріївна", "Володимирівна",
               "Романівна", "Борисівна", "Максимівна", "Євгенівна", "Арсенівна",
               "Олегівна", "Іллівна", "Леонідівна", "Тарасівна", "Федорівна"]
}

total_entries = 2000
female_percentage = 0.4
male_percentage = 0.6

num_females = int(total_entries * female_percentage)
num_males = total_entries - num_females

headers = ["Прізвище", "Ім’я", "По батькові", "Стать", "Дата народження",
           "Посада", "Місто проживання", "Адреса проживання", "Телефон", "Email"]

data = [headers]

def generate_male_entry():
    first_name = fake.first_name_male()
    last_name = fake.last_name_male()
    patronymic = random.choice(patronymics['male'])
    gender = "Чоловік"
    dob = fake.date_of_birth(minimum_age=16, maximum_age=85).strftime("%Y-%m-%d")
    job = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()

    return [last_name, first_name, patronymic, gender, dob, job, city, address, phone, email]

def generate_female_entry():
    first_name = fake.first_name_female()
    last_name = fake.last_name_female()
    patronymic = random.choice(patronymics['female'])
    gender = "Жінка"
    dob = fake.date_of_birth(minimum_age=16, maximum_age=85).strftime("%Y-%m-%d")
    job = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()

    return [last_name, first_name, patronymic, gender, dob, job, city, address, phone, email]

for _ in range(num_males):
    data.append(generate_male_entry())

for _ in range(num_females):
    data.append(generate_female_entry())


random.shuffle(data[1:])

with open('employees_large_with_patronymics.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data saved to employees_large_with_patronymics.csv")
