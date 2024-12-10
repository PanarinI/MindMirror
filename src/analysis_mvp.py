import json
import pandas as pd
import os

# Получаем текущую директорию, где находится ваш скрипт
current_dir = os.getcwd()
print(current_dir)

# Создаем путь к файлу в папке 'data'
file_path = os.path.join(current_dir, 'data', 'sample.json')

# Открываем и загружаем JSON-файл
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("Файл успешно загружен:", data)
except FileNotFoundError:
    print(f"Файл не найден по пути: {file_path}")


# Конвертируем сообщения в DataFrame
try:
    messages = pd.DataFrame(data['messages'])
except KeyError:
    print("Ключ 'messages' не найден в JSON-файле.")
    exit()

###БАЗОВЫЙ АНАЛИЗ###

# Подсчет количества сообщений по участникам
try:
    message_count_by_user = messages['from'].value_counts()

    # Преобразуем в DataFrame для визуализации
    message_distribution = message_count_by_user.reset_index()
    message_distribution.columns = ['Participant', 'Message Count']

    # Вывод результата
    print(message_distribution)
except KeyError:
    print("Ключ 'from' отсутствует в данных. Проверьте структуру файла.")


#### Группировка сообщений по дням
    def group_messages_by_day(messages):
        # Преобразуем дату в формат datetime
        messages['date'] = pd.to_datetime(messages['date'])
        # Группируем по дням и участникам
        daily_activity = messages.groupby([messages['date'].dt.date, 'from']).size().reset_index(name='Message Count')
        return daily_activity