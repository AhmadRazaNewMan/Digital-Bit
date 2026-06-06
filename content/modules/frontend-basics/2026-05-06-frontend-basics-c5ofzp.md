# Understanding Critical Rendering Path
## What
The critical rendering path refers to the sequence of steps that the browser takes to render a website, from receiving the HTML to displaying the first paint. This process involves parsing HTML, loading CSS and JavaScript files, and executing scripts. The critical rendering path is crucial for ensuring a good user experience, as it directly affects the page's load time and responsiveness.

## Why
Understanding the critical rendering path is essential for optimizing website performance. By identifying the bottlenecks in the rendering process, developers can make informed decisions about how to improve page load times, reduce latency, and enhance overall user experience. A slow critical rendering path can lead to a poor user experience, increased bounce rates, and lower search engine rankings.

## How
The critical rendering path involves the following steps:
* The browser receives the HTML document and starts parsing it
* The browser encounters a CSS file and loads it, as CSS is required for rendering
* The browser encounters a JavaScript file and loads it, but may execute it after the CSS has been loaded
* The browser executes the JavaScript code and updates the DOM
* The browser renders the page and displays the first paint

## One exercise or command
To analyze the critical rendering path of a website, you can use the Chrome DevTools. Open the Chrome DevTools, switch to the Network tab, and reload the page. Then, switch to the Performance tab and click on the "Reload" button to record the page load. The resulting waterfall chart will show the critical rendering path and help you identify potential bottlenecks.

## Further reading
* Google Web Fundamentals: [Critical Rendering Path](https://web.dev/critical-rendering-path/)
* MDN Web Docs: [Critical rendering path](https://developer.mozilla.org/en-US/docs/Web/Performance/Critical_rendering_path)
* Chrome DevTools: [Analyzing the Critical Rendering Path](https://developer.chrome.com/docs/devtools/evaluate-performance/#critical-rendering-path)

## Senior interview checkpoint

**Prompt:** Explain hydration mismatch root causes and debugging strategy in SSR apps.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
