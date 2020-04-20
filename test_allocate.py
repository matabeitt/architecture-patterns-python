from datetime import date, timedelta
import pytest
from model import Batch, OrderLine, allocate


def test_prefers_current_stock_batches_to_shipments():
    batch_stock = Batch('batch-STK-001', 'sku-clock', 10, eta=None)
    batch_ships = Batch('batch-SHP-001', 'sku-clock', 10,
                        eta=date.today() + timedelta(days=1))
    allocate_line = OrderLine('order-0001', 'sku-clock', 1)
    allocate(allocate_line, [batch_ships, batch_stock])

    assert batch_stock.available == 9
    assert batch_ships.available == 10


def test_returns_allocated_batch_ref():
    batch_stock = Batch('batch-STK-001', 'sku-clock', 10, eta=None)
    batch_ships = Batch('batch-SHP-001', 'sku-clock', 10,
                        eta=date.today() + timedelta(days=1))
    allocate_line = OrderLine('order-0001', 'sku-clock', 1)
    allocation = allocate(allocate_line, [batch_ships, batch_stock])

    assert batch_stock.reference == allocation
