# Светлана Ананьина, 6-я когорта — Финальный проект. Инженер по тестированию плюс
# Тестирование API Яндекс Самокат 2.0

import data
import sender_stand_request


# Создание заказа. Возвращает его трек
def create_new_order():
    response = sender_stand_request.post_new_order()    # Запрос к API
    assert response.status_code == 201
    return response.json()["track"]

# Тест создания и получения заказа в БД
def test_create_and_get_new_order():
    track = create_new_order()
    response = sender_stand_request.get_order_info(str(track))
    assert response.status_code == 200

