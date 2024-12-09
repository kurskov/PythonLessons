"""
На вход программе подается целое число k (1 <= k <= 365).
Прочитайте это число и определите, каким днем недели
(понедельник, вторник, среда, четверг, пятница, суббота или воскресенье)
является k-й день не високосного года, в котором 1 января является
понедельником.
"""

weeks_days = ["понедельник", "вторник", "среда", "четверг",
              "пятница", "суббота", "воскресенье"]

day = int(input())

print(weeks_days[day % 7 - 1])