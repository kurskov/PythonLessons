"""
Объявите в программе следующий список из строк:

t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]

Необходимо преобразовать его в двумерный (вложенный) список lst,
где каждая строка представляется списком из слов (слова разделяются пробелом),
но сохранять слова только длиной более трех символов. Решить данную задачу
следует с использованием list comprehension. Результат отобразить с помощью
команды:

print(lst)

То есть, на выходе список должен быть:

[['Скажи-ка,', 'дядя,', 'ведь', 'даром'], ...]
"""

t = ["– Скажи-ка, дядя, ведь не даром",
     "Я Python выучил с каналом",
     "Балакирев что раздавал?",
     "Ведь были ж заданья боевые,",
     "Да, говорят, еще какие!",
     "Недаром помнит вся Россия",
     "Как мы рубили их тогда!"
     ]

lst = [[w for w in s.split() if len(w) > 3] for s in t]

print(lst)