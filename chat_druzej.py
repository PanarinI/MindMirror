import json
import pandas as pd
import streamlit as st
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Загрузить JSON файл
with open("result_group.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Преобразовать данные в таблицу с помощью pandas
messages = []
for message in data["messages"]:
    msg = {
        "date": message.get("date"),
        "from": message.get("from", "Unknown"),
        "text": message.get("text", ""),
        "type": message.get("type", "")
    }

    # Если 'text' является списком, объединяем его в строку
    if isinstance(msg["text"], list):
        # Преобразуем все элементы списка в строку и соединяем их
        msg["text"] = ' '.join(str(item) for item in msg["text"])

    messages.append(msg)

# Создать DataFrame из списка сообщений
df = pd.DataFrame(messages)

# Отобразить таблицу в Streamlit
st.write("### Таблица сообщений", df)

# Анализ тональности с использованием TextBlob
df["sentiment_textblob"] = df["text"].apply(lambda x: TextBlob(x).sentiment.polarity)

# Анализ тональности с использованием VADER Sentiment
analyzer = SentimentIntensityAnalyzer()
df["sentiment_vader"] = df["text"].apply(lambda x: analyzer.polarity_scores(x)["compound"])

# Отобразить обновленную таблицу с результатами анализа
st.write("### Результаты анализа тональности", df)
