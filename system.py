from ticket import Ticket

class IncidentSystem:
    def __init__(self):
        self.tickets = []
        self.counter = 1

    def create_ticket(self, location, category, description):
        ticket = Ticket(self.counter, location, category, description)
        self.tickets.append(ticket)
        self.counter += 1
        print(f"Ticket created successfully! ID: {ticket.id}")

    def assign_ticket(self, ticket_id, department):
        for t in self.tickets:
            if t.id == ticket_id:
                t.assign(department)
                print("Ticket assigned!")
                return
        print("Ticket not found!")

    def start_work(self, ticket_id):
        for t in self.tickets:
            if t.id == ticket_id:
                t.start_work()
                print("Work started!")
                return
        print("Ticket not found!")

    def resolve_ticket(self, ticket_id, note):
        for t in self.tickets:
            if t.id == ticket_id:
                t.resolve(note)
                print("Ticket resolved!")
                return
        print("Ticket not found!")

    def view_tickets(self):
        if not self.tickets:
            print("No tickets available.")
        for t in self.tickets:
            t.display()