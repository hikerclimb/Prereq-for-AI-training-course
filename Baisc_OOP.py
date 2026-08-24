class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        print(self.name, self.email)

customer = Customer("John", "john@example.com")
customer.display()
