greeting = "Hello"
name = "Dio"
message = greeting + " " + name + "!!!"
print("concatenated message:", message)
print()
word = "Supercalifragilisticexpialidocious"
print("First letter:", word[0])
print("Last letter:", word[-1])
print("Beggining:", word[:8])
print("Middle:", word[9:20])
print("End:", word[27:])
print("All:", word[:])
print("Backwards:", word[::-1])
print()
country = "Germany"
length_of_word = len(country)
print(length_of_word)
print()
phrase = "sPoNgEbOB"
print("\nUpercase:", phrase.upper())
print("Lowercase:", phrase.lower())
print("Capitalize first letter: ", phrase.capitalize())
print()
string = "I'm a goofy goober"
new_string = string.replace("I'm", "you're")
print(string)
print(new_string)
print()
name = "Dio"
age = 348
city = "Cairo"
print(f"Hello, my name is {name}. I am {age} years old and live in {city}")
print(f"Next year, I'll be {age + 1}. My name in uppercase is {name.upper()}")
print()
quote = input("Give me your favorite quote:")
print(f"your quote is {len(quote)} characters long.")
first_name = input("what is your first name?")
last_name = input("and last name?")
print(last_name + "," + first_name)
print()
sample = input("Give me a word")
print(sample.upper())
print(sample.lower())
print(sample[::-1])