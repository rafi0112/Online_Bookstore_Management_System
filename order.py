orders = []

def place_order(id,book_title,quantity):
    order = {"id":id, "book_title":book_title, "quantity":quantity}
    orders.append(order)
def list_orders():
    return orders