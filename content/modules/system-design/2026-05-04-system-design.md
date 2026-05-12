# Backpressure Between Services
## What
Backpressure between services refers to the resistance or pushback that occurs when a downstream service is unable to handle the volume of requests or data being sent by an upstream service. This can happen in distributed systems where multiple services are interconnected and reliant on each other to function.

## Why
Backpressure is a critical consideration in system design because it can lead to cascading failures, where the inability of one service to handle requests causes a ripple effect throughout the system. Understanding and managing backpressure is essential to ensure the reliability, scalability, and performance of distributed systems.

## How
To manage backpressure, services can implement various strategies such as:
* **Rate limiting**: limiting the number of requests that can be sent to a downstream service within a given time frame
* **Load shedding**: randomly dropping requests when the downstream service is overwhelmed
* **Queueing**: buffering requests in a queue until the downstream service is able to process them
* **Circuit breakers**: detecting when a downstream service is not responding and preventing further requests from being sent

## One exercise or command
To simulate backpressure in a system, you can use a tool like `apache-jmeter` to generate a large volume of requests to a downstream service, while monitoring the performance of the upstream service using a command like: `jmeter -n -t test.jmx -l results.jtl`

## Further reading
* **System design patterns**: to learn more about strategies for managing backpressure, such as the **Bulkhead** pattern, which isolates components to prevent cascading failures
* **Distributed system principles**: to understand the fundamentals of distributed systems and how backpressure can impact system design
* **Service mesh architectures**: to explore how service meshes can help manage backpressure and improve the reliability of distributed systems
* **Queueing theory**: to dive deeper into the mathematical models that underlie queueing systems and understand how to optimize queueing strategies for managing backpressure

## Senior interview checkpoint

**Prompt:** Design a rate limiter that supports both global and per-user quotas.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
