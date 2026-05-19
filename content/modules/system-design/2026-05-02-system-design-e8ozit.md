# CQRS — read vs write scaling tradeoffs
## What
CQRS (Command Query Responsibility Segregation) is an architectural pattern that separates the responsibilities of handling commands (writes) and queries (reads) in a system. This separation allows for independent scaling of read and write operations, which is crucial in systems with high traffic or large amounts of data.

## Why
The main reason to use CQRS is to improve the scalability and performance of a system. By separating reads and writes, you can optimize each path independently, using different data models, databases, or even caching strategies. This separation also simplifies the development process, as each team can focus on either the command or query side without interfering with the other.

## How
To implement CQRS, you need to divide your system into two main components: the command side and the query side. The command side handles all write operations, such as creating, updating, or deleting data. The query side handles all read operations, such as retrieving data. You can use different databases or data storage systems for each side, and even use event sourcing to store the history of all changes made to the data.

## One exercise or command
Try to design a simple e-commerce system using CQRS. Define the commands for creating, updating, and deleting products, as well as the queries for retrieving product information. Consider using a relational database for the command side and a NoSQL database for the query side.

## Further reading
* Benefits of using CQRS in microservices architecture
* CQRS pattern in Azure
* Implementing CQRS with event sourcing
* Scaling CQRS systems with caching and load balancing
* Using CQRS in real-time analytics systems

## Senior interview checkpoint

**Prompt:** Explain cache invalidation strategy for hot keys with high write rates.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
