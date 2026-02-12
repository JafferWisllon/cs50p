amount_due = 50

while amount_due > 0:
    print("Amount due", amount_due)
    coin = int(input("Insert Coin: "))

    if coin == 25 or coin == 10 or coin == 5:
        amount_due -= coin

print("Change Owed: ", abs(amount_due))