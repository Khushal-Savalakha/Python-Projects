import os
import Online_Shopping_System_Search
import re
import datetime
from colorama import Fore, Style


class FetchData:
    search_data = dict()
    mobile_no = ""
    user_name = ""
    history_file = ""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m' 
    MAGNETA='\033[95m'


    @staticmethod
    def process_data():
        searched_data, search_result = Online_Shopping_System_Search.search()
        FetchData.fetch_data(searched_data, search_result)

    @staticmethod
    def file_name(file_name):
        FetchData.history_file = file_name

    @staticmethod
    def fetch_data(searched_data, search_result):
        file_path = "D:\\Online_Shopping_System_data\\"
        # global search_data
        index = 1
        price_data = []
        print(FetchData.GREEN+"--------------------Your Search Results--------------------")
        print(FetchData.END)
        for file_name in search_result:
            file = open(f"{file_path}{file_name}", "r")
            for line in file:
                line_split = line.lower().split(" ")
                if all(data in line_split for data in searched_data):
                    # print(line)
                    values = line.split("#")
                    price_data.append(values[2])
                    FetchData.search_data[index] = values
                    index += 1
            file.close()
        FetchData.display_menu_data(FetchData.search_data, price_data)

    @staticmethod
    def display_menu_data(search_data, price_data):
        for key, value in search_data.items():
            print(f'[{key}] {value[0]} price: {value[2]} {" ".join(value[3:])}')
        flag = True
        while flag:
            try:
                ans = int(input(FetchData.GREEN+"""-----------------------------------------\n"|   1] Price low to high.               |\n"|   2] Price High to low.               |\n"|   3] You want to select item.         |\n"|   4] Go back to search bar.           |\n"|   5] Payment History.                 |\n"|   6] To Exit.                         |\n"-----------------------------------------\n"Enter your choice: """))
                print(FetchData.END)
                if ans in [1, 2]:
                    FetchData.sorting_dictionary(search_data, price_data, ans)
                elif ans == 3:
                    Payment.select_item(search_data)
                elif ans == 4:
                    FetchData.process_data()
                elif ans==5:
                    FetchData.payment_history()
                elif ans==6:
                    print(FetchData.YELLOW+"Thank you! Visit Again.")
                    print(FetchData.END)
                    break
                else:
                    print(FetchData.RED+'Enter Valid Option!')
                    print(FetchData.END)
            except BaseException as e:
                print(FetchData.RED+"You must have to write Valid Option!")
                print(FetchData.END)
    
    @staticmethod
    def payment_history():
        file = open(
                    f"D:\\Customer_info\\Payment History\\{FetchData.history_file}.txt",
                    "r",
                )
        data=file.read()
        if(data!=''):
            print(FetchData.GREEN+'````````````````````Payment History````````````````````')
            print(FetchData.YELLOW+data)
            print(FetchData.END)
        else:
            print(FetchData.RED+"No any transaction  Found!")
        file.close()

    @staticmethod
    def sorting_dictionary(data_sorting, price_data, ans):
        sorting_by_price = price_data.copy()
        if ans == 1:
            # Sorting in ascending order
            sorting_by_price.sort()
        if ans == 2:
            # Sorting in descending order
            sorting_by_price.sort(reverse=True)
        count = 1
        sorted_dictionary = dict()
        # Sorting the dictionary by price
        while len(sorting_by_price) != 0:
            for i in data_sorting.values():
                # Checking if sorting_by_price is not empty before accessing its elements
                if sorting_by_price and sorting_by_price[0] == i[2]:
                    sorting_by_price.pop(0)
                    sorted_dictionary[count] = i
                    count += 1
        FetchData.display_menu_data(sorted_dictionary, price_data)


class CustomerData(FetchData):
    password = ""
    email = ""
    email_flag = 0
    mobile_flag = 0
    phone_no = ""

    def __init__(self):
        CustomerData.customer_data_gathering_menu()

    @staticmethod
    def customer_data_gathering_menu():
        flag = True
        while flag:
            customer_choice = input(
                "_________________________________________________\n"
                "| 1] Do you want to create an Account (Sign Up). |\n"
                "| 2] Do you want to Sign In.                     |\n"
                "|________________________________________________|\n"
                "Enter your choice: "
            )
            if customer_choice == "1":
                flag2 = True
                flag = False
                while flag2:
                    choice = input(
                        "_________________________________________________\n"
                        "| 1] Sign Up through Mobile No.                  |\n"
                        "| 2] Sign Up through Email Id.                   |\n"
                        "|________________________________________________|\n"
                        "Enter your choice: "
                    )
                    if choice == "1":
                        flag2 = False
                        CustomerData.sign_up(1)
                    elif choice == "2":
                        flag2 = False
                        CustomerData.sign_up(2)
                    else:
                        print("Enter  a valid option.")
            elif customer_choice == "2":
                flag2 = True
                flag = False
                while flag2:
                    choice = input(
                        "1] Sign in through Mobile No\n"
                        "2] Sign in through Email ID\n"
                        "----------------------------------------------\n"
                        "Enter Your Choice: "
                    )

                    if choice == "1":
                        flag2 = False
                        CustomerData.sign_in(1)
                    elif choice == "2":
                        flag2 = False
                        CustomerData.sign_in(2)
                    else:
                        print("Enter  a valid option.")
            else:
                print("Enter a valid option.")

    @staticmethod
    def sign_in(choice):
        file = open("D:\\Customer_info\\customer_info.txt", "r")
        if choice == 1:
            mobile_no = input("Enter Your Mobile Number : ")
            password = input("Enter Your Password : ")
            flag = 0
            for line in file:
                data = line.split()
                if mobile_no in data and password in data:  
                    FetchData.user_name = data[0]
                    CustomerData.phone_no = mobile_no
                    CustomerData.mobile_flag = 1
                    flag = True
            if flag == 1:
                print(FetchData.MAGNETA+f"welcome back {FetchData.user_name}")
            else:
                print("User not Found!")
                CustomerData.customer_data_gathering_menu()
        elif choice == 2:
            email_id = input("Enter Your Email : ")

            password = input("Enter Your Password : ")
            flag = 0
            for line in file:
                data = line.split()
                if email_id in data and password in data:
                    FetchData.user_name = data[0]
                    flag = 1
            if flag == 1:
                CustomerData.email = email_id
                CustomerData.email_flag = 1
                print(FetchData.MAGNETA+f"welcome back {FetchData.user_name}")
                print(FetchData.END)
            else:
                print("User not Found!")
                CustomerData.customer_data_gathering_menu()

    @staticmethod
    def has_no_digits(name):
        for char in name:
            if char.isdigit():
                return False
        return True

    @staticmethod
    def sign_up(choice):
        file = open("D:\\Customer_info\\customer_info.txt", "a")
        n_f = True
        while n_f:
            name = input("Enter Name : ")
            if CustomerData.has_no_digits(name):
                n_f = False
            else:
                print("Name should not contain digits!")
        p_f = True
        while p_f:
            CustomerData.password = input("enter Your Password:")
            if (len(CustomerData.password) >= 6) and (len(CustomerData.password) <= 8):
                p_f = False
        if choice == 1:
            CustomerData.get_mobile_no()
            file.write(
                f"{name} {CustomerData.mobile_no} {CustomerData.password} {datetime.datetime.now().date()}\n"
            )
            CustomerData.phone_no = CustomerData.mobile_no
            CustomerData.mobile_flag = 1
            print("Data added successfully")
        if choice == 2:
            CustomerData.get_gmail_address()
            file.write(
                f"{name} {CustomerData.email} {CustomerData.password} {datetime.datetime.now().date()}\n"
            )
            CustomerData.email_flag = 1
            print("Data added successfully")
        file.close()

    @staticmethod
    def get_mobile_no():
        count = 0
        is_valid_mn = False
        while not is_valid_mn:
            FetchData.mobile_no = input("Enter Mobile Number:")

            if len(FetchData.mobile_no) == 10:
                for m in range(len(FetchData.mobile_no)):
                    if m == 0:
                        if "7" <= FetchData.mobile_no[m] <= "9":
                            count += 1
                            continue
                        else:
                            print(
                                f"First digit should not be {FetchData.mobile_no[m]}\n"
                                f"It must be between [7-9].\n"
                                f"And rest between [0-9]."
                            )
                            count = 0
                            break
                    else:
                        if "0" <= FetchData.mobile_no[m] <= "9":
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

    @staticmethod
    def get_gmail_address():
        # Regular expression pattern for validating Gmail addresses
        pattern = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"

        while True:
            CustomerData.email = input("Enter your email: ")
            if re.match(pattern, CustomerData.email):
                print("Valid Gmail address.")
                break
            else:
                print("Invalid Gmail address. Please try again.")



class Payment(FetchData):
    total_amount = 0
    modification = False
    customer_cart = {}
    selected_data_cart = dict()

    @staticmethod
    def select_item(search_data):
        selected_item = []
        selected_item_quantity = []
        # global selected_data_cart
        print(
            FetchData.GREEN+"_________________________________________\n| Enter your item data like below        |\n| 1*2 4*3 means item1 2 times and        |\n| item4 3 times                          |\n|________________________________________|"
        )
        print(FetchData.END)
        item_data = input("Enter item data: ")
        list1 = item_data.split()
        for i in list1:
            list_1 = i.split("*")
            selected_item.append(int(list_1[0]))
            selected_item_quantity.append(int(list_1[1]))
            values = search_data.get(int(list_1[0]))
            Payment.selected_data_cart[values[1]] = int(list_1[1])
        Payment.payment_bill()

    @staticmethod
    def payment_bill():
        if Payment.modification:
            for key in list(
                Payment.selected_data_cart.keys()
            ):  # Using list() to avoid dictionary changed size during iteration error
                if Payment.selected_data_cart[key] == 0:
                    Payment.selected_data_cart.pop(key)
                    print(Payment.selected_data_cart)
                    Payment.modification = False
        id_to_search = (
            Payment.selected_data_cart.keys()
        )  # {'w1':2,'w24':3} particular key has this quantity
        print(id_to_search)
        selected_data = {}
        Payment.total_amount = 0
        file_path = "D:\\Online_Shopping_System_data\\"
        product_file_names = os.listdir("D:\\Online_Shopping_System_data")
        for file_name in product_file_names:
            with open(f"{file_path}{file_name}", "r") as file:
                for line in file:
                    line_list = line.split("#")
                    if any(id_ in line_list for id_ in id_to_search):
                        selected_data[line_list[1]] = line_list
        file.close()

        print(FetchData.GREEN+"--------Total Bill-----------------")
        print(FetchData.END)
        count = 1
        for id_ in id_to_search:
            values = selected_data.get(id_)
            if values is not None:
                price = float(values[2])
                quantity = Payment.selected_data_cart[id_]
                amount = price * quantity
                print(
                    f'[{count}] {values[0]} {" ".join(values[4:])}  {price}*{quantity}   {amount} rupees'
                )
                Payment.total_amount += amount
                count += 1
                
            else:
                print(FetchData.RED+f"No data found for ID: {id_}\n")
                print(FetchData.END)
        print(f"Total amount: {Payment.total_amount} rupees")
        rounded_number = round(Payment.total_amount, 3)
        str_amount = str(rounded_number)
        split_amount = str_amount.split(".")
        payable_amount_in_words = ""
        payable_amount_in_words=payable_amount_in_words+Payment.convert_to_words(int(split_amount[0]))+' point '+Payment.convert_to_words(int(split_amount[1]))
        print(f'Total payable amount in words:{payable_amount_in_words}')
        count = 0
        for i in split_amount:
            if count == 0:
                payable_amount_in_words += Payment.convert_to_words(int(i)) + " Point "
                count = 1
            else:
                if int(i) != 0:
                    payable_amount_in_words += Payment.convert_to_words(int(i))
        flag = True
        while flag:
            choice = input(
                FetchData.GREEN+"_________________________________________\n"
                "| 1] Process further for Payment          |\n"
                "| 2] Go back to Main Menu                 |\n"
                "| 3] Delete cart data                     |\n"
                "| 4] Modify the data                      |\n"
                "|________________________________________|\n"
                "Enter your choice: "
            )
            print(FetchData.END)
            if choice == "1":
                file = open(
                    f"D:\\Customer_info\\Payment History\\{FetchData.history_file}.txt",
                    "a",
                )
                file.write(
                    f"----------------{str(datetime.datetime.now().date())}----------------\n"
                )
                for id_ in id_to_search:
                    values = selected_data.get(id_)
                    if values is not None:
                        price = float(values[2])
                        quantity = Payment.selected_data_cart[id_]
                        amount = price * quantity
                        print(f'[{count}] {values[0]} {" ".join(values[4:])}  {price}*{quantity}   {amount} rupees\n')
                        file.write(
                            f'[{count}] {values[0]} {" ".join(values[4:])}  {price}*{quantity}   {amount} rupees\n'
                        )
                        Payment.total_amount += amount
                        count += 1
                    else:
                        print(f"No data found for ID: {id_}\n")
                file.write(f"Total Payable Amount:{str(Payment.total_amount)}\n")
                flag = False
                file.write(FetchData.MAGNETA+"Payment Done.")
                file.close()
                Payment.selected_data_cart.clear()
                print("Payment Done Successfully")
                print(FetchData.END)
            elif choice == "2":
                flag = False
                FetchData.process_data()
            elif choice == "3":
                flag = False
                Payment.selected_data_cart.clear()
                print(Payment.selected_data_cart)
            elif choice == "4":
                flag = False
                Payment.modification = True
                Payment.select_item(FetchData.search_data)
            else:
                print(FetchData.RED+"Enter Valid Option!")

    @staticmethod
    def number_value(num):
        # Dictionaries for numbers and their representations
        num_dict = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            10: "Ten",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }
        num_list = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            10,
            20,
            30,
            40,
            50,
            60,
            70,
            80,
            90,
        ]
        if num in num_dict:
            return num_dict.get(num)
        else:
            counter = 0
            while counter < len(num_list):
                if num >= num_list[counter]:
                    counter += 1
                else:
                    break
            return (
                num_dict.get(num_list[counter - 1])
                + " "
                + Payment.number_value(num - num_list[counter - 1])
            )

    # Function to convert a number into words
    @staticmethod
    def convert_to_words(number):
        n = number
        units_counter = 0
        num_str = ""

        unit_dict = {
            100000000000: "Kharab",
            1000000000: "Arab",
            10000000: "Crore",
            100000: "Lakh",
            1000: "Thousand",
            100: "Hundred",
            1: "",
        }
        # Lists to track magnitudes and their order
        units_list = [100000000000, 1000000000, 10000000, 100000, 1000, 100, 1]
        while n != 0:
            if n // units_list[units_counter]:
                num1 = n // units_list[units_counter]
                num_str = (
                    num_str
                    + " "
                    + Payment.number_value(num1)
                    + " "
                    + unit_dict.get(units_list[units_counter])
                )
                n = n % units_list[units_counter]
            units_counter += 1

        return f"{num_str.strip()}"

    # Example usage
    # Call this function after you have populated the selected_data_cart dictionary
    # payment_bill()



class Menu:
    def __init__(self):
        c = CustomerData()
        if CustomerData.email_flag:
            data = CustomerData.email.split("@")
            history_file = data[0]
        elif CustomerData.mobile_flag:
            history_file = CustomerData.phone_no
        FetchData.file_name(history_file)
        FetchData.process_data()


m = Menu()
