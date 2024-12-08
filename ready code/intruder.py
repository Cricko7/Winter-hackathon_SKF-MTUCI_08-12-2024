import os
import random

# Базовый URL сервера
BASE_URL = "http://127.0.0.1:5000"

# Генерация пароля
def generate_password():
    return str(random.randint(100,999))

# Проверка состояния двери
def check_door(door):
    response = requests.get(f"{BASE_URL}/check_door/{door}")
    
    if response.status_code == 200:
        door_info = response.json()
        if door_info['status'] == 'open':
            print("Поздравляю! Дверь открыта.")
        else:
            password = generate_password()
            print("Дверь закрыта. Вам нужно ввести пароль из трех цифр.")
            user_input = input(f"Введите пароль (например, {password}): ")
            if user_input == password:
                print("Поздравляю! Вы открыли дверь.")
            else:
                print("ААА-А-А!!! Как шумно!!! Сработала система сигнализации!")
    else:
        print("Неверное название двери.")

# Создание пожара
def create_fire(location):
    response = requests.post(f"{BASE_URL}/create_fire/{location}")
    
    if response.status_code == 200:
        fire_message = response.json()
        print(fire_message['message'])
    else:
        print("Неверное место.")

# Основная логика программы
def main():
    while True:
        action = input("Выберите действие: 1 - Проверить дверь, 2 - Создать пожар, 3 - Выход: ")
        
        if action == '1':
            door = input("Введите название двери (room1, room2, hallway): ")
            check_door(door)
        
        elif action == '2':
            location = input("Введите место для создания пожара (room1, room2, hallway): ")
            create_fire(location)
        
        elif action == '3':
            print("Выход из программы.")
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()