class Bug:
    def _init_(self, title, description, assigned_to=None, priority="Low", status="Open"):
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.priority = priority
        self.status = status

class BugTracker:
    def _init_(self):
        self.bugs = []

    def log_bug(self, title, description):
        bug = Bug(title, description)
        self.bugs.append(bug)
        print("Bug logged successfully!")

    def assign_bug(self, bug_idx, assignee):
        if 0 <= bug_idx < len(self.bugs):
            self.bugs[bug_idx].assigned_to = assignee
            print("Bug assigned successfully!")
        else:
            print("Invalid bug index.")

    def prioritize_bug(self, bug_idx, priority):
        if 0 <= bug_idx < len(self.bugs):
            self.bugs[bug_idx].priority = priority
            print("Bug prioritized successfully!")
        else:
            print("Invalid bug index.")

    def change_status(self, bug_idx, status):
        if 0 <= bug_idx < len(self.bugs):
            self.bugs[bug_idx].status = status
            print("Bug status changed successfully!")
        else:
            print("Invalid bug index.")

    def list_bugs(self):
        for idx, bug in enumerate(self.bugs):
            print(f"Bug {idx}:")
            print(f"Title: {bug.title}")
            print(f"Description: {bug.description}")
            print(f"Assigned To: {bug.assigned_to}")
            print(f"Priority: {bug.priority}")
            print(f"Status: {bug.status}")
            print()

def main():
    tracker = BugTracker()

    while True:
        print("Bug Tracker Menu:")
        print("1. Log Bug")
        print("2. Assign Bug")
        print("3. Prioritize Bug")
        print("4. Change Bug Status")
        print("5. List Bugs")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter bug title: ")
            description = input("Enter bug description: ")
            tracker.log_bug(title, description)
        elif choice == "2":
            bug_idx = int(input("Enter bug index: "))
            assignee = input("Enter assignee: ")
            tracker.assign_bug(bug_idx, assignee)
        elif choice == "3":
            bug_idx = int(input("Enter bug index: "))
            priority = input("Enter priority: ")
            tracker.prioritize_bug(bug_idx, priority)
        elif choice == "4":
            bug_idx = int(input("Enter bug index: "))
            status = input("Enter status: ")
            tracker.change_status(bug_idx, status)
        elif choice == "5":
            tracker.list_bugs()
        elif choice == "6":
            print("Exiting Bug Tracker.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()