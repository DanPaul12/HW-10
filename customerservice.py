service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def add_ticket(tickets, ticket):
    tickets[ticket] = {}
    print(f"{ticket} has been registered")

def update_status(tickets, ticket, new_status):
    tickets[ticket]["Status"] = new_status
    print(f"{ticket} is now {new_status}")

def display_tickets(tickets):
    for ticket in tickets.items():
        print(f"{ticket}")

def display_open_tickets(tickets):
    for ticket, statuses in tickets.items():
        for status in statuses:
            if status == "open":
                print(f"{ticket}")

# this last function doesn't work, please let me know
# what I should have done to filter by status
        


while True:
    choice = int(input("What would you like to do? \n1.Open a new service ticket. \n2.Update the status of an existing ticket. \n3.Display all tickets or filter by status. \nPlease select a number 1-3: "))
    if choice == 1:
        ticket = input("What is the ticket number? (Ticket001, Ticket002, etc): ")
        add_ticket(service_tickets, ticket)
    elif choice == 2:
        ticketnum = input("What is the ticket number? (Ticket001, Ticket002, etc): ")
        new_status = input("Do you want this ticket open or closed?")
        update_status(service_tickets, ticketnum, new_status)
    elif choice == 3:
        choice = int(input("Would you like to 1. Display all tickets or 2. Display only open tickets? Enter 1 or 2: "))
        if choice == 1:
            display_tickets(service_tickets)
        elif choice == 2:
            display_open_tickets(service_tickets)
    else:
        print("Please choose a number between 1-3.")