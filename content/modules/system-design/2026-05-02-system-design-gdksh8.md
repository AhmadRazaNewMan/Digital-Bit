# Idempotency Keys for Payments and Retries
## What
Idempotency keys are unique identifiers used to prevent duplicate payments or operations in a system. They ensure that even if a request is retried multiple times, the outcome remains the same. This is especially crucial in payment processing systems where duplicate transactions can lead to financial losses.

## Why
Idempotency is necessary for maintaining data consistency and preventing errors in distributed systems. Without idempotency keys, a system may process the same payment multiple times, resulting in incorrect balances or overcharging customers. Idempotency keys provide a way to identify and prevent such duplicate operations.

## How
To implement idempotency keys, a system generates a unique identifier for each payment or operation. This identifier is sent with the request and stored on the server-side. If a retry is attempted, the system checks the idempotency key to determine if the operation has already been processed. If it has, the system returns the original result without re-processing the request.

## One exercise or command
Try designing a payment processing system that uses idempotency keys to prevent duplicate transactions. Consider the following:
* How will you generate unique idempotency keys?
* How will you store and manage these keys on the server-side?
* What happens if a retry is attempted with an invalid or missing idempotency key?

## Further reading
* Key concepts in idempotency and retry mechanisms:
  * Unique identifier generation
  * Server-side storage and management
  * Error handling and retry strategies
* Relevant technologies and protocols:
  * HTTP idempotent methods (e.g., GET, PUT, DELETE)
  * Payment processing APIs and gateways (e.g., Stripe, PayPal)
  * Distributed system design patterns and principles

## Senior interview checkpoint

**Prompt:** Design a rate limiter that supports both global and per-user quotas.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
