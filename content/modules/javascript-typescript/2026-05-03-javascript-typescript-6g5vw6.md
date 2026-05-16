# Async Cancellation with AbortController
## What
The AbortController is an API in JavaScript that allows you to abort ongoing asynchronous operations, such as fetch requests or timeouts. It provides a way to cancel these operations when they are no longer needed, which can help improve the performance and responsiveness of your application.

## Why
Using AbortController is essential in scenarios where you need to cancel ongoing requests, such as when a user navigates away from a page or closes a tab. This helps prevent unnecessary work from being done on the server and reduces the load on your application.

## How
To use AbortController, you create an instance of the controller and pass its signal to the asynchronous operation. When you want to cancel the operation, you call the abort method on the controller. The signal is then set to aborted, and the operation is cancelled.

## One exercise or command
Try the following example:
```javascript
const controller = new AbortController();
const signal = controller.signal;

// Simulate a fetch request
fetch('https://example.com', { signal })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));

// Cancel the request after 1 second
setTimeout(() => {
  controller.abort();
}, 1000);
```

## Further reading
* The AbortController API: https://developer.mozilla.org/en-US/docs/Web/API/AbortController
* Using AbortController with fetch: https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch#parameters
* Best practices for using AbortController: https://web.dev/abortable-fetch 
* AbortController support in browsers: https://caniuse.com/abortcontroller 
* AbortController polyfill for older browsers: https://github.com/moznion/abortcontroller-polyfill

## Senior interview checkpoint

**Prompt:** Design cancellation-safe async flow with AbortController for chained requests.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
