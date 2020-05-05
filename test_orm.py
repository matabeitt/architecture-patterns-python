import pytest
import model


def test_orderline_mapper_can_load_lines(session):
    session.execute(
        'INSERT INTO order_lines (order_id, sku, quantity) VALUES '
        '("order1", "RED-CHAIR", 12),'
        '("order1", "RED-TABLE", 13),'
        '("order2", "BLUE-LIPSTICK", 14)'
    )
    expected = [
        model.OrderLine("order1", "RED-CHAIR", 12),
        model.OrderLine("order1", "RED-TABLE", 13),
        model.OrderLine("order2", "BLUE-LIPSTICK", 14),
    ]
    assert session.query(model.OrderLine).all() == expected


def test_orderline_mapper_can_save_lines(session):
    orderline = model.OrderLine("order1", "DECORATIVE-WIDGET", 12)
    session.add(orderline)
    session.commit()

    rows = list(
        session.execute(
            'SELECT order_id, sku, quantity FROM "order_lines"'
        )
    )
    assert rows == [("order1", "DECORATIVE-WIDGET", 12)]
