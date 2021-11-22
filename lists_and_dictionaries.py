#lesson 5 (cложные типы данных)
# списки
list = [3, 5, 7, 9, 10.5]
print (list)
list.append ("Python")
print (list)

#словари
dictionary = {"city": "Москва", "temperature": 20}
print (dictionary["city"])
dictionary["temperature"] = dictionary["temperature"] - 5 #уменьшаем температуру на 5°С
print (dictionary)

#задание на работу со словарями
print (dictionary.get("country", "Россия")) # вывод "Россия" для отсутвующего элемента                                   
dictionary["date"] = "27.05.2019" #добавление элемента в словарь
print (dictionary)  #проверка
print (len(dictionary)) #вывод длины словаря