# deposit - сумма вклада, interest_rate -процентная ставка,
# amount_months - количество месяцев
def compute_income(deposit, interest_rate, amount_months):
    # вычислить прибыль
    income = (deposit * (1 + interest_rate / (12 * 100))**amount_months -
              deposit)

    return income


x = float(input())

k = float(input())

n = int(input())

# вычислить прибыль с помощью функции

s = compute_income(x, k, n)

# вывести результат

print(round(s))
