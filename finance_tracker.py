import json
import matplotlib.pyplot as plt

class FinanceTracker:
    def __init__(self):
        self.expenses = []
        self.load_data()

    def load_data(self):
        """Load existing data from a JSON file (if available)"""
        try:
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []

    def save_data(self):
        """Save expenses to a JSON file"""
        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, category, amount):
        """Add a new expense"""
        self.expenses.append({"category": category, "amount": amount})
        self.save_data()
        print(f"✅ Added: {category} - ${amount}")

    def view_expenses(self):
        """View all recorded expenses"""
        if not self.expenses:
            print("❌ No expenses recorded.")
            return
        
        print("\n=== Expense List ===")
        for i, exp in enumerate(self.expenses, 1):
            print(f"{i}. {exp['category']} - ${exp['amount']}")

    def plot_expenses(self):
        """Generate a pie chart of expenses"""
        if not self.expenses:
            print("❌ No expenses to display.")
            return

        categories = {}
        for expense in self.expenses:
            categories[expense["category"]] = categories.get(expense["category"], 0) + expense["amount"]

        labels = categories.keys()
        amounts = categories.values()

        plt.figure(figsize=(6, 6))
        plt.pie(amounts, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title("Expense Distribution")
        plt.show()

# Main Menu
def main():
    tracker = FinanceTracker()

    while True:
        print("\n===== Personal Finance Tracker =====")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Show Expense Chart")
        print("4️⃣ Exit")
        choice = input("Select an option (1-4): ")

        if choice == "1":
            category = input("Enter category (Food, Rent, Bills, etc.): ")
            try:
                amount = float(input("Enter amount: $"))
                tracker.add_expense(category, amount)
            except ValueError:
                print("❌ Invalid amount! Please enter a number.")
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.plot_expenses()
        elif choice == "4":
            print("✅ Exiting... Have a great day!")
            break
        else:
            print("❌ Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
