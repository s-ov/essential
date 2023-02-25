# Создайте список товаров в интернет-магазине. Сериализуйте его при помощи pickle и сохраните в JSON.
import pickle as pkl
import json

ware_list = {'clothes': {'shoes': ['Nike', 'Puma'], 'T-shirts': ['Nike', 'Puma']},
             'electronics': {'TV sets': ['LG', 'JVC'], 'stereo systems': ['LG', 'JVC']},
             'household appliances': {'vacuum cleaners': ['LG', 'Phillips'], 'refrigerators': ['LG', 'Phillips']}
             }

with open('ware_list.pkl', 'wb') as file:
    pkl.dump(ware_list, file)

with open('ware_list.pkl', 'rb') as file:
    data = pkl.load(file)

json_data = json.dumps(data)
print(json_data)
