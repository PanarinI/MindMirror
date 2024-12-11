import subprocess

# Команда для запуска Streamlit
command = ["streamlit", "run", "analyze.py"]

# Запуск Streamlit через subprocess
process = subprocess.Popen(command, shell=True)

# Далее ваш код может продолжить выполнение
print("Streamlit сервер запущен в фоновом режиме...")


