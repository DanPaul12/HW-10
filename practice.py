service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def add_ticket(tickets, ticket):
    tickets[ticket] = {}
    print(f"{ticket} has been registered")

def update_status(tickets, ticket):
    tickets[ticket]["Status"] = "closed"
    print(f"{ticket} is now closed")

def display_tickets(tickets):
    for ticket in tickets.items():
        print(f"{ticket}")
        


while True:
    choice = int(input("What would you like to do? \n1.Open a new service ticket. \n2.Update the status of an existing ticket. \n3.Display all tickets or filter by status. \nPlease select a number 1-3: "))
    if choice == 1:
        ticket = input("What is the ticket number?: ")
        add_ticket(service_tickets, ticket)
    elif choice == 2:
        ticketnum = input("What is the ticket number?")
        update_status(service_tickets, ticketnum)
    elif choice == 3:
        display_tickets(service_tickets)
    else:
        print("Please choose a number between 1-3.")