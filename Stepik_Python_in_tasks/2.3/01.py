def compute_lambda(t, b, lamb_0):

    lamb = b * lamb_0 / (t - 100)

    return lamb


def compute_lambda_si(t):

    return compute_lambda(t, 33, 884)


t1, t2 = float(input("t1 = ")), float(input("t2 = "))

if t1 > t2:
    t1, t2 = t2, t1

if t1 <= 100:

    print("Неверные границы температур")

else:

    n = 20
    h = (t2 - t1)/(n - 1)
    t_list = [t1 + i * h for i in range(n)]

    lambda_list = [compute_lambda_si(t) for t in t_list]

    print("-" * 21)
    print(f"| {"t":>7} | {"L(t)":>7} |")
    print("-" * 21)
    for i in range(len(t_list)):
        print(f"| {t_list[i]:7.2f} | {lambda_list[i]:7.2f} |")
    print("-" * 21)
