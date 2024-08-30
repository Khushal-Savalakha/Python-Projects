import sys
import numpy as np
import datetime
from colorama import Fore, Style

class SuperApp:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m' 
    MAGNETA='\033[95m'

    def __init__(self):
        print(SuperApp.MAGNETA+"Hello!")
        print("Welcome to the Super App.")
        print(SuperApp.END)
        SuperApp.showing_menu(self)
    
    @staticmethod
    def showing_menu(self):
        check = True
        while check:
            print(SuperApp.GREEN+"_________________________________________")
            print("|1. MyPay.                              |")
            print("|2. Book my show.                       |")
            print("|3. To Exit.                            |")
            print("|_______________________________________|")
            print(SuperApp.END)
            choice = input("Enter your choice what you want to do: ")
            if choice == "1":
                print("You have chosen MyPay")
                MyPay.my_pay_main()
            elif choice == "2":
                print("You have chosen Book my show")
                BookMyShow.book_my_show_main()
            elif choice == "3":
                print("Thank you! Visit Again.")
                check = False
            else:
                print("Invalid choice")

class MyPay:

    receipt_name=''
    transfer_amount=0
    bank_balance=1000000
    wallet_balance=10000
    num_of_transactions=0
    index=0
    mobile_no=''
    upi_id=''
    account_number=''
    choice=''
    transactions = np.empty((50, 8), dtype=object)
    transaction_choice=''

    @staticmethod
    def my_pay_main():
        print("Welcome to myPay !")
        check = True
        while check:
            print(SuperApp.GREEN+"_________________________________________")
            print("|1. Check Wallet Balance.               |")
            print("|2. Transfer Money.                     |")
            print("|3. Add money to Wallet.                |")
            print("|4. Add money Wallet to Bank Account.   |")
            print("|5. Check Transfer history.             |")
            print("|6. To Exit.                            |")
            print("|_______________________________________|")
            print(SuperApp.END)
            MyPay.choice = input("MyPay Choice: ")
            if MyPay.choice.lower() in ["back", "6"]:
                return
            MyPay.my_pay_menu()  # My pay's [1 to 6] functions execution method.

    @staticmethod
    def my_pay_menu():
        if MyPay.choice == "1":
            print("Your current Wallet Balance is:",MyPay.wallet_balance)
            print("Your current Bank Balance is:",MyPay.bank_balance)
        elif MyPay.choice == "2":
            print("You have chosen Transfer Money.")
            MyPay.transfer_money()  # Money Transaction
        elif MyPay.choice == "3":
            print("You have chosen Add money to Wallet.")
            MyPay.internal_transaction(3)  # Account To Wallet Internal Transaction
        elif MyPay.choice == "4":
            print("You have chosen Add money from Wallet to Bank Account.")
            MyPay.internal_transaction(4)  # Wallet To Account Internal Transaction
        elif MyPay.choice == "5":
            print("You have chosen to Check Transfer history.")
            MyPay.print_transfer_history()  # Showing all Money Transfer History
        else:
            print("Enter between 1 to 6 or back")

    @staticmethod
    def transfer_money():
        transfer_choice = input(SuperApp.GREEN+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                                "|1. Transfer to MobileNo     |\n"
                                "|2. Transfer to Upi          |\n"
                                "|3. Transfer to Account      |\n"
                                "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                                "Transfer Choice: ")
        print(SuperApp.END)
        if transfer_choice == "1":
            MyPay.recipient_name = input("\nEnter Recipient Name: ")
            MyPay.get_mobile_no()  # Getting valid Mobile Number
        elif transfer_choice == "2":
            MyPay.recipient_name = input("\nEnter Recipient Name: ")
            MyPay.get_upi()  # Getting valid UPI Id
        elif transfer_choice == "3":
            MyPay.recipient_name = input("\nEnter Recipient Name: ")
            MyPay.get_account_details()  # Getting valid Account Details
        elif transfer_choice.lower() == "back":
            return
        else:
            print("Invalid Choice.")

    @staticmethod
    def get_mobile_no():
        count = 0
        is_valid_mn = False
        while not is_valid_mn:
            mobile_no = input("Enter Mobile Number (or 'back' to return): ")
            if mobile_no.lower() == "back":
                return
            if len(mobile_no) == 10:
                for m in range(len(mobile_no)):
                    if m == 0:
                        if '7' <= mobile_no[m] <= '9':
                            count += 1
                            continue
                        else:
                            print(f"First digit should not be {mobile_no[m]}\n"
                                  f"It must be between [7-9].\n"
                                  f"And rest between [0-9].")
                            count = 0
                            break
                    else:
                        if '0' <= mobile_no[m] <= '9':
                            count += 1
                            continue
                        else:
                            print("Enter digits between [0-9]")
                            count = 0
                            break
                if count == 10:
                    print("Number Added successfully.")
                    is_valid_mn = True
            else:
                print("Enter 10 digits.")

        if is_valid_mn:
            MyPay.get_amount("Mobile Number", mobile_no)
    

    @staticmethod
    def get_upi():
        count = 0
        # UPI (typically username@bankname).
        is_valid_upi = False
        while not is_valid_upi:
            upi_id = input("Enter UPI ID (or 'back' to return): ")
            flag = upi_id.find("@")
            if upi_id.lower() == "back":
                return
            if flag != -1:
                if upi_id.endswith(("oksbi", "ybl", "okaxis", "okhdfcbank")):
                    is_valid_upi = True
                else:
                    print("Invalid bank name\nUPI (typically username@bankname).")
            else:
                print("Invalid UPI format")

        if is_valid_upi:
            MyPay.get_amount("UPI ID", upi_id)
            
    @staticmethod
    def get_account_details():
        bank_no_count = 0
        account_no_count = 0
        ifsc_no_count = 0
        is_valid_bank = False
        is_valid_account = False
        is_valid_ifsc = False

        bank_data = [
            ["SBI", "11"],
            ["ICICI", "12"],
            ["HDFC", "14"],
            ["BOB", "14"],
            ["AXIS", "15"]
        ]

        # Bank Name
        while not is_valid_bank:
            bank_name = input("Bank Name (SBI/ICICI/HDFC/BOB/AXIS) (or 'back' to return): ").upper()
            if bank_name == "BACK":
                return
            for m in range(len(bank_data)):
                if bank_name.lower() == bank_data[m][0].lower():
                    bank_no_count = m
                    is_valid_bank = True
                    break

        # Account Number
        if is_valid_bank:
            while not is_valid_account:
                account_number = input("Enter Account Number: ")
                if account_number == "back":
                    return
                temp = int(bank_data[bank_no_count][1])
                if len(account_number) == temp:
                    for m in range(len(account_number)):
                        if m == 0:
                            if '1' <= account_number[m] <= '9':
                                account_no_count += 1
                                continue
                            else:
                                print("Account number does not start with 0")
                                account_no_count = 0
                                break
                        else:
                            if '0' <= account_number[m] <= '9':
                                account_no_count += 1
                                continue
                            else:
                                print("Enter digits between [0-9].")
                                account_no_count = 0
                                break
                    if account_no_count == len(account_number):
                        # checks whether any condition falls down or not ?
                        print("Re-enter Account for verification")
                        acc_re_enter = input()
                        if acc_re_enter == account_number:
                            is_valid_account = True
                        else:
                            print("Didn't match!")
                            account_no_count = 0
                else:
                    print("Invalid Account Number length")

	#IFSC CODE Format: The IFSC is an 11-character code 
	# with the first four alphabetic characters representing the bank name,
	# and the last six characters (usually numeric, but can be alphabetic) 
	# representing the branch. 
	# The fifth character is 0 (zero) and reserved for future use.
	# IFSC number  Ex:sbie0qwerty Ex:sbiw0123456
        if is_valid_account:
            while not is_valid_ifsc:
                ifsc = input("Enter IFSC code: ").upper()
                if ifsc == "BACK":
                    return
                if len(ifsc) == 11:
                    for m in range(len(ifsc)):
                        if m >= 0 and m <= 3:
                            if 'A' <= ifsc[m] <= 'Z':
                                ifsc_no_count += 1
                                continue
                        elif m == 4:
                            if ifsc[m] == '0':
                                ifsc_no_count += 1
                                continue
                        elif m >= 5 and m <= 10:
                            if 'A' <= ifsc[m] <= 'Z' or '0' <= ifsc[m] <= '9':
                                ifsc_no_count += 1
                                continue
                    if ifsc_no_count == len(ifsc):
                        print("IFSC Entered Successfully")
                        is_valid_ifsc = True
                    else:
                        print("Invalid IFSC")
                        ifsc_no_count = 0
                else:
                    print("Invalid IFSC length")

        if is_valid_ifsc and is_valid_account and is_valid_bank:
            MyPay.get_amount("BANK ACCOUNT", account_number)
        
    @staticmethod
    def get_amount(payment_method, payment_id):
        choice=''
        while not ((choice.upper() == 'Y') or (choice.upper() == 'N')):
            choice = input("Do you want to proceed? (Y/N): ").upper()
            if choice.upper() == "Y":
                try:
                    MyPay.transfer_amount = float(input("Enter the amount to be transferred: "))
                    MyPay.transaction_selection(MyPay.transfer_amount)
                    MyPay.payment_verification(MyPay.transfer_amount, payment_method, payment_id)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            elif choice.upper() == "N":
                return
            else:
                print("Invalid choice. Please enter Y or N.")

    @staticmethod
    def transaction_selection(transfer_amount):
        if transfer_amount <= MyPay.wallet_balance and transfer_amount <= MyPay.bank_balance:
            while True:
                MyPay.transaction_choice = input("Transaction from (Wallet/BankAccount)? : ").lower()
                if MyPay.transaction_choice in ["wallet",'bankaccount']:
                    break
                else:
                    print("Invalid choice. Please enter from Wallet or BankAccount.")
        elif transfer_amount <= MyPay.wallet_balance and transfer_amount >= MyPay.bank_balance:
            MyPay.transaction_choice="wallet"
        elif transfer_amount <= MyPay.bank_balance and transfer_amount > MyPay.wallet_balance:
            MyPay.transaction_choice="bankAccount"
        else:
            print("Insufficient balance!\nPayment not possible.\nManage more funds.")
            MyPay.transaction_choice=""
            return
                
    @staticmethod
    def payment_verification(transfer_amount, payment_method, payment_id):
       if MyPay.payment_validation(MyPay.transaction_choice):
           MyPay.transaction_process(transfer_amount, MyPay.transaction_choice)
           if payment_id == "bookMyShowpvt@okaxis":
               MyPay.get_history(transfer_amount, MyPay.transaction_choice, "Book My show Private limited", payment_method, payment_id)
           elif payment_id == "Last check":
               # Handle other payment methods
               pass
           else:
               MyPay.get_history(transfer_amount, MyPay.transaction_choice,MyPay.recipient_name, payment_method, payment_id)
           print("Transaction Done Successfully")
       else:
           print("Too many attempts sir!\nTry again after 24 hours")
           sys.exit(0)  # Exiting the program if payment attempts exceed
        
    @staticmethod
    def transaction_process(transfer_amount, transaction_choice):
        if transaction_choice == "wallet":
            MyPay.wallet_balance -= transfer_amount
        elif transaction_choice == "bankaccount":
            MyPay.bank_balance -= transfer_amount
    
    @staticmethod
    def payment_validation(transaction_choice):
        n = 1
        bank_pin = "654321"
        wallet_pin = "123456"
        while n <= 3:
            pin_check = input("Enter the pin:")
            if transaction_choice == "wallet":
                if pin_check==wallet_pin:
                    return True
                else:
                    print("Invalid Pin")
                    n += 1
            elif transaction_choice == "bankaccount":
                if pin_check==bank_pin:
                    return True
                else:
                    print("Invalid Pin")
                    n += 1
        return False   

        
    @staticmethod
    def internal_transaction(n):
        if n == 3:
            print("Enter amount you want to add to your wallet:")
            b_acc_to_wallet = int(input())
            if b_acc_to_wallet <= MyPay.bank_balance:
                MyPay.wallet_balance += b_acc_to_wallet
                MyPay.bank_balance -= b_acc_to_wallet
                print("Done successfully")
            else:
                print("Insufficient balance in your bank account.")
        elif n == 4:
            print("Enter amount you want to add to your bank account from wallet:")
            wallet_to_b_acc = int(input())
            if wallet_to_b_acc <= MyPay.wallet_balance:
                MyPay.bank_balance += wallet_to_b_acc
                MyPay.wallet_balance -= wallet_to_b_acc
                print("Done successfully")
            else:
                print("Insufficient balance in your wallet.")   
    

    @staticmethod
    def get_history(transefer_amount,transaction_choice,receipt_name,payment_method,payment_id):
        Index=MyPay.num_of_transactions
        MyPay.num_of_transactions+=1
        current_datetime = datetime.datetime.now()
        date_and_time = str(current_datetime).split(' ')
        date=date_and_time[0]
        time=date_and_time[1]
        MyPay.transactions[Index][0]=MyPay.num_of_transactions
        MyPay.transactions[Index][1]=transefer_amount
        MyPay.transactions[Index][2]=transaction_choice
        MyPay.transactions[Index][3]=receipt_name
        MyPay.transactions[Index][4]=payment_method
        MyPay.transactions[Index][5]=payment_id
        MyPay.transactions[Index][6]=date
        MyPay.transactions[Index][7]=time


    @staticmethod
    def print_transfer_history():
        print("_______________________________________________________________________")
        print("Transaction History:")
        for i in range(MyPay.num_of_transactions):
            print(f"{MyPay.transactions[i][0]}. RS {MyPay.transactions[i][1]}/- Transfer from "
                  f"{MyPay.transactions[i][2]} to {MyPay.transactions[i][3]}'s {MyPay.transactions[i][4]}: "
                  f"{MyPay.transactions[i][5]}. Date: {MyPay.transactions[i][6]}, Time: {MyPay.transactions[i][7]}.")
        print("_______________________________________________________________________")



class BookMyShow(MyPay):
    cinemas = ["PVR", "Cinepolis", "Raj Mandir Cinema", "Sunset Drive-In Cinema"]
    movies = [
        "Sholay",
        "Prem Rog",
        "Lagaan",
        "3 Idiots",
        "URI",
        "The Nun",
        "Avatar"
    ]
    cin_movi_time = [
        [
            # PVR
            ["Lagaan", "06.00PM TO 09.00PM", "07.30PM TO 10.30PM", "11.00AM TO 02.00PM"],
            ["3 Idiots", "09.00PM TO 11.30PM", "06.30PM TO 09.00PM", "01.00AM TO 03.30AM"],
            ["URI", "08.00PM TO 10.30PM", "08.30PM TO 11.00PM", "09.00AM TO 11.30AM"]
        ],
        [
            # Cinepolis
            ["URI", "08.00PM TO 11.00PM", "09.30PM TO 12.30PM", "01.00AM TO 03.00PM"],
            ["Prem Rog", "06.00PM TO 09.00PM", "07.30PM TO 10.30PM", "11.00AM TO 02.00PM"],
            ["Sholay", "04.00PM TO 06.30PM", "05.30PM TO 08.00PM", "09.00AM TO 11.30AM"]
        ],
        [
            # Raj Mandir Cinema
            ["Avatar", "06.00PM TO 09.00PM", "07.30PM TO 10.30PM", "08.30PM TO 11.00PM"],
            ["Sholay", "09.00AM TO 11.30AM", "06.00PM TO 09.00PM", "05.30PM TO 08.00PM"],
            ["Lagaan", "06.30PM TO 09.00PM", "06.00PM TO 09.00PM", "06.30PM TO 09.00PM"]
        ],
        [
            # Sunset Drive-In Cinema
            ["The Nun", "04.00PM TO 06.30PM", "07.30PM TO 10.30PM", "09.00AM TO 11.30AM"],
            ["Prem Rog", "09.00PM TO 11.30PM", "09.30PM TO 12.00PM", "01.00AM TO 03.00PM"],
            ["3 Idiots", "08.00PM TO 11.00PM", "06.00PM TO 09.00PM", "06.30PM TO 09.00PM"]
        ]
    ]

    prices = [
        [150.0, 110.0, 90.00],
        [95.0, 170.0, 190.00],
        [50.0, 210.0, 190.00],
        [100.0, 180.0, 190.00]
    ]

    seats = [
        [True, True, True, False, True, True, True],
        [True, True, True, False, True, True, True],
        [True, True, True, False, True, True, True],
        [False, False, False, False, False, False, False],
        [True, True, True, False, True, True, True],
        [True, True, True, False, True, True, True],
        [True, True, True, False, True, True, True]
    ]

    selected_cinema = None
    selected_movie = None
    selected_time = None
    no_of_tickets = 0
    total_price = 0.0
    movie_opt=None

    @staticmethod
    def book_my_show_main():
        check = False
        choice = ""
        print(SuperApp.MAGNETA+"Welcome to the Book My Show.")
        print(SuperApp.END)

        while not check:
            print("_______________________________________________________________________")
            print("1). Select Movie via Cinema")
            print("2). Select Cinema via Movie")
            print("_______________________________________________________________________")
            choice = input("Book my show choice: ")

            if choice.lower() == "back":
                return
            elif choice == "1":
                BookMyShow.cinemas_menu()
                BookMyShow.cinema_choice()
            elif choice == "2":
                BookMyShow.movies_menu()
                BookMyShow.movie_choice()

    @staticmethod
    def cinemas_menu():
        print("____________________________________________________________________________________")
        for i in range(len(BookMyShow.cin_movi_time)):
            print(f"{i+1}]. {BookMyShow.cinemas[i]}")
            for j in range(len(BookMyShow.cin_movi_time[i])):
                print(f"{j+1}).", end=" ")
                for k in range(len(BookMyShow.cin_movi_time[i][j])):
                    if k == 0:
                        print(f"{BookMyShow.cin_movi_time[i][j][k]}~~~>", end=" ")
                    else:
                        print(BookMyShow.cin_movi_time[i][j][k], end=" ")
                print(".")
            print("")
        print("____________________________________________________________________________________")
    
    # def __init__(self):
    #     self.book_my_show_main()
    @staticmethod
    def cinema_choice():
        flag=True
        while flag:
            cinema_opt = input("Enter Cinema No :(1/2/3/4)? : ")
            if cinema_opt == "1":
                BookMyShow.movie_and_time_choice(1)
                flag=False
            elif cinema_opt == "2":
                BookMyShow.movie_and_time_choice(2)
                flag=False
            elif cinema_opt == "3":
                BookMyShow.movie_and_time_choice(3)
                flag=False
            elif cinema_opt == "4":
                BookMyShow.movie_and_time_choice(4)
                flag=False
            elif cinema_opt.lower() == "back":
                return
            else:
                print("Invalid Input !")
    
    @staticmethod
    def movie_and_time_choice(cinema_number):
        movie_number = None
        timing = None
        for i in range(cinema_number-1, cinema_number):
            print(f"{i+1}]. {BookMyShow.cinemas[i]}")
            for j in range(len(BookMyShow.cin_movi_time[i])):
                print(f"{j+1}).", end=" ")
                for k in range(len(BookMyShow.cin_movi_time[i][j])):
                    if k == 0:
                        print(f"{BookMyShow.cin_movi_time[i][j][k]}~~~>", end=" ")
                    else:
                        print(BookMyShow.cin_movi_time[i][j][k], end=" ")
                print(".")
            print("")
        while True:
            try:
                movie_number = int(input("Enter Movie number :(1/2/3)? : "))
                if 1 <= movie_number <= 3:
                    break
                else:
                    print("Invalid Input! Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid Input! Please enter a number.")

        # Timing Printing
        print(BookMyShow.cin_movi_time[cinema_number-1][movie_number-1][0])
        print(f"1). {BookMyShow.cin_movi_time[cinema_number-1][movie_number-1][1]}")
        print(f"2). {BookMyShow.cin_movi_time[cinema_number-1][movie_number-1][2]}")
        print(f"3). {BookMyShow.cin_movi_time[cinema_number-1][movie_number-1][3]}")

        while True:
            try:
                timing = int(input("Enter Timings :(1/2/3)? : "))
                if 1 <= timing <= 3:
                    break
                else:
                    print("Invalid Input! Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid Input! Please enter a number.")

        # Storing All results
        selected_cinema = BookMyShow.cinemas[cinema_number-1]
        selected_movie = BookMyShow.cin_movi_time[cinema_number-1][movie_number-1][0]
        selected_time = BookMyShow.cin_movi_time[cinema_number-1][movie_number-1][timing]
        line = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print(f"{line}\n{selected_cinema}\n{selected_movie}\n{selected_time}.\n{line}")
        BookMyShow.movie_cost(cinema_number, movie_number)

    @staticmethod
    def movie_cost(cinema_number, movie_number):
        ticket_price = BookMyShow.prices[cinema_number - 1][movie_number - 1]
        print(f"Price for one Ticket : Rs{ticket_price}/-.")
    
        BookMyShow.no_of_tickets = int(input("No of Tickets: "))
    
        BookMyShow.total_price = ticket_price *BookMyShow.no_of_tickets
        print("Your total cost is:",BookMyShow.total_price)
        # Printing Seating
        BookMyShow.seat_print(BookMyShow.no_of_tickets)

    @staticmethod
    def seat_print(no_of_tickets):
        print("Available seat Matrix")

        for row in BookMyShow.seats:
            for seat in row:
                if seat:
                    print(SuperApp.GREEN+"[o]", end="")
                else:
                    print(SuperApp.RED+"[x]", end="")
            # print()
            print(SuperApp.END)

        print("Here [o] is Empty seats & [x] is occupied seats")
        # Seat Selection
        BookMyShow.seat_select(no_of_tickets)

    @staticmethod
    def seat_select(no_of_tickets):
        for i in range(no_of_tickets):
            while True:
                try:
                    row = int(input(f"Enter Seat {i+1} Row: "))
                    column = int(input(f"Enter Seat {i+1} Column: "))
                    if 0 < row < 8 and 0 < column < 8:
                        if not BookMyShow.seats[row - 1][column - 1]:
                            print(f"Sorry, seat {row}x{column} is not available. Please select another seat.")
                            continue
                        else:
                            BookMyShow.seats[row - 1][column - 1] = False
                            break
                    else:
                        print("Invalid seat selection. Row and column numbers must be between 1 and 7.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

        # New Seat Arrangement
        print("New seat matrix:")
        for row in BookMyShow.seats:
            for seat in row:
                if seat:
                    print(SuperApp.GREEN+"[o]", end="")
                else:
                    print(SuperApp.RED+"[x]", end="")
            # print()
            print(SuperApp.END)

        BookMyShow.ticket_payment()

    @staticmethod
    def ticket_payment():
        BookMyShow.transaction_selection(BookMyShow.total_price)
        BookMyShow.payment_verification(BookMyShow.total_price, "UPI ID", "bookMyShowpvt@okaxis")

    @staticmethod
    def movies_menu():
        print("____________________________________________________________________________________")
        for m in range(len(BookMyShow.movies)):
            print(f" {m+1}]. {BookMyShow.movies[m]}", end="")
        print("\n____________________________________________________________________________________")
   
    @staticmethod
    def movie_choice():
        # Movie selection
        flag=True
        while flag:
            BookMyShow.movie_opt = input("Enter movie No [1-7]? : ")
            if BookMyShow.movie_opt.lower() == "back":
                # flag=False
                return
            else:
                for i in range(1, 8):
                    if BookMyShow.movie_opt == str(i):
                        BookMyShow.cinema_and_time_choice(i)
                        break
                else:
                    print("Invalid choice!")

    @staticmethod
    def cinema_and_time_choice(movie_number):
        temp_cinema = [0, 0, 0, 0]
        number = 0
        movie_index = 0
        selected_movie = BookMyShow.movies[movie_number - 1]
        print(selected_movie)

        for cinema in range(len(BookMyShow.cin_movi_time)):
            for movie in range(len(BookMyShow.cin_movi_time[cinema])):
                if selected_movie.strip() == BookMyShow.cin_movi_time[cinema][movie][0].strip():
                    print(f"{number + 1}]. {BookMyShow.cinemas[cinema]}")
                    temp_cinema[number] = cinema + 1
                    number += 1

        while True:
            try:
                cinema_number = int(input("Enter Cinema number: "))
                if 1 <= cinema_number <= number:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and", number)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        selected_cinema = BookMyShow.cinemas[temp_cinema[cinema_number - 1] - 1]
        print(selected_cinema)

        if selected_cinema == "PVR":
            c_i = 0
        elif selected_cinema == "Cinepolis":
            c_i = 1
        elif selected_cinema == "Raj Mandir Cinema":
            c_i = 2
        elif selected_cinema == "Sunset Drive-In Cinema":
            c_i = 3
        else:
            print("Nothing to come here!")

        for m in range(len(BookMyShow.cin_movi_time[c_i])):
            if selected_movie.strip() == BookMyShow.cin_movi_time[c_i][m][0].strip():
                print(BookMyShow.cin_movi_time[c_i][m][0].strip())
                movie_index = m

        print(f"1]. {BookMyShow.cin_movi_time[c_i][movie_index][1]}")
        print(f"2]. {BookMyShow.cin_movi_time[c_i][movie_index][2]}")
        print(f"3]. {BookMyShow.cin_movi_time[c_i][movie_index][3]}\n")

        while True:
            try:
                timing = int(input("Enter Timings (1/2/3): "))
                if 1 <= timing <= 3:
                    break
                else:
                    print("Invalid input. Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        selected_time = BookMyShow.cin_movi_time[c_i][movie_index][timing]
        line = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print(f"{line}\n{selected_cinema}\n{selected_movie}\n{selected_time}.\n{line}")
        BookMyShow.movie_cost(c_i + 1, movie_index + 1)


a=SuperApp()
# BookMyShow().book_my_show_main()

        