def deposit():
    amount = int(input("Enter Amount : "))
    return amount


def withdraw(w):
    print(f"Now You have {w}TK.")


def show_amount(t):
    print(f"You have {t}TK.")


def main():
    total_amount = 0

    while True:
        print("\n\nBanking Program.")
        print("1. Deposit.")
        print("2. Withdraw.")
        print("3. Show amount.")
        print("4. Exit.")


        ref = int(input(">>>>>>Choice (1-4): "))

        if ref == 1:
            total_amount += deposit()
        elif ref == 2:
            amount_of_withdraw = int(input("Enter withdraw amount : "))
            if amount_of_withdraw > total_amount:
                print("Sorry! You don't have enough money.\nPlease Deposit some money.")
            else:
                total_amount -= amount_of_withdraw
                withdraw(total_amount)

        elif ref == 3:
            show_amount(total_amount)
        elif ref == 4:
            print("Exit.")
            break
        else:
            print("Something was wrong! Please try again.")
            break


main()
