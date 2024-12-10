import matplotlib
matplotlib.use('TkAgg')  # Устанавливаем стабильный бэкэнд
import matplotlib.pyplot as plt

from src.preprocess import load_chat_data

# Загрузка данных
file_path = 'data/sample.json'
messages = load_chat_data(file_path)

# Группировка данных
daily_activity = group_messages_by_day(messages)

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

# Вызов функции для визуализации
plot_daily_activity(daily_activity)


