# Backpressure Between Services
## What
Backpressure between services refers to the resistance or pushback that occurs when a downstream service is unable to handle the volume of requests or data being sent by an upstream service. This can happen in distributed systems where multiple services are interconnected and rely on each other to function properly. Backpressure can lead to increased latency, errors, and even crashes if not managed properly.

## Why
Understanding and managing backpressure is crucial in system design because it can have a significant impact on the overall performance and reliability of the system. When a downstream service is unable to handle the incoming requests, it can lead to a backlog of requests, causing delays and errors. If left unmanaged, backpressure can propagate upstream, causing a ripple effect throughout the system.

## How
To manage backpressure, several strategies can be employed, including:
* Implementing rate limiting to control the volume of requests being sent to a downstream service
* Using queues or buffers to temporarily store requests that cannot be processed immediately
* Implementing retry mechanisms to handle failed requests
* Using load balancing to distribute requests across multiple instances of a service
* Monitoring system metrics to detect early signs of backpressure and take corrective action

## One exercise or command
To simulate backpressure in a system, you can use a command like `siege` to generate a high volume of requests to a service, while monitoring the system's performance using tools like `htop` or `kubectl top`.

## Further reading
* Benefits of using message queues to manage backpressure:
  + Decoupling services to prevent cascading failures
  + Improving system scalability and reliability
  + Allowing for more efficient use of system resources
* Best practices for implementing rate limiting and load balancing:
  + Using algorithms like token bucket or leaky bucket to control request rates
  + Distributing requests across multiple instances of a service to improve responsiveness
  + Monitoring system metrics to detect early signs of backpressure and take corrective action
* Tools and technologies for managing backpressure:
  + Message queues like Apache Kafka or RabbitMQ
  + Load balancing solutions like HAProxy or NGINX
  + Monitoring tools like Prometheus or Grafana

## Senior interview checkpoint

**Prompt:** Explain cache invalidation strategy for hot keys with high write rates.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
