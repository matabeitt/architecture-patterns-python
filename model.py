from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(unsafe_hash=True)
class OrderLine:
    order_id: str
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
        self.stock = quantity
        self._allocations = set()

    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available >= line.quantity

    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated(self) -> int:
        return sum(o.quantity for o in self._allocations)

    @property
    def available(self) -> int:
        return self.stock - self.allocated
