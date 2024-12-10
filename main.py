import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

from src.preprocess import load_chat_data
from src.analysis import analyze_chat_data

if __name__ == "__main__":
    # Укажите путь к вашему JSON-файлу
    file_path = "data/sample.json"

    try:
        # Загружаем данные
        data = load_chat_data(file_path)
        print("Данные успешно загружены.")

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









