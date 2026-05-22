# Rate Limiting: Per User vs Per IP
## What
Rate limiting is a technique used to control the number of requests a user or IP address can send to a server within a certain time frame. This is done to prevent abuse, denial-of-service attacks, and to ensure fair usage of resources. There are two common approaches: rate limiting per user and rate limiting per IP.

## Why
Rate limiting per user is more secure and targeted, as it restricts the number of requests from a specific user account, regardless of the IP address used. On the other hand, rate limiting per IP is simpler to implement but may lead to false positives, where a single IP address is shared by multiple users, and all are restricted due to the actions of one. The choice between the two depends on the specific requirements of the application and the trade-off between security and complexity.

## How
To implement rate limiting per user, a backend system would need to track user authentication and associate each request with a user ID. For rate limiting per IP, the system would need to track the IP address of each incoming request. In both cases, a counter or timer would be used to enforce the rate limit, and excess requests would be blocked or throttled.

## One exercise or command
To test rate limiting, you can use tools like `curl` to simulate multiple requests from the same IP or user, and observe how the server responds. For example: 
`curl -X GET http://example.com/api/endpoint -H "Authorization: Bearer user_token"`

## Further reading
* Key differences between rate limiting per user and per IP
* Implementing rate limiting using Redis or Memcached as a counter store
* Best practices for setting rate limit thresholds and response codes
* Using rate limiting to prevent brute-force attacks on authentication endpoints
* Comparison of rate limiting algorithms, such as token bucket and leaky bucket

## Senior interview checkpoint

**Prompt:** Design idempotent retry handling for a payment callback endpoint.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
