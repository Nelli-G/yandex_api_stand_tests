# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
# Это популярная библиотека, которая позволяет взаимодействовать с веб-сервисами
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

#Этот код отправляет HTTP GET-запрос к заданному URL-адресу, который складывается
#из базового адреса сервиса и пути к его документации, оба определены в модуле
#конфигурации. Затем он выводит HTTP-статус код ответа от сервера, который указывает
#на результат выполнения запроса.

# Определяем функцию get_docs, которая не принимает параметров
def get_docs():
    # Выполняем GET-запрос к URL, который складывается из базового URL-адреса сервиса
    # и пути к документации, заданных в модуле конфигурации
    # Функция возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

# Вызываем функцию get_docs и сохраняем результат в переменную response
#response = get_docs()

# Выводим в консоль HTTP-статус код полученного ответа
# Например, 200 означает успешный запрос, 404 - не найдено и т.д.
#print(response.status_code)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count":20})

#log_response = get_logs()

#print(str(log_response.status_code) + " " + str(log_response.headers))

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

#users_response = get_users_table()

#print(users_response.status_code)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

#new_user_response = post_new_user(data.user_body)

#print(new_user_response.status_code)
#print(new_user_response.json())

def post_products_kits(product_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=product_ids,
                         headers=data.headers)

#kits_response = post_products_kits(data.product_ids)

#print(kits_response.status_code)
#print(kits_response.json())