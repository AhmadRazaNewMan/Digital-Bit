# Critical Rendering Path: What Blocks First Paint
## What
The critical rendering path refers to the sequence of steps a browser takes to render a web page. It involves fetching and processing the HTML, CSS, and JavaScript files, as well as rendering the initial viewport. The first paint, also known as the first contentful paint, is when the browser first renders any content from the DOM.

## Why
Understanding what blocks the first paint is crucial for optimizing the performance of a web page. A slow first paint can lead to a poor user experience, increased bounce rates, and lower search engine rankings. Common blockers of the first paint include large JavaScript files, complex CSS selectors, and slow server response times.

## How
To identify what blocks the first paint, developers can use the browser's DevTools to analyze the critical rendering path. This involves:
* Inspecting the HTML and CSS files to ensure they are optimized and minified
* Analyzing the JavaScript files to identify any bottlenecks or slow-executing code
* Checking the server response times to ensure they are within an acceptable range
* Optimizing images and other media to reduce their file size and improve load times

## One exercise or command
Use the `performance` tab in Chrome DevTools to analyze the critical rendering path and identify any blockers of the first paint. Run the command `performance.getEntries()` in the console to retrieve a list of performance entries, including the time it took for the first paint to occur.

## Further reading
* Learn about the [critical rendering path](https://web.dev/critical-rendering-path/) and how to optimize it
* Discover how to [improve the performance](https://web.dev/fast/) of your web pages
* Read about [web performance optimization](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency) best practices
* Explore the [browser's DevTools](https://developer.chrome.com/docs/devtools/) and learn how to use them to analyze and optimize your web pages

## Senior interview checkpoint

**Prompt:** Explain hydration mismatch root causes and debugging strategy in SSR apps.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
