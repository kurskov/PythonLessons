"""Это будет наш секрет

Шифр Цезаря, также известный как шифр сдвига, код Цезаря — один
из самых простых и наиболее широко известных методов шифрования.
Он назван в честь римского полководца Гая Юлия Цезаря, использовавшего
его для секретной переписки со своими генералами.

Давайте реализуем эту систему шифрования. Однако для простоты мы
будем сдвигать только латинские символы по кругу.

Формат ввода
Вводится размер сдвига для шифрования.
В файле public.txt содержится текст на английском языке.

Формат вывода
В файл private.txt запишите зашифрованный текст.
"""

pitch = int(input())
pitch %= 26

upper_limits = {"low": 65, "hi": 90}
lower_limits = {"low": 97, "hi": 122}

with open("public.txt", encoding="UTF-8") as file_input:
    lines = file_input.readlines()

output_line = ""

for input_line in lines:

    for letter in input_line:
        if letter.isupper():
            if ord(letter) + pitch < upper_limits["low"]:
                oversize = -pitch - (ord(letter) - upper_limits["low"])
                output_line += chr(upper_limits["hi"] - oversize + 1)
            elif ord(letter) + pitch > upper_limits["hi"]:
                oversize = pitch - (upper_limits["hi"] - ord(letter))
                output_line += chr(upper_limits["low"] + oversize - 1)
            else:
                output_line += chr(ord(letter) + pitch)
        elif letter.islower():
            if ord(letter) + pitch < lower_limits["low"]:
                oversize = -pitch - (ord(letter) - lower_limits["low"])
                output_line += chr(lower_limits["hi"] - oversize + 1)
            elif ord(letter) + pitch > lower_limits["hi"]:
                oversize = pitch - (lower_limits["hi"] - ord(letter))
                output_line += chr(lower_limits["low"] + oversize - 1)
            else:
                output_line += chr(ord(letter) + pitch)
        else:
            output_line += letter

with open("private.txt", "w", encoding="UTF-8") as file_out:
    file_out.writelines(output_line)
