# Rate Limiting per User vs per IP
## What
Rate limiting is a technique used to control the number of requests a user or IP address can make to a server within a certain time frame. It helps prevent abuse, denial-of-service (DoS) attacks, and improves overall system performance. There are two common approaches to rate limiting: per user and per IP.

## Why
Rate limiting per user is more secure as it prevents a single user from overwhelming the system, even if they are using multiple IP addresses. On the other hand, rate limiting per IP is simpler to implement but can be evaded by users who have access to multiple IP addresses. The choice between the two approaches depends on the specific use case and security requirements.

## How
To implement rate limiting per user, you need to store the request count for each user in a database or cache. When a user makes a request, you increment their request count and check if it exceeds the limit. If it does, you block the request. For rate limiting per IP, you store the request count for each IP address and follow the same process.

## One exercise or command
Try implementing a simple rate limiter using a dictionary to store the request count for each user or IP address. For example, you can use the following Python command to test the rate limiter: `python -c "import requests; for i in range(10): requests.get('https://example.com')"` and observe how the rate limiter responds.

## Further reading
* Techniques for rate limiting: 
  * Token bucket algorithm
  * Leaky bucket algorithm
* Tools for rate limiting: 
  * NGINX rate limiting module
  * AWS API Gateway usage plans
* Best practices for rate limiting: 
  * Monitor and analyze traffic patterns
  * Adjust rate limits based on user behavior
  * Implement IP blocking for abusive IPs

## Senior interview checkpoint

**Prompt:** Explain how to debug p95 latency spikes in a Node API under burst traffic.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
