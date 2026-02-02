def main():
    amount_due = 75
    accepted_coins = [50, 20, 10, 5]
    while amount_due > 0:
        print (f"Amount Due: {amount_due}p")
        coin = int(input("Insert Coin:"))
        if coin in accepted_coins: amount_due -= coin
    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}p")
if __name__ == "__main__":
    main()
