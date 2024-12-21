import json

# Открываем экспортированный файл
with open("data/GN.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Очищаем сообщения
cleaned_data = []
for message in data["messages"]:
    if message["type"] == "message" and "text" in message:
        cleaned_data.append({
            "timestamp": message["date"],
            "sender": message["from"],
            "message": message["text"]
        })

# Сохраняем очищенные данные
with open("cleaned_chat_data.json", "w", encoding="utf-8") as output:
    json.dump(cleaned_data, output, ensure_ascii=False, indent=4)
