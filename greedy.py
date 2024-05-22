def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"], reverse=True)
    total_calories = 0
    total_cost = 0
    chosen_items = []

    for item, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            total_calories += data["calories"]
            total_cost += data["cost"]
            chosen_items.append(item)

    return total_calories, chosen_items

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(budget + 1):
            if items[list(items.keys())[i - 1]]["cost"] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[list(items.keys())[i - 1]]["cost"]] + items[list(items.keys())[i - 1]]["calories"])

    total_calories = dp[n][budget]
    chosen_items = []

    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            chosen_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]

    return total_calories, chosen_items


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 145

total_calories, chosen_items = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Total calories:", total_calories)
print("Chosen items:", chosen_items)

total_calories_dp, chosen_items_dp = dynamic_programming(items, budget)
print("Dynamic Programming:")
print("Total calories:", total_calories_dp)
print("Chosen items:", chosen_items_dp)