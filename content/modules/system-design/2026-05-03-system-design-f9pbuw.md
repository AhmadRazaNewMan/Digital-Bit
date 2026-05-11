# Idempotency Keys for Payments and Retries
## What
Idempotency keys are unique identifiers used to prevent duplicate operations, particularly in payment systems. They ensure that even if a request is retried multiple times, the operation is only performed once. This is crucial for preventing unintended charges or actions.

## Why
Idempotency keys are essential for managing retries in payment systems, as network failures or timeouts can lead to repeated requests. Without idempotency keys, these repeated requests could result in multiple charges or incorrect updates, causing financial losses or data inconsistencies.

## How
To implement idempotency keys, a unique identifier is generated for each payment request. This identifier is then passed with the request to the payment processor. If the request is retried, the same identifier is used. The payment processor checks the identifier to determine if the operation has already been performed. If it has, the processor returns a success response without performing the operation again.

## One exercise or command
Try designing a simple payment system that incorporates idempotency keys. Consider the following command: `curl -X POST https://example.com/pay -H "Idempotency-Key: $UNIQUE_ID" -d "amount=10&currency=USD"`. How would you handle retries and duplicate requests in this system?

## Further reading
* Designing idempotent APIs for payment processing
* Best practices for implementing idempotency keys
* Handling retries and timeouts in distributed systems
* Payment Card Industry Data Security Standard (PCI-DSS) guidelines for idempotency and retries
* Case studies of companies that have successfully implemented idempotency keys for payments and retries

## Senior interview checkpoint

**Prompt:** Explain cache invalidation strategy for hot keys with high write rates.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
