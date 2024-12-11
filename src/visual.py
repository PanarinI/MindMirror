import matplotlib
matplotlib.use('TkAgg')  # Устанавливаем стабильный бэкэнд
import matplotlib.pyplot as plt
from src.prep import load_chat_data
from src.analyze import analyze_chat_data
from config import DATA_FILES


# Функция для визуализации
def plot_daily_activity(daily_activity):
    plt.figure(figsize=(10, 6))

    # Группируем по участникам и строим графики
    for participant, group in daily_activity.groupby('from'):
        plt.plot(group['date'], group['Message Count'], marker='o', label=participant)

    plt.xlabel('Date')
    plt.ylabel('Message Count')
    plt.title('Daily Activity by Participants')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()  # Оптимизируем расположение элементов
    plt.show()


if __name__ == "__main__":
    try:
        # Загружаем данные
        data = load_chat_data(DATA_FILES["GN"])
        print("Данные успешно загружены.")

        # Выполняем анализ
        results = analyze_chat_data(data)

        # Извлекаем группировку сообщений по дням
        daily_activity = results["daily_activity"]

        # Вызов функции для визуализации
        plot_daily_activity(daily_activity)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
