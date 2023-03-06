class Batch:
    def __init__(self, reference: str, SKU: str, available_quantity: int):
        self.reference = reference
        self.SKU = SKU
        self.available_quantity = available_quantity

    def allocate(self, order_line: "OrderLine"):
        self.available_quantity -= order_line.quantity


class OrderLine:
    def __init__(self, order_reference: str, SKU: str, quantity: int):
        self.order_reference = order_reference
        self.SKU = SKU
        self.quantity = quantity
