# Critical Rendering Path: What Blocks First Paint
## What
The critical rendering path is the sequence of steps a browser takes to render a webpage. It involves fetching, processing, and rendering resources such as HTML, CSS, and JavaScript. The first paint, also known as the first contentful paint, is when the browser first renders content from the DOM. Understanding what blocks the first paint is essential for optimizing webpage performance.

## Why
Blocking the first paint can lead to a poor user experience, as it delays the time it takes for content to appear on the screen. Common culprits that block the first paint include large JavaScript files, complex CSS layouts, and synchronous resource loading. Identifying and addressing these bottlenecks can significantly improve webpage performance.

## How
To optimize the critical rendering path, developers can use various techniques such as:
* Minimizing and compressing JavaScript and CSS files
* Using asynchronous resource loading
* Prioritizing critical resources
* Avoiding complex CSS layouts and animations
* Leveraging browser caching and caching libraries

## One exercise or command
Use the Chrome DevTools to analyze the critical rendering path of a webpage: 
1. Open Chrome DevTools by pressing F12 or right-clicking on a webpage and selecting "Inspect".
2. Switch to the "Performance" tab.
3. Click on the "Record" button to start recording a performance profile.
4. Reload the webpage to capture the critical rendering path.
5. Stop the recording and analyze the results to identify potential bottlenecks.

## Further reading
* [Google Web Fundamentals: Critical Rendering Path](https://web.dev/critical-rendering-path/)
* [MDN Web Docs: Critical rendering path](https://developer.mozilla.org/en-US/docs/Web/Performance/Critical_rendering_path)
* [Web Performance Optimization Techniques](https://www.w3.org/TR/2017/NOTE-wpo-2017-0306/)
