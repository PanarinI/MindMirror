import pandas as pd
import streamlit as st

# Загрузите данные
df = pd.read_json("result_group.json")

# Создаем веб-приложение с таблицей
st.title("Telegram Chat Analysis")
st.write(df)  # Показывает таблицу





#### в чат друзей


