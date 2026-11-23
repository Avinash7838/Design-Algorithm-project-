
# Fractional Knapsack using Greedy Algorithm

def fractional_knapsack(products, capacity):

    # Sort products by profit per unit weight
    products = sorted(
        products,
        key=lambda x: x["profit"] / x["weight"],
        reverse=True
    )

    total_profit = 0
    selected = []
    remaining = capacity

    for product in products:

        if remaining <= 0:
            break

        if product["weight"] <= remaining:

            selected.append({
                "name": product["name"],
                "weight": product["weight"],
                "profit": product["profit"],
                "fraction": 1
            })

            total_profit += product["profit"]
            remaining -= product["weight"]

        else:

            fraction = remaining / product["weight"]

            selected.append({
                "name": product["name"],
                "weight": remaining,
                "profit": product["profit"] * fraction,
                "fraction": fraction
            })

            total_profit += product["profit"] * fraction
            remaining = 0

    return selected, total_profit


# 0/1 Knapsack using Dynamic Programming

def zero_one_knapsack(products, capacity):

    n = len(products)

    # Create DP table
    dp = [[0 for x in range(capacity + 1)]
          for y in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):

        weight = products[i - 1]["weight"]
        profit = products[i - 1]["profit"]

        for w in range(capacity + 1):

            if weight <= w:

                dp[i][w] = max(
                    profit + dp[i - 1][w - weight],
                    dp[i - 1][w]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    # Find selected products
    selected = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            product = products[i - 1]
            selected.append(product)
            w -= product["weight"]

    selected.reverse()

    return selected, dp[n][capacity]
