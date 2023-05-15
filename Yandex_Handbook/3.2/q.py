"""
Друзья друзей

Теория шести рукопожатий — социологическая теория,
согласно которой любые два человека на Земле разделены не более,
чем пятью уровнями общих знакомых (и, соответственно, шестью уровнями связей).
Формальная математическая формулировка теории: диаметр графа знакомств
не превышает 6. Мы не станем так сильно углубляться в дружественные связи
и пока нам хватит только двух уровней.
Напишите программу, которая по списку дружественных пар для каждого человека
определяет список «друзей 2-го уровня».

Формат ввода
В каждой строке записывается два имени.
Окончанием ввода служит пустая строка.

Формат вывода
Выведите список всех людей и их «друзей 2-го уровня» в формате
«Человек: Друг1, Друг2, ...».
Список людей и друзей в каждой строке требуется вывести в алфавитном порядке
без повторений.
"""

first_hand = dict()
while (text := input()) != "":
    pair = text.split()
    for name in pair:
        if not first_hand.get(name, False):
            first_hand[name] = set(pair)
        else:
            first_hand[name] |= set(pair)

second_hand = dict()
for person in first_hand:
    second_hand[person] = set()
    for friend in first_hand[person]:
        second_hand[person] |= first_hand[friend]
    second_hand[person] -= first_hand[person]
    second_hand[person] = list(second_hand[person])
    second_hand[person].sort()

names = list(second_hand)
names.sort()

for name in names:
    friends = ""
    for friend in second_hand[name]:
        friends += friend + ", "
    print(f"{name}: {friends[:len(friends) - 2]}")
