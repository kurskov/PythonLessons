"""
Буквенная статистика

Вашему решению будет предоставлена строка text.
Напишите выражение для генерации словаря, который содержит информацию
о частоте употребления букв в заданной строке.
При анализе не учитывайте регистр, а ключами словаря сделайте использованные
в строке буквы в нижнем регистре.

Примечание
В решении не должно быть ничего, кроме выражения.
"""

{letter: text.lower().count(letter) for letter in text.lower() if letter.isalpha()}
