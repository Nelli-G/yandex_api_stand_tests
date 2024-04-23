import requests

import sender_stand_request

import data

# Функция для изменения значения в параметре firstName в теле запроса
def get_user_body(first_name):
    current_body = data.user_body.copy()
    if first_name is not False:
        current_body["firstName"] = first_name
    else:
        current_body.pop("firstName")
    return current_body

#Функция для позитивной проверки
def positive_assert(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    users_table_response = sender_stand_request.get_users_table()
    # Использование обратной косой черты (\) в конце позволяет перенести часть кода на новую строку для лучшей читаемости.
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1

# Тест 1. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов
def test_create_user_2_letters_in_first_name_get_success_response():
    positive_assert("Aa")

# Тест 2. Успешное создание пользователя
# Параметр fisrtName состоит из 15 символов
def test_create_user_15_letters_in_first_name_get_success_response():
    positive_assert("Ааааааааааааааа")

# Функция для негативной проверки, когда в ответе ошибка: "Имя пользователя введено некорректно..."
def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
    assert user_response.json()["message"] == "Имя пользователя введено некорректно. " \
                                             "Имя может содержать только русские или латинские буквы, " \
                                             "длина должна быть не менее 2 и не более 15 символов"

# Функция для негативной проверки, когда в ответе ошибка: "Не все необходимые параметры были переданы"
def negative_assert_parameters(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
    assert user_response.json()["message"] == "Не все необходимые параметры были переданы"

# Функция для негативной проверки, когда в ответе ошибка: если тип Число, то только код 400
def negative_assert_number_type(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400

# Тест 3. Ошибка при создании пользователя
# Параметр fisrtName состоит из 1 символа
def test_create_user_1_letter_in_first_name_get_unsuccess_response():
    negative_assert_symbol("А")

# Тест 4. Ошибка при создании пользователя
# Параметр fisrtName состоит из 16 символов
def test_create_user_16_letters_in_first_name_get_unsuccess_response():
    negative_assert_symbol("Аааааааааааааааа")

# Тест 5. Успешное создание пользователя
# Параметр fisrtName содержит латиницу
def test_create_user_english_letters_in_first_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Успешное создание пользователя
# Параметр fisrtName содержит кириллицу
def test_create_user_russian_letters_in_first_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Ошибка при создании пользователя
# Параметр fisrtName содержит пробел
def test_create_user_has_space_in_first_name_get_unsuccess_response():
    negative_assert_symbol("Человек и Ко")

# Тест 8. Ошибка при создании пользователя
# Параметр fisrtName содержит спецсимволы
def test_create_user_has_special_symbols_in_first_name_get_unsuccess_response():
    negative_assert_symbol("№%@")

# Тест 9. Ошибка при создании пользователя
# Параметр fisrtName состоит из цифр
def test_create_user_has_numbers_in_first_name_get_unsuccess_response():
    negative_assert_symbol("123")

# Тест 10. Ошибка при создании пользователя
# Параметра fisrtName нет в запросе
def test_create_user_no_first_name_get_unsuccess_response():
    negative_assert_parameters(False)

# Тест 11. Ошибка при создании пользователя
# Параметр fisrtName состоит из пустой строки
def test_create_user_empty_first_name_get_unsuccess_response():
    negative_assert_parameters("")

# Тест 12. Ошибка при создании пользователя
# Параметр fisrtName имеет тип Число
def test_create_user_number_type_first_name_get_unsuccess_response():
    negative_assert_number_type(12)


