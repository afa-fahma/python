class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def apply_bonus(self, percentage):
        self.salary += self.salary * percentage / 100

    def display_info(self):
        print(f"Name: {self.name} | Position: {self.position} | Salary: {self.salary}")


e1 = Employee(input("Enter name: "),
              input("Enter position: "),
              float(input("Enter salary: ")))
e1.apply_bonus(float(input("Enter bonus %: ")))

e2 = Employee(input("Enter name: "),
              input("Enter position: "),
              float(input("Enter salary: ")))
e2.apply_bonus(float(input("Enter bonus %: ")))

e1.display_info()
e2.display_info()



# class Order:
#     def __init__(self, order_id, product_name, status):
#         self.order_id = order_id
#         self.product_name = product_name
#         self.status = status
# orders = []
# for i in range(2):
#     order_id = int(input("Enter order ID: "))
#     product_name = input("Enter product name: ")
#     status = input("Enter status: ")
#     orders.append(Order(order_id, product_name, status))
# print("\nUpdated Orders:")
# for order in orders:
#     print(f"{order.order_id} - {order.product_name} - {order.status}")

