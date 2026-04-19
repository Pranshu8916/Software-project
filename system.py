# Import Ticket class
from ticket import Ticket


class IncidentSystem:
    def __init__(self):
        # List to store all tickets
        self.tickets = []

        # Counter to assign unique ID
        self.counter = 1

    # Function to create new ticket
    def create_ticket(self, location, category, description):
        # Create ticket object
        ticket = Ticket(self.counter, location, category, description)

        # Add ticket to list
        self.tickets.append(ticket)

        print(f"Ticket created successfully! ID: {ticket.id}")

        # Increase counter
        self.counter += 1

    # Function to assign ticket
    def assign_ticket(self, ticket_id, department):
        for t in self.tickets:
            if t.id == ticket_id:
                t.assign(department)
                print("Ticket assigned successfully!")
                return

        print("Ticket not found!")

    # Function to start work
    def start_work(self, ticket_id):
        for t in self.tickets:
            if t.id == ticket_id:
                t.start_work()
                print("Work started!")
                return

        print("Ticket not found!")

    # Function to resolve ticket
    def resolve_ticket(self, ticket_id, note):
        for t in self.tickets:
            if t.id == ticket_id:
                t.resolve(note)
                print("Ticket resolved!")
                return

        print("Ticket not found!")

    # Function to display all tickets
    def view_tickets(self):
        if not self.tickets:
            print("No tickets available.")

        for t in self.tickets:
            t.display()
