# string_inverter.py

def invert_string(s):
    return s[::-1]

# Приклад використання
if __name__ == "__main__":
    user_input = input("Enter a string to invert: ")
    print("Inverted string: ", invert_string(user_input))
