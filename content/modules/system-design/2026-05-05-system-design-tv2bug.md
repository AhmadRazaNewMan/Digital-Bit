# Backpressure Between Services
## What
Backpressure between services refers to the resistance or pushback that occurs when a downstream service is unable to handle the volume of requests or data being sent by an upstream service. This can happen in distributed systems, microservices architecture, or any system where multiple services are interconnected and dependent on each other. Backpressure can lead to increased latency, errors, and even crashes if not managed properly.

## Why
Understanding and managing backpressure is crucial for maintaining the stability and performance of a system. When a downstream service is overwhelmed, it can lead to a cascade of failures throughout the system, causing significant disruption to users. By recognizing the signs of backpressure and implementing strategies to mitigate it, developers can ensure their system remains resilient and responsive under various loads and conditions.

## How
To manage backpressure, developers can implement several strategies, including:
* Load shedding: intentionally dropping or delaying non-essential requests to prevent overwhelming the downstream service
* Rate limiting: restricting the number of requests that can be sent to the downstream service within a given time frame
* Caching: storing frequently accessed data in memory to reduce the load on the downstream service
* Bulkheading: isolating components or services to prevent failures from spreading and to maintain overall system stability
* Implementing queues or buffers to handle excessive requests and process them when the downstream service is ready

## One exercise or command
Try running a simple simulation using `apache-kafka` or `rabbitmq` to demonstrate how backpressure can occur in a message queue system. Use a producer to send messages at a high rate and a consumer that processes messages at a slower rate, observing how the queue grows and how the system responds to the backpressure.

## Further reading
* Key concepts in system design: scalability, availability, and fault tolerance
* Understanding message queues and their role in managing backpressure
* Strategies for load shedding and rate limiting in distributed systems
* Implementing bulkheading and caching in microservices architecture
* Best practices for monitoring and responding to backpressure in production environments

## Senior interview checkpoint

**Prompt:** Explain cache invalidation strategy for hot keys with high write rates.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
