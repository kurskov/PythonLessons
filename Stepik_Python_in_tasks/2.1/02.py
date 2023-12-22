def compute_income(deposit, interest_rate, amount_months):

    income = (deposit * (1 + interest_rate / (12 * 100))**amount_months -
              deposit)

    return income


k = float(input())
n = int(input())
s = float(input())

for x in range(1000, 30000):
    income = compute_income(x, k, n)
    if round(income) == s:
        print(x)
