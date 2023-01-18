# Skillfactory_test_automation_final_project

Финальный тестовый проект Skillfactory курса INTQAP

Автоматизированное ui-тестирование нового интерфейса авторизации в личном кабинете от заказчика Ростелеком Информационные Технологии (https://b2c.passport.rt.ru/)
____

+ Тест-кейсы доступны по ссылке: https://docs.google.com/spreadsheets/d/1W4LPjmEzJtVouJ4QDtkQmUqFSHkn0lOaJLCCXogbx2w/edit?usp=sharing

+ Баг-репорты доступны по ссылке:
https://docs.google.com/spreadsheets/d/1EFlbciCSjXWw7eBjyUwjK_r2AB5pb4Ok8GYgRaq6RZk/edit?usp=sharing

1. В папке pages в файле base_page.py находится конструктор webdriver и общие для всех тестируемых страниц методы.

2. В папке pages в файлах auth_page.py, change_pass_page.py, reg_page.py находятся методы проверок: файл auth_page.py содержит методы проверок формы авторизации; файл change_pass_page.py содержит методы проверок формы восстановления пароля; файл reg_page.py содержит методы проверок формы регистрации.

3. В папке tests в файлах test_auth_page.py, test_change_pass_page.py, test_reg_page.py находятся тесты. Все тесты помечены номером, совпадающим с номером тест-кейса в файле: https://docs.google.com/spreadsheets/d/1W4LPjmEzJtVouJ4QDtkQmUqFSHkn0lOaJLCCXogbx2w/edit?usp=sharing. Во всех файлах с тестами, находятся закомментированные команды для запуска тестов из командной строки (запуск тестов формы авторизации: # python -m pytest -v --tb=line tests/test_auth_page.py; запуск тестов формы восстановления пароля: # python -m pytest -v --tb=line tests/ test_change_pass_page.py; запуск тестов формы регистрации: # python -m pytest -v --tb=line tests/ test_reg_page.py)

4. В папке pages в файле "locators.py находятся все локаторы.

5. В корне проекта в файле conftest.py находится фикстура с функцией открытия и закрытия браузера. 

6. В корне проекта в файле settings.py находятся методы и переменные для параметризации тестов

7. В корне проекта в файле pytest.ini зарегистрированы метки маркировок тестов.

8. В корне проекта в файле requirements.py описаны используемые библиотеки.
