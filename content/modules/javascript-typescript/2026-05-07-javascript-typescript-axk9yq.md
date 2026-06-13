# Async Cancellation with AbortController
## What
The AbortController is an API that allows you to cancel asynchronous operations, such as fetching data from a server or reading a file. It provides a way to signal that an operation should be cancelled, and allows the operation to react to this signal.

## Why
Async cancellation is useful in a variety of scenarios, such as when a user navigates away from a page that is still loading data, or when an operation is taking too long and needs to be timed out. The AbortController provides a standard way to handle these scenarios, making it easier to write robust and responsive asynchronous code.

## How
To use the AbortController, you create a new instance of the controller and pass its signal to the asynchronous operation. The operation can then listen for the abort signal and cancel itself when it is received. Here is a basic example of how to use the AbortController:
* Create a new AbortController instance
* Pass the controller's signal to the asynchronous operation
* Use the controller's abort method to signal that the operation should be cancelled

## One exercise or command
Try using the AbortController to cancel a fetch operation:
```javascript
const controller = new AbortController();
fetch('https://example.com/data', { signal: controller.signal })
  .then(response => response.json())
  .catch(error => console.error(error));
controller.abort();
```

## Further reading
* [MDN Documentation: AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)
* [MDN Documentation: AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)
* [MDN Documentation: Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

## Senior interview checkpoint

**Prompt:** Design cancellation-safe async flow with AbortController for chained requests.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
