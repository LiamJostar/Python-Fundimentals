#fuctions are blocks that can be reused
#to run it, you "call" it by writing the name, () and arguments

print("Functions (Procedures)")

print("\nExample 1")

def say_hi():
    print("hi")

def say_bye():
    print("bye")

say_hi()
say_bye()

print("\nExample 2")

def say_clear():
    print("Let me be clear,")

say_clear()

def express_this(e):
    return e

expression1 = express_this(14+20)
print(expression1)
expression2 = express_this(31*3)
print(expression2)

print("\nExample 3")

def greeter(n):
    return f"Hi {n}!"

first = greeter("Jojo")
second = greeter("Bizbo")
third = greeter("Hoppy")

print(first, second, third)

print("\nExample 4")

def remainder(a,b):
    return a % b

result = remainder(3,2)

print(result)

print("\nExample 5")

def is_far(distance):
    if distance < 1:
        return "Error"
    if distance >= 100:
        return "thats far"
    elif distance < 100 and distance >= 20:
        return "thats not too far"
    elif distance < 20 and distance > 0:
        return "thats nearby"
    # else:
    #     return "Error"

say_clear()
print(is_far(100))

print("\nExample 6")

def double_sequencer(number, times):
    value = number
    sequence = []
    for i in range(times):
        value = value * 2
        sequence.append(value)
        
    return sequence

result = double_sequencer(1,50)
print(result)