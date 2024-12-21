from transformers import pipeline
import json
import matplotlib
matplotlib.use('TkAgg')  # Установить интерактивный backend
import matplotlib.pyplot as plt
import pandas as pd  # Для удобства работы с результатами

# Подключение модели анализа тональности
sentiment_analyzer = pipeline("sentiment-analysis", model="blanchefort/rubert-base-cased-sentiment")

# Загрузка данных чата
file_path = 'F:/PythonProject/MirrorMind/data/sample.json'  # Укажите путь к вашему JSON-файлу
with open(file_path, 'r', encoding='utf-8') as f:
    chat_data = json.load(f)

# Извлечение текстов сообщений
messages = [msg["text"] for msg in chat_data["messages"] if "text" in msg and isinstance(msg["text"], str)]
print(f"Количество сообщений: {len(messages)}")
print(f"Пример сообщений: {messages[:5]}")

# Анализ тональности
batch_size = 32
results = []
for i in range(0, len(messages), batch_size):
    batch = messages[i:i + batch_size]
    print(f"Обработка батча {i // batch_size + 1} из {len(messages) // batch_size + 1}...")
    batch_results = sentiment_analyzer(batch)
    # Добавляем сообщение, метку и уверенность в результаты
    for msg, res in zip(batch, batch_results):
        results.append({
            "message": msg,
            "sentiment": res["label"],
            "confidence": round(res["score"] * 100, 2)  # Уверенность в процентах
        })

# Подсчёт тональности
emotions = {"POSITIVE": 0, "NEUTRAL": 0, "NEGATIVE": 0}
for result in results:
    emotions[result['sentiment']] += 1

print("Эмоциональный фон чата:")
print(emotions)

# Сохраняем результаты с confidence в файл (опционально)
results_df = pd.DataFrame(results)
results_df.to_csv("chat_analysis_results.csv", index=False, encoding="utf-8")
print("Подробные результаты сохранены в 'chat_analysis_results.csv'.")

# Визуализация
labels = emotions.keys()
sizes = emotions.values()
colors = ['#8fd694', '#d3d3d3', '#ff6b6b']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Эмоциональный фон чата")

# Отображение графика
plt.show()

# Вывод результатов по каждому сообщению
print("\nРезультаты анализа (топ 5 сообщений):")
for result in results[:5]:
    print(f"Сообщение: {result['message']}")
    print(f"Тональность: {result['sentiment']}, Уверенность: {result['confidence']}%\n")
