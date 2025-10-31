names = ["Mark", "John", "Mia", "Steve", "Michael", "Alice", "mary"]

result = list(filter(lambda name: name.lower().startswith('m'), names))

print(result)