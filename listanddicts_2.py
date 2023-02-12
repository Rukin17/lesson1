dicts = {"city": "Москва", "temperature": 20}
print(dicts["city"])
dicts["temperature"] -= 5
print(dicts)

print(dicts.get("country", 'Россия'))
dicts["date"] = "27.05.19"
print(len(dicts))