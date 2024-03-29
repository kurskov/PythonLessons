"""
Легенды велогонок возвращаются: кто быстрее?

В новом сезоне за первенство в велогонках вновь борются
лучшие из лучших. Протяжённость заключительной трассы — 43872м,
и все хотят знать, кто получит золотую медаль.

Нам известны средние скорости трёх претендентов на победу – Пети,
Васи и Толи. Кто из них победит?

Формат ввода
В первой строке записана средняя скорость Пети.
Во второй — Васи.
В третьей — Толи.

Формат вывода
Красивый пьедестал (ширина ступеней 8 символов).

Примечание
В данный момент визуализация тестов работает некорректно.

Ответ на первый тест:

          Петя          
  Толя  
                  Вася  
   II      I      III   
"""

finish = sorted({(int(input()), "Петя"),
                 (int(input()), "Вася"),
                 (int(input()), "Толя")})

print(f"          {finish[2][1]}          ")
print(f"  {finish[1][1]}  ")
print(f"                  {finish[0][1]}  ")
print("   II      I      III   ")
