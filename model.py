from dataclasses import dataclass
from datetime import date
from typing import Optional, List


class OutOfStock(Exception):
    pass


>>>>>> > chapter_01


class OutOfStock(Exception):
    pass


def allocate(line: OrderLine, batches: List[Batch]) -> str:
    try:
        batch = next(
            b for b in sorted(batches) if b.can_allocate(line)
        )
        return batch.reference
    except StopIteration:
        raise OutOfStock(f'Out of stock for sky {line.sku}')


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

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    def __hash__(self):
        return hash(self.reference)

    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta


def allocate(line: OrderLine, batches: List[Batch]) -> str:
    try:
        batch = next(b for b in sorted(batches) if b.can_allocate(line))
        batch.allocate(line)
    except StopIteration:
        raise OutOfStock(f'Out Of Stock: {line.sku}')
    return batch.reference
