# [json python]
# Структура json
# {
#     "firstName": "Jane",
#     "lastName": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "firstName": "Alice",
#             "age": 6
#         },
#         {
#             "firstName": "Bob",
#             "age": 8
#         }
#     ]
# }

# для использования json
import json

# Пример сериализации JSON Python
# Например есть файл data_file.json содержащий
# data = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#     }
# }

# Серилизация
# для читения файла json применять конструкции
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
# где (1) объект данных, который сериализуется и 
# (2), файловый объект, в который будут вписаны байты

# или
json_string = json.dumps(data)
json.dumps(data, indent=4)  # добавятся отсупы

# Десириализация
with open('config.json', 'r') as write_file:
    data = json.load(write_file)
    print(data['request_select'])

# Или
blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)