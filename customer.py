customers = []

def add_customer(name,email,phone):
    customer = {"name":name, "email":email, "phone":phone}
    customers.append(customer)
def list_customers():
    return customers