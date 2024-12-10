import json

# Откройте исходный JSON файл с чатом
with open("result_group.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Укажите, сколько сообщений оставить
num_messages_to_keep = 1000  # Например, оставляем первые 3 сообщения

# Укорачиваем список сообщений
data["messages"] = data["messages"][:num_messages_to_keep]

# Записываем обновленный JSON в новый файл
with open("result_group_shortened.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Файл успешно укорочен и сохранён как 'result_group_shortened.json'.")
