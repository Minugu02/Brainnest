filename = 'lorem.txt'
with open(filename, 'r') as file:
    data = file.read()

lines = len(data.split('\n'))
words = len(data.split())
characters = len(data)

print(f"Number of lines: {lines}")
print(f"Number of words: {words}")
print(f"Number of characters: {characters}")
