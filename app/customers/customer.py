class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def display_details(self):
        print("Name: ",self.name)
        print("Customer ID: ",self.customer_id)

cust = Customer("Yashraj","CUST1001")

cust.display_details()