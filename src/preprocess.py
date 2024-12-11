import json
from config import DATA_FILE_PATH  # иммпортируем путь

# Определяем функцию load_chat_data
def load_chat_data(DATA_FILE_PATH):
    try:
        with open(DATA_FILE_PATH, 'r', encoding='utf-8') as f:
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
        data = load_chat_data(DATA_FILE_PATH)
        print("Данные успешно загружены.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

