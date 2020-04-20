# Architecture Patterns in Python

by Harry Percival and Bob Gregory

## Chapter 1: Domain Modeling

### Our Business Case

This book follows many examples, but the primary focus of this repo will be the domain model of a furniture retailer.

When buying an article of furniture the system determines how to get goods to the consumer. The coordination of the furniture is done by **allocating** existing stock or planned stock to a customer's order(s).

The current system simply allocates existing stock to a customer's order. Here, we can actually assume the effective inventory is comprised of **existing stock** as well as **inbound stock**, this effectively creates the illusion that the business is out of stock less often.

#### Domain Model

A Domain model represents the design that mental maps the business owners have of their business processes into programmatic code in a clean object oriented form.

When developing a Domain Model, its key to listen to the business owner's jargon and try your best to encode their sentiment and knowledge into the model.

#### Our Domain Model

We have identified the object `OrderLine` which represents an atomic consumer order. An `Orderline` has the following properties: `reference, sku, quantity` which refer to the reference ID of the order, the product being purchased, and the product quantity.

Additionally, the `Batch` object is identifies an atomic collection of stock. The properties of which are `reference, sku, quantity, eta`.

> Functionally, any number of `OrderLine(s)` can be `allocated` to a `Batch` once the `Orderline.SKU` matches the `Batch.SKU` and the total quantity of all `OrderLine(s)` being `allocated` do not exceed the `Batch.Quantity`.

---
