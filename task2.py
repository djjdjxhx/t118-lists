requests = ["ПК-1", "ПК-2", "ПК-3"]

requests.append("ПК-4")
requests.insert(0, "Срочно")
requests[requests.index("ПК-2")] = "ПК-2 исправлен"
requests.remove("ПК-3")
last_item = requests.pop()

print("Извлечённое значение:", last_item)
print("Оставшийся список:", requests)