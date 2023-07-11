import configuration
import requests
import data

# Создание нового заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json = data.order_body,
                         headers = data.headers)

# Получение данных заказа по его треку (строка)
def get_order_info(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + track)

