import json
from config import DATA_FILES  # Импортируем словарь с путями к файлам

# Определяем функцию load_chat_data
def load_chat_data(file_path):
    """
    Загружает данные из указанного файла JSON.
    :param file_path: Путь к файлу JSON.
    :return: JSON-объект с данными.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print("Файл успешно загружен.")
            print("Формат: <json>")
            return data
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        raise

if __name__ == "__main__":
    try:
        # Загружаем данные в переменную data
        data = load_chat_data(DATA_FILES["GN"])  # Передаём путь к файлу из словаря DATA_FILES
        print("Данные успешно загружены.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
