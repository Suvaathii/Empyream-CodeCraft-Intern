class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.search_history = []

    def search_product(self, product_name):
        self.search_history.append(product_name)

    def get_recommendations(self, product_database):
        # Simple recommendation: suggest products related to the user's search history
        suggestions = []
        for product_name in self.search_history:
            for product in product_database:
                if product_name.lower() in product.name.lower() and product not in suggestions:
                    suggestions.append(product)
        return suggestions

class Product:
    def __init__(self, product_id, name, category, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price

def main():
    product_database = [
        Product("P001", "Laptop", "Electronics", 1000),
        Product("P002", "Smartphone", "Electronics", 800),
        Product("P003", "Headphones", "Electronics", 100),
        Product("P004", "Running Shoes", "Clothing", 80),
        Product("P005", "Backpack", "Fashion", 40),
        Product("P006", "Tablet", "Electronics", 500),
        # ... add more products
    ]

    users = {}
    while True:
        print("\n1. Register User")
        print("2. Search for a Product")
        print("3. Get Recommendations")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter User ID: ")
            name = input("Enter your name: ")
            users[user_id] = User(user_id, name)
            print(f"User {name} registered successfully!")

        elif choice == "2":
            user_id = input("Enter User ID: ")
            if user_id in users:
                user = users[user_id]
                product_name = input("Enter the product name you are looking for: ")
                user.search_product(product_name)
                print(f"Searching for {product_name}...")
            else:
                print("User not found!")

        elif choice == "3":
            user_id = input("Enter User ID: ")
            if user_id in users:
                user = users[user_id]
                recommendations = user.get_recommendations(product_database)
                print("Recommended Products:")
                for product in recommendations:
                    print(f"{product.name} - ${product.price} ({product.category})")
            else:
                print("User not found!")

        elif choice == "4":
            print("Exiting the system.")
            break

if __name__ == "__main__":
    main()