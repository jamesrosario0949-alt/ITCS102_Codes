base_cost = float(input("Enter the weight: "))
base_cost2 = float(input("Enter the distance: "))


if base_cost >= 30 or base_cost2 >= 1000:
    print("Oversized, FALSE, FALSE")
elif base_cost * 1.40 + 30 == base_cost2 * 1.40 + 30:
    print("International Express")
elif base_cost >= 20 and base_cost2 * 1.20 + 25:
    print("Express or Heavy International")
elif base_cost >= 2 and base_cost2 <= 100 and base_cost <= 1.9 and base_cost2 <= 100:
    print("Free shipping, FALSE, FALSE")
else:
    print("Standard Shipping")