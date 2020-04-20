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


def test_allocating_to_batch_reduces_available():
    batch = Batch("batch-ref-1", "SKU-Product-Table", 20, eta=date.today())
    orderline = OrderLine('order-id', "SKU-Product-Table", 2)
    batch.allocate(orderline)

    assert batch.available == 20-2
