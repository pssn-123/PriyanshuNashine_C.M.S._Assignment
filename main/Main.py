class Main_module():



    def login(self):
        print('Courier Management System Login')
        print("1. Customerr Login")
        print("2. Admin Login")

    def user_menu(self):
        print("Courier Management System Customer Login")
        print("Menu")
        print("1 Place a new Courier Order : ")
        print("2 Get Order Status : ")
        print("3 Cancel a Courier Order : ")
        print("4 Get Assigned Order : ")


    def admin_menu(self):
        print("Courier Management System Admin Login")


    def main(self):
        while True:
            Main_module.login()
            choice = input('Enter the User type')
            if choice == '1':
                Main_module.user_menu()
                option = input("Enter the Operation number : ")
                if option == '1':



if __name__ = "__main__":
    Main_module.main()