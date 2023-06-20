"""Транслитерация 2.0

Для международных документов русский текст преобразуется
с использованием латинского алфавита.
ГОСТ Р 52535.1-2006 задаёт правила транслитерации идентификационных карт.
Ниже приведена таблица замен:

    А — A
    Б — B
    В — V
    Г — G
    Д — D
    Е — E
    Ё — E
    Ж — ZH
    З — Z
    И — I
    Й — I
    К — K
    Л — L
    М — M
    Н — N
    О — O
    П — P
    Р — R
    С — S
    Т — T
    У — U
    Ф — F
    Х — KH
    Ц — TC
    Ч — CH
    Ш — SH
    Щ — SHCH
    Ы — Y
    Э — E
    Ю — IU
    Я — IA

Давайте транслитерируем русский текст.
Букву «ё» транслитерируйте как «e», «й» как «и», а «ъ» и «ь»
(и их заглавные версии «Ъ» и «Ь») должны исчезнуть из текста.
Строчные буквы заменяются на строчные, заглавные заменяются на заглавные.
Если заглавная буква превращается при транслитерации в несколько букв,
то заглавной должна остаться только первая из них (например, «Ц» → «Tc»).
Все некириллические символы должны остаться на месте.

Формат ввода
В одной папке с вашей программой лежит файл cyrillic.txt.
В нём, в числе прочих, содержится некоторое количество кириллических символов.

Формат вывода
В файл transliteration.txt записать результат транслитерации исходного файла.
"""

alpabet = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "e",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "i",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "tc",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ъ": "",
    "ы": "y",
    "ь": "",
    "э": "e",
    "ю": "iu",
    "я": "ia",
}

text = []
with open("cyrillic.txt", encoding="UTF-8") as file_input:
    lines = file_input.readlines()
    for line in lines:
        symbols = list(line)

        new_line = []
        for symbol in symbols:
            if symbol.isalpha() and symbol.isupper():
                capital = True
                symbol = symbol.lower()
            else:
                capital = False
            if symbol in alpabet:
                symbol = alpabet[symbol]
            if capital:
                symbol = symbol.capitalize()
            new_line.append(symbol)

        text.append("".join(new_line))

with open("transliteration.txt", "w", encoding="UTF-8") as file_output:
    file_output.writelines(text)
