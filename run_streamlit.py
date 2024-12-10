import subprocess

# Команда для запуска Streamlit
command = ["streamlit", "run", "chat_druzej.py"]

# Запуск Streamlit через subprocess
process = subprocess.Popen(command, shell=True)

# Далее ваш код может продолжить выполнение
print("Streamlit сервер запущен в фоновом режиме...")


# command = ["streamlit", "run", "main.py"] # streamlit run main.py
# streamlit run chat_druzej.py