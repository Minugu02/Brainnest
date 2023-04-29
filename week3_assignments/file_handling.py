
# 1. Write a Python program that reads a text file and prints the number of lines, words, and characters in the file.

filename = 'lorem.txt'
with open(filename, 'r') as file:
    data = file.read()

lines = len(data.split('\n'))
words = len(data.split())
characters = len(data)

print(f"Number of lines: {lines}")
print(f"Number of words: {words}")
print(f"Number of characters: {characters}")

'''
output:

Number of lines: 15
Number of words: 173
Number of characters: 1011

'''

# 2. Write a Python program that reads a CSV file and converts it into a dictionary. Each row of the CSV file should be a key-value pair in the dictionary.

import csv

def csv_to_dict(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader) # get the header row
        dict_list = []
        for row in reader:
            # create a dictionary for each row
            dict_row = {}
            for i in range(len(header)):
                dict_row[header[i]] = row[i]
            dict_list.append(dict_row)
        return dict_list


file_path = 'data.csv'
csv_dict = csv_to_dict(file_path)
print(csv_dict)

'''
output:

[{'Fname': 'Jack', 'Lname': 'Antoff', 'City': 'Hamburg'}, {'Fname': 'Clara', 'Lname': 'Blake', 'City': 'Milan'}, {'Fname': 'Justin', 'Lname': 'Timber', 'City': 'Lyon'}, {'Fname': 'Katy', 'Lname': 'Perry', 'City': 'Paris'}]

'''

# 3. Write a Python program that reads a binary file and converts it into a hexadecimal string. The program should output the hexadecimal string to a text file.

import binascii

with open('file.bin', 'rb') as f:
    binary_data = f.read()
    hex_string = binascii.hexlify(binary_data).decode('utf-8')

with open('hex_string.txt', 'w') as f:
    f.write(hex_string)


# 4. Write a Python program that reads a text file containing numbers and calculates the sum of all the numbers in the file.

with open('numbers.txt', 'r') as f:
    total = 0

    for line in f:
        total += int(line)

print(f"The sum of all the numbers in the file is {total}")

'''
output

The sum of all the numbers in the file is 323

'''

# 5. Write a Python program that reads a text file and removes all the blank lines. The modified text should be written back to the file.

filename = "lorem.txt"

with open(filename, "r") as f:
    lines = f.readlines()

# remove blank lines
lines = [line for line in lines if line.strip()]

with open(filename, "w") as f:
    f.writelines(lines)

