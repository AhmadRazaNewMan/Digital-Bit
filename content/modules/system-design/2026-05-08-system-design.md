# Idempotency Keys for Payments and Retries
## What
Idempotency keys are unique identifiers used to ensure that an operation, such as a payment, is only processed once. This is particularly important in distributed systems where retries may occur due to network failures or other issues.

## Why
Idempotency keys are necessary to prevent duplicate payments or other unintended consequences of retries. Without idempotency keys, a system may process the same payment multiple times, leading to financial losses and other problems.

## How
To implement idempotency keys, a system can use a unique identifier for each payment request. This identifier is included in the request and stored in a database or other storage system. When a retry occurs, the system checks the identifier to determine if the payment has already been processed. If it has, the system can return a success response without processing the payment again.

## One exercise or command
Try designing a payment system that uses idempotency keys to handle retries. Consider the following command: `curl -X POST -H "Idempotency-Key: $ID" -d "amount=$AMOUNT&currency=$CURRENCY" https://example.com/payments`

## Further reading
* Use cases for idempotency keys in payment systems:
  + Preventing duplicate charges
  + Handling network failures and retries
  + Ensuring consistency in distributed systems
* Best practices for implementing idempotency keys:
  + Using unique and random identifiers
  + Storing identifiers in a database or other storage system
  + Checking identifiers before processing payments
* Relevant technologies and tools:
  + Payment gateways and APIs
  + Distributed databases and storage systems
  + Networking and retry mechanisms

## Senior interview checkpoint

**Prompt:** Design a rate limiter that supports both global and per-user quotas.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
