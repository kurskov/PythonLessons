# pitch = input()

upper_low_limit = 65
upper_high_limit = 91
lower_low_limit = 97
lower_high_limit = 123

input_line = "Hello, world!"
output_line = ""

for letter in input_line:
    if letter.isupper():
        if ord(letter) + pitch < upper_low_limit:
            output_line += 