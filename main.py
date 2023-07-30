file= open('file.txt')
L=list(file)
file.close()

def display_statistics():
    pass

def book_Ticket():
    pass

def display_ticket():
    pass

def change_priority():
    pass

def disable_ticket():
    pass

def run_events():
    pass

def admin_menu():
        
            print("choose one of the below options Admin:\n")
            print("1.Display Statistics\n"+
                "2.Book a Ticket\n"+
                "3.Display all Tickets\n"+
                "4.Change Tickets Priority\n"+
                "5.Disable Ticket\n"
                "6.Run Events\n"+
                "7.Exit")
            choice = eval(input("Enter your choice (1-7):"))
            while choice!=7:
                if choice == "1":
                    print("You selected: Display Statistics")
                    display_statistics()
                elif choice == "2":
                    print("You selected: Book a Ticket")
                    book_Ticket()
                elif choice == "3":
                    print("You selected: Display all Tickets")
                    display_ticket()
                elif choice == "4":
                    print("You selected: Change Tickets Priority")
                    change_priority()
                elif choice == "5":
                    print("you selected: Disable Ticket")
                    disable_ticket()
                elif choice == "6":
                    print("You selected: Run Events")
                    run_events()
            print("you are exiting the admin menu:\n")

def book_ticket():
    pass

def user_menu():
    
    print("1.Book a ticket\n"+
        "2.Exit")
    choice = eval(input("Enter your choice (1 or 2):"))
    while choice!=2:
        if choice =="1":
            print("you want to book a ticket:\n")
            book_ticket()
    print("you are exiting the user menu:\n")


def greet_start():
    max=5
    while max>0:
        username=str(input("enter your username:"))
        password=input("enter your password:")

        if username=="admin" and password=="admin123123":
            admin_menu()
            break
        elif password=="":
            user_menu()
            break
        else:
            max=max-1
            print("Incorrect Username and/or password")
    if max==0:
        print("you tried more than 5 times so exiting")
greet_start()
