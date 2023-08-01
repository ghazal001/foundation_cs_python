#this fct will sort the list by the date or by the id 
#worst case=>O(N^2)
def date_id_sorted(L):
    for x in range(len(L)): #N
        check_swap=False
        for y in range(len(L)-x-1):#N
            if L[y].split(",")[3]>L[y+1].split(",")[3] or (L[y].split(",")[3]==L[y+1].split(",")[3] and L[y].split(",")[1]>L[y+1].split(",")[1]):
                check_swap=True
                temp=L[y]
                L[y]=L[y+1]
                L[y+1]=temp
        if not check_swap:
            break
    return L
#will sort the list L by the priority of each elemnt 
#worst case=>O(N^2)
def priority_sorted(L):
    for x in range(len(L)):#N
        check_swap=False
        for y in range(len(L)-x-1):#N
            if L[y].split(",")[4]>L[y+1].split(",")[4]:
                check_swap=True
                temp=L[y]
                L[y]=L[y+1]
                L[y+1]=temp
        if not check_swap:
            break
    return L



#it will count the tickets number for each element and 
# get the event having the maximum number of tickets 
#worst case=>O(N)
def display_statistics(L):
    #dictionary to store the nb of tickets for each events
    tickets_events={}
    for x in L:#N
        parts=x.split(",")
        event = parts[1]
        if event in tickets_events:
            tickets_events[event]+=1
        else:
            tickets_events[event]=1
    max_tickets=max(tickets_events,key=tickets_events.get)
    print("the Evenet with the highest number of tickets is:",max_tickets)
    print("its number of tickets is :",tickets_events[max_tickets])



#will return the ticket id like tick01 this will return 01
#worst case=>O(n) where n is the length of the ticket
def get_ticket_id(ticket):
    return ticket.split(",")[0][4:]


#will book a ticket for the admin by first thing will get the highest id 
#and will atomatically increment it and append the new ticket to the list
# worst case=> O(N) Nis the number of element in L
def book_ticket(L):
    username = input("Enter your username: ")#1
    event_id = int(input("Enter the event ID: "))#1
    event_date = input("Enter the event date (yyyymmdd): ")#1
    priority = int(input("Enter the priority: "))#1
    #highest id 
    highest_ticket_id = max([get_ticket_id(ticket) for ticket in L], default=0)    
    ticket_id=int(highest_ticket_id) + 1
    new_ticket=f"tick{ticket_id},ev{str(event_id)},{username},{event_date},{priority}"
    L.append(new_ticket)
    print("ticket booked successfully:")
    for ticket in L:#N
        print(ticket)

#will only display the new registred  ticket date>=2023
#worst case=>O(N^2)
def display_ticket(L):
    date_id_sorted(L)#N^2
    print("the tickets registred in the system are:")
    for ticket in L:
        parts=ticket.split(",")
        ticket_date=parts[3]
        ticket_year=ticket_date[0:4]
        if int(ticket_year)>=2023:
            print(ticket)

#will search if the ticket is found by providing its ticket id 
#and it will return its index
#worst case=>O(N) Nis the number of element of L
def find_ticket_index(L,ticket_id):
    for i,ticket in enumerate(L):
        parts=ticket.split(",")
        current_ticket_id=int(parts[0][4:])
        if current_ticket_id==ticket_id:
            return i
    return None

#will change the priority of the found ticket and added back to the list
#worst case=>O(N)
def change_priority(L,ticket_id,new_priority):
    ticket_index=find_ticket_index(L,ticket_id)
    
    if ticket_index is not None:
            ticket=L[ticket_index]
            parts = ticket.split(",")
            # Update the priority of the ticket
            parts[-1] = str(new_priority)
            ticket = ",".join(parts)
            L[ticket_index]=ticket
            print("priority changed successfully")
            print(ticket)
    else:
        print(f"Ticket with ID {ticket_id} not found.")

#will delete the found ticket from the list
#worst case=>O(N)
def disable_ticket(L,ticket_id):
    ticket_index=find_ticket_index(L,ticket_id)#N
    if ticket_index is not None:
        del L[ticket_index]
        print("the ticket is removed successfully:  \n")
        print("the new list without the removed ticket is :",L)
    else:
        print(f"Ticket with ID {ticket_id} not found.")

#will display the events at today's date 
#worst case=>nlogn
def display_today_events(L,date):
    today_events=[event for event in L if event.split(",")[3] == date]
    if not today_events:
        print("there's no event for this date")
        return
    priority_sorted(today_events)
    print("the events are sorted by priority:")
    for event in today_events:
        print(event)
#will delete the today's event from the list after we display it 
#worst case=>nlogn
def run_events(L):
    choosen_date="20230803"
    display_today_events(L,choosen_date)
    priority_sorted(L)
    #remove these events from the list
    L=[event for event in L if event.split(",")[3] !=choosen_date]
    print("the list after we remove the today's events:")
    for event in L:
        print(event)
    return L

#this is the menu for the admin that contain the options that he can choose from 
def admin_menu(L):
        while True:
            print("choose one of the below options Admin:\n")
            print("1.Display Statistics\n"+
                "2.Book a Ticket\n"+
                "3.Display all Tickets\n"+
                "4.Change Tickets Priority\n"+
                "5.Disable Ticket\n"
                "6.Run Events\n"+
                "7.Exit")
            choice = int(input("Enter your choice (1-7):"))
            if choice == 1:
                print("You selected: Display Statistics")
                display_statistics(L)
            elif choice == 2:
                print("You selected: Book a Ticket")
                book_ticket(L)
            elif choice == 3:
                print("You selected: Display all Tickets")
                display_ticket(L)
            elif choice == 4:
                print("You selected: Change Tickets Priority")
                ticket_id=int(input("Enter the ticket ID to change priority:"))
                new_priority=int(input("enter the new priority:"))
                change_priority(L,ticket_id,new_priority)
            elif choice == 5:
                print("you selected: Disable Ticket")
                ticket_id=int(input("Enter the ticket ID to remove it from the list:"))
                disable_ticket(L,ticket_id)
            elif choice == 6:
                print("You selected: Run Events")
                run_events(L)
            elif choice == 7:
                print("you are exiting the admin menu:\n")
                break
            else:
                print("your choice is invalid.try again")
                continue
            
#will let the user to book a new ticket and added to the list and save it 
#to the file
#worst case=>O(N) N is the number of element inside the list
def book_user_ticket(L,username):
    event_id = int(input("Enter the event ID: "))
    event_date = input("Enter the event date (yyyymmdd): ")
    priority ="0"
    highest_ticket_id = max([get_ticket_id(ticket) for ticket in L], default=0)    
    ticket_id=int(highest_ticket_id) + 1
    new_ticket=f"tick{ticket_id},ev{str(event_id)},{username},{event_date},{priority}"
    L.append(new_ticket)
    print("ticket booked successfully:")
    for ticket in L:
        print(ticket)
#this is the menu for the user that he can choose from
def user_menu(username):
    while True:
        print("1.Book a ticket\n"+
            "2.Exit")
        choice = int(input("Enter your choice (1 or 2):"))
        if choice == 1:
            print("you want to book a ticket:\n")
            book_user_ticket(L,username)
        elif choice == 2:
            print("you are exiting the user menu:\n")
            break
        else:
            print("Invalid choice,please try again (1 or 2)")
#log in form 
def greet_start():
    counter=5
    while counter>0:
        username=str(input("enter your username:"))
        password=input("enter your password:")

        if username == "admin" and password == "admin123123":
            admin_menu(L)
            break
        elif password=="":
            user_menu(username)
            break
        else:
            counter=counter-1
            print("Incorrect Username and/or password!!")
    if counter==0:
        print("you tried more than 5 times so exiting!!")
#open the file we want to impor from it the elemeent and while using the with it's automatically close it 
with open('file.txt','r') as file:
    L=list(file)


greet_start()
#adding the added events to the file
with open('file.txt', 'w') as file:
    file.writelines(L)