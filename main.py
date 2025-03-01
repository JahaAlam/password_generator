import random
letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/"]

random_choice = random.choice(letters)
print(random_choice)
print("Welcome to Password Generator !")

nr_letters = int(input("How many letter would you like  in your password !\n"))
nr_symbols = int(input("How many symbols would you like in your password ! \n"))
nr_numbers = int(input("how many number would you like in your password ! \n"))

# easy level password generator
password = ""
for char in range(0, nr_letters):
    password += random.choice(letters)

for char in range(0, nr_symbols):
    password += random.choice(symbols)


for char in range(0, nr_numbers):
    password += random.choice(numbers)


print(password)