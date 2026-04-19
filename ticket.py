# Import Enum for status
from enum import Enum


# Enum to define ticket status
class Status(Enum):
    SUBMITTED = "Submitted"
    ASSIGNED = "Assigned"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"


class Ticket:
    def __init__(self, ticket_id, location, category, description):
        # Initialize ticket properties
        self.id = ticket_id
        self.location = location
        self.category = category
        self.description = description

        # Default status is Submitted
        self.status = Status.SUBMITTED

        # No department assigned initially
        self.assigned_to = None

        # No resolution at start
        self.resolution_note = None

    # Assign ticket to department
    def assign(self, department):
        self.assigned_to = department
        self.status = Status.ASSIGNED

    # Start working on ticket
    def start_work(self):
        if self.status == Status.ASSIGNED:
            self.status = Status.IN_PROGRESS

    # Resolve ticket
    def resolve(self, note):
        if self.status == Status.IN_PROGRESS:
            self.status = Status.RESOLVED
            self.resolution_note = note

    # Display ticket details
    def display(self):
        print("\n--- Ticket ---")
        print(f"ID: {self.id}")
        print(f"Location: {self.location}")
        print(f"Category: {self.category}")
        print(f"Description: {self.description}")
        print(f"Assigned To: {self.assigned_to}")
        print(f"Status: {self.status.value}")

        # Show resolution if exists
        if self.resolution_note:
            print(f"Resolution: {self.resolution_note}")
