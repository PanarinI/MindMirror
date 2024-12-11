import pandas as pd

def analyze_chat_data(data):
    """
    Выполняет первичный анализ данных чата.
    Возвращает результаты анализа.
    """
    try:
        # Извлекаем метаданные чата
        chat_name = data.get("name", "Неизвестно")
        chat_type = data.get("type", "Неизвестно")
        creation_date = data.get("date", "Неизвестно")

        # Преобразуем сообщения в DataFrame
        messages = pd.DataFrame(data.get("messages", []))
        if messages.empty:
            raise ValueError("Сообщения отсутствуют в JSON-файле.")

        # Общее количество сообщений
        total_messages = len(messages)

        # Подсчёт сообщений по участникам
        if 'from' not in messages.columns:
            raise KeyError("Ключ 'from' отсутствует в данных.")
        message_count_by_user = messages['from'].value_counts()
        message_distribution = message_count_by_user.reset_index()
        message_distribution.columns = ['Participant', 'Message Count']

        # Первая и последняя даты чата
        messages['date'] = pd.to_datetime(messages['date'], errors='coerce')
        first_date = messages['date'].min()
        last_date = messages['date'].max()

        # Группировка сообщений по дням и участникам
        daily_activity = messages.groupby(
            [messages['date'].dt.date, 'from']
        ).size().reset_index(name='Message Count')

        # Возвращаем результаты анализа
        return {
            "chat_name": chat_name,
            "chat_type": chat_type,
            "creation_date": creation_date,
            "message_distribution": message_distribution,
            "first_date": first_date,
            "last_date": last_date,
            "daily_activity": daily_activity,
            "total_messages": total_messages
        }
    except Exception as e:
        print(f"Произошла ошибка при анализе данных: {e}")
        raise

if __name__ == "__main__":
    from src.preprocess import load_chat_data  # Импортируем функцию загрузки данных

    try:
        # Загружаем данные
        data = load_chat_data(DATA_FILE_PATH)  # Вызываем функцию для загрузки данных
        print("Данные успешно загружены для анализа.")

        # Выполняем анализ
        results = analyze_chat_data(data)

        # Выводим результаты анализа
        print(f"Название чата: {results['chat_name']}")
        print(f"Тип чата: {results['chat_type']}")
        print(f"Дата создания чата: {results['creation_date']}")
        print(f"Общее количество сообщений: {results['total_messages']}")
        print(f"Первое сообщение: {results['first_date']}")
        print(f"Последнее сообщение: {results['last_date']}")
        print("\nСписок участников и количество их сообщений:")
        print(results["message_distribution"].to_string(index=False))
        print("\nГруппировка сообщений по дням и участникам:")
        print(results["daily_activity"].head())  # Выводим первые строки
    except Exception as e:
        print(f"Произошла ошибка: {e}")
