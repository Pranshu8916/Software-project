from enum import Enum

class Status(Enum):
    SUBMITTED = "Submitted"
    ASSIGNED = "Assigned"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"


class Ticket:
    def __init__(self, ticket_id, location, category, description):
        self.id = ticket_id
        self.location = location
        self.category = category
        self.description = description
        self.status = Status.SUBMITTED
        self.assigned_to = None
        self.resolution_note = None

    def assign(self, department):
        self.assigned_to = department
        self.status = Status.ASSIGNED

    def start_work(self):
        if self.status == Status.ASSIGNED:
            self.status = Status.IN_PROGRESS

    def resolve(self, note):
        if self.status == Status.IN_PROGRESS:
            self.status = Status.RESOLVED
            self.resolution_note = note

    def display(self):
        print("\n--- Ticket ---")
        print(f"ID: {self.id}")
        print(f"Location: {self.location}")
        print(f"Category: {self.category}")
        print(f"Description: {self.description}")
        print(f"Assigned To: {self.assigned_to}")
        print(f"Status: {self.status.value}")
        if self.resolution_note:
            print(f"Resolution: {self.resolution_note}")