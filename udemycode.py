x = 15
price = 9.99

discount = 0.2

result = price * (1 - discount)
print(result)

name = "Rolf"
name = "Bob"
print(name)
print(name * 2)

a = 25
b = a
print(a)
print(b)

b = 17
print(b)

name = "Rolf"
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)
with_name_two = greeting.format("Krista")

print(with_name_two)

longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format("Rolf", "Wednesday")
print(formatted)

name = input("What is your name please?")
print(name)

size_input = input("How big is your house?")
square_feet = int(size_input)
square_metres = square_feet / 10.8
print(f"{square_feet} square feet is {square_metres:.3f} square metres.")
