import json
import pandas as pd

# Определяем функцию load_chat_data
def load_chat_data(file_path):
    """
    Загружает данные чата из JSON.
    Возвращает весь JSON-объект.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print("Файл успешно загружен.")
            print("Формат: <json>")  # Добавляем вывод формата
            return data
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        raise


# Путь к JSON-файлу
file_path = "data/sample.json"  # Укажите ваш путь к JSON-файлу

# Используем функцию load_chat_data
try:
    chat_data = load_chat_data(file_path)

except Exception as e:
    print(f"Произошла ошибка при загрузке данных: {e}")



