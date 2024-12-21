import openpyxl
import pandas as pd

# Загрузите файл CSV
file_path = 'F:/PythonProject/MirrorMind/chat_analysis_results.csv'
df = pd.read_csv(file_path)

# Функция декодирования текста
def decode_text(text):
    try:
        return text.encode('latin1').decode('utf-8')
    except:
        return text

# Примените функцию к каждому значению
df = df.applymap(lambda x: decode_text(x) if isinstance(x, str) else x)

# Сохраните исправленный файл в Excel
df.to_excel('chat_analysis_results_fixed.xlsx', index=False)
print("Файл перекодирован и сохранён как chat_analysis_results_fixed.xlsx")
