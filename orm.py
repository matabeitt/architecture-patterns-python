from sqlalchemy import (
    Table, MetaData, Column,
    Integer, String, Date,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship
import model

metadata = MetaData()

order_lines = Table(
    'order_lines',
    metadata,
    Column('id', Integer, primary_key=True, auto_increment=True),
    Column('sku', String(255)),
    Column('quantity', Integer, nullable=False),
    Column('order_id', String(255))
)


def start_mappers():
    order_lines_mapper = mapper(model.OrderLine, order_lines)
