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

## Chapter 2: Repository Pattern

A key focus in designing this system with OOP in mind is the Dependency inversion principle (DIP) of SOLID design considerations.

Specifically, we will look into an abstraction over the data storage module of the system, and ensure that it upholds to the requirements of SOLID and specifically: DIP.

> **Persisting the Domain Model**
> If we need to run tests on our system that uses a database and API, it becomes much harder to write and maintain. Undoubtedly we will need some sort of persistent storage in a production environment.

### Requirements: Defining the API

What we mean here is the API endpoint for example, `/allocate` which handles adding the `OrderLine` object attributes as `HTTP` parameters in order to construct an Object and `allocate()` it to our storage module.

> **Flask** was chosen because it is lightweight, but you may optionally use **Django**.

### Data Access & DIP

We will visualise our domain model as being "inside" and the dependencies flow inward toward it.

> We want to ensure our **Domain model** has no dependencies whatsoever. _If the infrastructure concerns are in the Domain, then testing becomes slower_

### Domain Model & ORM

#### Declarative ORM

Typically, in Django or SQLAlchemy, you define your model as a structure that is composed of ORM specific objects: `id: Column(Integer, primary_key=true)`, but as you can see, with this method, your model becomes directly coupled with the ORM and becomes inextensible. 

> This is the standard or "out of the box" implementation of using ORM with Domain Models in Django or SQLAlchemy.

#### ORM & DIP

We may optionally invert the dependency of the Model and ORM, i.e. the ORM will depend on the Model. This is done by creating ORM Objects and mapping them to a Domain model object using the `sqlalchemy.orm.mapper` module.

### Repository Pattern

In a development environment, we can use local memory to store objects that we wish to display. In a production environment, we require the use of an external database - one that needs to be explicitly `commit` to. The **Repository Pattern** allows us to abstract the limitations of the database as if it were our local filesystem.

#### The Abstract Repository

The simplest repository only uses `add()` and `get()`. This simplicity also prevents us from coupling the domain to the storage implementation.

#### Trade Offs

1. Every time we expact our Domain model, the Repository also requires additional logic.
2. Additional cost in maintenance, and execution.

#### Testing the Repository

A `FakeRepository` could be used as a wrapper around a `set(...[Batch])`, allowing us to test and reason easily.

### Port versus Adapter

**Port** is the interface between one module and the module being abstracted.

**Adapter** is the implementation of a *Port*

> e.g `AbstractRepository` is a port, while `FakeRepository` is an adapter.

---