from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class OrderLine:
    id: str
    sku: str
    quantity: int


class Batch:
    def __init__(
        self,
        reference: str,
        sku: str,
        quantity: int,
        eta: Optional[date] = None
    ):
        self.reference = reference
        self.sku = sku
        self.eta = eta
        self.available = quantity

    def allocate(self, line: OrderLine):
        self.available -= line.quantity
