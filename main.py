import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

from config import DATA_FILES
from src.prep import load_chat_data
from src.analyze import analyze_chat_data
from src.visual import plot_daily_activity



if __name__ == "__main__":
    try:
        # Загружаем данные
        data = load_chat_data(DATA_FILES["GN"])
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
        # Выдаем визуализацию
        plot_daily_activity(results["daily_activity"])

    except Exception as e:
        print(f"Произошла ошибка: {e}")









