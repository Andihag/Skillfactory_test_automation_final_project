from faker import Faker
import random
import string

url_base_page = "https://b2c.passport.rt.ru/"

url_change_page = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials"

def sql_injection():
   sql_injection = '<script>alert("Поле input уязвимо!")</script>'
   return sql_injection

def random_int():
   random_int = random.randint(1, 99999999999)
   return random_int

def generate_string(num):
   return "а" * num

def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

def valid_email():
   random_valid_email = Faker().email()
   return random_valid_email

def valid_phone():
   random_valid_phone = random.randint(1111111111, 9999999999)
   return random_valid_phone

def valid_first_name():
   random_valid_first_name = Faker(['ru_RU']).first_name()
   return random_valid_first_name

def first_name_en():
   random_first_name_en = Faker().first_name()
   return random_first_name_en

def first_name_last_name():
   random_first_name_last_name = Faker().name()
   return random_first_name_last_name

def valid_last_name():
   random_valid_last_name = Faker(['ru_RU']).last_name()
   return random_valid_last_name

def without_name_email():
    return "@ru.ru"

def without_at_email():
    return "ru.ru"

def without_domain_email():
    return "ru@"

def valid_password():
    pwd = []
    for i in range(3):
        pwd.append(random.choice(string.ascii_lowercase))
        pwd.append(random.choice(string.ascii_uppercase))
        pwd.append(random.choice(string.digits))
    return (''.join(pwd))

def valid_password2():
    pwd = []
    for i in range(3):
        pwd.append(random.choice(string.ascii_lowercase))
        pwd.append(random.choice(string.ascii_uppercase))
        pwd.append(random.choice(string.digits))
    return (''.join(pwd))

valid_email_or_phone = [valid_email(), "77700774321", "375555251505"]

valid_password = [valid_password()]

valid_password2 = [valid_password2()]

valid_first_name = [valid_first_name()]

valid_last_name = [valid_last_name()]

invalid_name = [random_int()
                , generate_string(1)
                , generate_string(31)
                , first_name_en()
                , chinese_chars()
                , special_chars()
                , first_name_last_name()
                ]

invalid_email_or_phone = [without_name_email()
                          , without_at_email()
                          , without_domain_email()
                          , russian_chars()
                          , chinese_chars()
                          , special_chars()
                          ]

invalid_password = [random_int()
                    , generate_string(10)
                    , russian_chars()
                    , chinese_chars()
                    , special_chars()
                    , first_name_en()
                    , first_name_last_name()
                    ]


