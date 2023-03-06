import dataclasses
import datetime


class Batch:
    def __init__(self, reference: str, SKU: str, available_quantity: int, ETA: datetime.date | None):
        self.reference = reference
        self.SKU = SKU
        self.available_quantity = available_quantity
        self.ETA = ETA

    def allocate(self, order_line: "OrderLine"):
        self.available_quantity -= order_line.quantity


@dataclasses.dataclass(frozen=True)
class OrderLine:
    order_reference: str
    SKU: str
    quantity: int
