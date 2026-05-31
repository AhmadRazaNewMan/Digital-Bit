# Critical Rendering Path: What Blocks First Paint
## What
The critical rendering path refers to the sequence of steps that a web browser takes to render a webpage. It involves the browser parsing HTML, CSS, and JavaScript files, and then using this information to paint the webpage on the screen. The critical rendering path is crucial for ensuring a good user experience, as it determines how quickly a webpage can be displayed to the user.

## Why
Understanding the critical rendering path is important because it helps developers optimize the performance of their webpages. By minimizing the time it takes for the browser to render a webpage, developers can improve the user experience and increase engagement. Several factors can block the first paint, including large JavaScript files, complex CSS selectors, and slow server response times.

## How
To optimize the critical rendering path, developers can take several steps. These include minimizing the amount of JavaScript code, using efficient CSS selectors, and optimizing images. Developers can also use techniques such as code splitting and lazy loading to reduce the amount of code that needs to be parsed and executed. Additionally, using a content delivery network (CDN) can help reduce the time it takes for the browser to receive the necessary files.

## One exercise or command
Use the Chrome DevTools to analyze the critical rendering path of a webpage. Open the Chrome DevTools, switch to the "Performance" tab, and click on the "Record" button. Then, reload the webpage and examine the waterfall chart to see which resources are blocking the first paint.

## Further reading
* Learn about the critical rendering path and how to optimize it on [Web Fundamentals](https://web.dev/critical-rendering-path/)
* Understand how to use Chrome DevTools to analyze the critical rendering path on the [Chrome DevTools website](https://developer.chrome.com/docs/devtools/)
* Discover techniques for optimizing the critical rendering path, such as code splitting and lazy loading, on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/Performance/Optimizing_content_efficiency)

## Senior interview checkpoint

**Prompt:** Audit a page for accessibility regressions after a redesign; list highest-risk fixes first.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
