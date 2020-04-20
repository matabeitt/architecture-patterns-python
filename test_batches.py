from datetime import date
from model import OrderLine, Batch


def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch('batch-001', sku, batch_qty, eta=date.today()),
        OrderLine('order-001', sku, line_qty)
    )


def test_can_allocate_if_available_gt_required():
    batch_lg, line_sm = make_batch_and_line('sku-ikea-chair', 100, 10)
    assert batch_lg.can_allocate(line_sm)


def test_cannot_allocate_if_available_lt_required():
    batch_sm, line_lg = make_batch_and_line('sku-ikea-desk', 20, 100)
    assert batch_sm.can_allocate(line_lg) is False


def test_can_allocate_if_available_eq_required():
    batch_eq, line_eq = make_batch_and_line('sky-ikea-lamp', 100, 100)
    assert batch_eq.can_allocate(line_eq)


def test_cannot_allocate_if_sku_do_not_match():
    batch = Batch('batch-001', 'sku-ikea-table', 100)
    order = OrderLine('order-001', 'sku-ikea-desk', 5)
    assert batch.can_allocate(order) is False


def test_allocating_to_batch_reduces_available():
    batch = Batch("batch-ref-1", "SKU-Product-Table", 20, eta=date.today())
    orderline = OrderLine('order-id', "SKU-Product-Table", 2)
    batch.allocate(orderline)

    assert batch.available == 20-2
