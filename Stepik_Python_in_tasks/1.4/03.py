year = int(input())

days = 366 if not (year % 4) and not (not (year % 100) and year % 400) else 365

print(days if year >= 1582 else "error")
