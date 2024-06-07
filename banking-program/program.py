def deposit():
    amount = float(input("Enter Amount : "))
    return int(amount)


def withdraw(w):
    print(f"Now You have {w}TK.")


def show_amount(t):
    print(f"You have {t}TK.")


def main():
    print(">> Attention! If You make any mistake You might be lost all of Your money. So, Be careful. <<")
    alert = input("Do You agree? (y/n):")
    if alert.lower() == "y":
        run = True
    else:
        run = False


    total_amount = 0

    while run:
        print("\n\nBanking Program.")
        print("1. Deposit.")
        print("2. Withdraw.")
        print("3. Show amount.")
        print("4. Exit.")

        ref = input(">>>>>>Choice (1-4): ")
        int_ref = int(ref)
        if int_ref == 1:
            total_amount += deposit()
        elif int_ref == 2:
            amount_of_withdraw = input("Enter withdraw amount : ")
            if float(amount_of_withdraw) > total_amount:
                print("Sorry! You don't have enough money.\nPlease Deposit some money.")
            else:
                total_amount -= float(amount_of_withdraw)
                withdraw(total_amount)

        elif int_ref == 3:
            show_amount(total_amount)
        elif int_ref == 4:
            print("If You quit the program. It will wastes all of your balance.")
            final_agreement = input("Do You agree? [y/n]:").lower()
            if final_agreement == "y":
                print("Bye, Good luck.")
                run = False
            else:
                continue

        else:
            print("Something was wrong! Please try again.")
            continue


main()
