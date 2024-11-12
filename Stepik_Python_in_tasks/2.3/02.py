def payment(t, s, n, k):

    return s / n + (s - (t - 1) * s / n) * k / 1200


s, n, k = int(input()), int(input()), int(input())

full_payment = 0

for t in range(1, n + 1):
    pay = payment(t, s, n, k)
    full_payment += pay
    print(f"{t:2d} месяц - {pay:8.2f} руб")

print(f"Доход банка - {full_payment - s:6.2f} руб")
