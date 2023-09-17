pitch = int(input())

upper_limits = {"low": 65, "hi": 91}
lower_limits = {"low": 97, "hi": 123}

with open("public.txt", encoding="UTF-8") as file_input:
    lines = file_input.readlines()

output_line = ""

for input_line in lines:

    for letter in input_line:
        if letter.isupper():
            if ord(letter) + pitch < upper_limits["low"]:
                oversize = -pitch - (ord(letter) - upper_limits["low"])
                output_line += chr(upper_limits["hi"] - oversize)
            elif ord(letter) + pitch > upper_limits["hi"]:
                oversize = pitch - (upper_limits["hi"] - ord(letter))
                output_line += chr(upper_limits["low"] + oversize)
            else:
                output_line += chr(ord(letter) + pitch)
        elif letter.islower():
            if ord(letter) + pitch < lower_limits["low"]:
                oversize = -pitch - (ord(letter) - lower_limits["low"])
                output_line += chr(lower_limits["hi"] - oversize)
            elif ord(letter) + pitch > lower_limits["hi"]:
                oversize = pitch - (lower_limits["hi"] - ord(letter))
                output_line += chr(lower_limits["low"] + oversize)
            else:
                output_line += chr(ord(letter) + pitch)
        else:
            output_line += letter
    output_line =+ "\n"

with open("private.txt", "w", encoding="UTF-8") as file_out:
    file_out.writelines(output_line)
