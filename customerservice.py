service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def add_ticket(tickets, ticket, customer):
    tickets.update({ticket:customer})
    print(f"ticket {ticket} for {customer} has been registered")

def update_status():
    pass

def display_tickets():
    pass


while True:
    choice = int(input("What would you like to do? \n1.Open a new service ticket. \n2.Update the status of an existing ticket. \n3.Display all tickets or filter by status. Please select a number 1-3: "))
    if choice == 1:
        ticket = input("What is the ticket number?: ")
        customer = input("What is the customer's name?")
        add_ticket(service_tickets, ticket, customer)
    else:
        print("didnt work")
    if choice == 2:
        update_status()
        pass
    else:
        pass
    if choice == 3:
        display_tickets()
        pass
    else:
        pass