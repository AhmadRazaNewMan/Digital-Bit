# Critical Rendering Path: What Blocks First Paint
## What
The critical rendering path refers to the sequence of steps that a browser takes to render a webpage. It involves the browser parsing HTML, CSS, and JavaScript files, and using the parsed data to construct the DOM and CSSOM trees, which are then used to compute the layout and paint the pixels on the screen. The first paint, also known as the first contentful paint, is the moment when the browser first renders any content from the DOM.

## Why
Understanding the critical rendering path is crucial for optimizing the performance of web applications. A slow or blocked critical rendering path can result in a delayed first paint, leading to a poor user experience. Common blockers of the first paint include large JavaScript files, complex CSS styles, and slow server responses.

## How
To optimize the critical rendering path and minimize blockers of the first paint, developers can take several steps:
* Minimize the amount of JavaScript that needs to be parsed and executed before the first paint
* Use efficient CSS styles and avoid complex selectors
* Optimize server response times and ensure that the HTML document is delivered quickly
* Use techniques such as code splitting and lazy loading to reduce the amount of data that needs to be transferred and parsed

## One exercise or command
Try running the command `lighthouse https://example.com` in your terminal to analyze the performance of a webpage and identify potential blockers of the first paint.

## Further reading
* https://web.dev/critical-rendering-path
* https://web.dev/first-contentful-paint
* https://developer.mozilla.org/en-US/docs/Web/Performance/Critical_rendering_path
* https://web.dev/optimize-css
* https://web.dev/code-splitting 
* Books on web performance optimization
