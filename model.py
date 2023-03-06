import dataclasses
import datetime


class Batch:
    def __init__(self, reference: str, sku: str, purchased_quantity: int, eta: datetime.date | None):
        self.reference = reference
        self.sku = sku
        self.purchased_quantity = purchased_quantity
        self.eta = eta
        self.allocated_order_lines: set["OrderLine"] = set()

    def allocate(self, order_line: "OrderLine"):
        if self.can_allocate(order_line):
            self.allocated_order_lines.add(order_line)

    def deallocate(self, order_line: "OrderLine"):
        if order_line in self.allocated_order_lines:
            self.allocated_order_lines.remove(order_line)

    def can_allocate(self, order_line: "OrderLine"):
        return self.sku == order_line.sku and self.available_quantity >= order_line.quantity

    @property
    def allocated_quantity(self):
        return sum(allocated_order_line.quantity for allocated_order_line in self.allocated_order_lines)

    @property
    def available_quantity(self):
        return self.purchased_quantity - self.allocated_quantity


@dataclasses.dataclass(frozen=True)
class OrderLine:
    order_reference: str
    sku: str
    quantity: int
