from Product import Product


def shop():
    print("Products avialable in stock")
    dct = {1: "Samsung A30", 2: "iPhone 11Pro", 3: "Nokia 3310"}
    lst = [1, 2, 3]

    for k in lst:

        print(dct[k])


product_prompts = [
    "Samsung A30\nDescription: 2gbRAM, 13MP\nPrice: $200\n(a) Buy\n(b) Next Product\n\n",
    "iPhone 11Pro\nDescription: 4gbRAM, 43MP\nPrice: $300\n(a) Buy\n(b) Next Product\n\n",
    "Nokia 3310\nDescription: 1gbRAM, 5MP\nPrice: $100\n(a) Buy\n(b) Next Product\n\n"
]

products = [
    Product(product_prompts[0], "a", 200),
    Product(product_prompts[1], "a", 300),
    Product(product_prompts[2], "a", 100)
]

cart = 0
price = 0


def view_products(products):
    print("\nWelcome!!! You are now logged in\n")

    shop()

    proChoice = input("\nEnter name of the product to BUY, type 'END' to check out product in cart type 'EXIT' to logout: ").lower()

    def logOut():
  
        continue_shopping = input("Type 'CONT' to continue shopping, type 'END' to check out product in cart, type 'EXIT' to logout: ").lower()

        if continue_shopping == "cont":
            view_products(products)
        elif continue_shopping == "end":
            print("You got " + str(cart) + " Product in chart")
            print("The total price of the product is " + str(price))

            ossai = input("Type 'CONT' to continue shopping,\
             type 'EXIT' to logout: ").lower()
            if ossai == "cont":
                view_products(products)
            else:
                print("Thanks for Shopping with us. See you later!!")
        else:
            print("Thanks for Shopping with us. See you later!!")

    for item in products:
        if proChoice == "samsung a30":
            print("\n")
            print(products[0].prompt)
            answer = input("Insert Option: ")
            if answer.lower() == products[0].answer:
                global price
                price += products[0].price
                global cart
                cart += 1
            logOut()
        elif proChoice == "iphone 11pro":
            print("\n")
            print(products[1].prompt)
            answer = input("Insert Option: ")
            if answer.lower() == products[1].answer:
                price += products[1].price
                cart += 1
            logOut()
        elif proChoice == "nokia 3310":
            print("\n")
            print(products[2].prompt)
            answer = input("Insert Option: ")
            if answer.lower() == products[2].answer:
                price += products[2].price
                cart += 1
            logOut()
        elif proChoice == "end":
            print("You got " + str(cart) + " Product in chart")
            print("The total price of the product is " + str(price))
            logOut()
        elif proChoice == "exit":
            print("Thanks for Shopping with us. See you later!!")
        else:
            print("Sorry! Product not in stock")
            logOut()

        break


def logged():
    print("Type 1 to Create an Account. Type 2 to login")
    global choice
    choice = input("Enter choice here: ")

    if choice == ("1"):
        print("Welcome to the Create an Account interface")
        username = input("Username: ")
        password = input("Password: ")
        details = username.lower() + " " + password + "\n"

        acc_file = open("account.txt", "r")
        file_lines = acc_file.readlines()

        if details in file_lines:
            print("You already have an account type 2 to login")
            print("\n")
            logged()
        else:
            acc_file = open("account.txt", "a")
            acc_file.write(details)
            acc_file.close()
            view_products(products)

        acc_file.close()

    elif choice == ("2"):
        print("Welcome, input your Username and Password to login")
        username = input("Username: ")
        password = input("password: ")
        details = username.lower() + " " + password + "\n"

        acc_file = open("account.txt", "r")
        file_lines = acc_file.readlines()

        if details in file_lines:
            view_products(products)
        else:
            print("Incorrect Username or Password")
            print("\n")
            logged()

        acc_file.close()


logged()