import json

def convert_csv_to_jsonl(input_csv_file, output_jsonl_file):
    messages = []

    with open(input_csv_file, 'r') as csv_file, open(output_jsonl_file, 'w') as jsonl_file:
        csv_reader = csv.DictReader(csv_file)

        # Ограничиваем количество строк 7000
        rows = list(csv_reader)[-7000:]

        for row in rows:
            date = row['date']
            open_value = row['open']
            high = row['high']
            low = row['low']
            close = row['close']

            # Создаем сообщение для системы
            system_message = {
                "role": "system",
                "content": "IDN is a chatbot that helps in trading."
            }

            # Создаем сообщение для пользователя
            user_message = {
                "role": "user",
                "content": f"What will be open, high, low, close of BTC at the moment of {date}?"
            }

            # Создаем сообщение для ассистента
            assistant_message = {
                "role": "assistant",
                "content": f"Open: {open_value}, High: {high}, Low: {low}, Close: {close}"
            }

            # Добавляем тройку "system", "user" и "assistant" в блок "messages"
            messages.append({"messages": [system_message, user_message, assistant_message]})

        # Записываем все сообщения в JSONL файл
        for entry in messages:
            json.dump(entry, jsonl_file, ensure_ascii=False)
            jsonl_file.write('\n')

if __name__ == "__main__":
    input_csv_file = "power_data.csv"
    output_jsonl_file = "data.jsonl"

    convert_csv_to_jsonl(input_csv_file, output_jsonl_file)
