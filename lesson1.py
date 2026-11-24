name = input("Enter customer name: ")
email = input("Enter customer email: ")
budget = float(input("Enter customer budget: "))

customer = {
    "name": name,
    "email": email,
    "budget": budget
}

print("\nCustomer Information:")
print(customer)