# CSS Containment and Layout Thrashing Basics
## What
CSS containment and layout thrashing are crucial concepts in frontend development that affect the performance and efficiency of web pages. Containment refers to the ability to isolate a part of the DOM, preventing it from affecting the rest of the page. Layout thrashing occurs when the browser is forced to recalculate the layout of a page repeatedly, leading to performance issues.

## Why
Understanding CSS containment and layout thrashing is essential for optimizing the performance of complex web applications. By containing parts of the DOM, developers can prevent unnecessary layout recalculations and reduce the risk of layout thrashing. This, in turn, improves the overall user experience by reducing lag, jitter, and other performance-related issues.

## How
To implement CSS containment, developers can use the `contain` property, which allows them to specify the types of containment they want to apply to an element. For example, `contain: layout` isolates the element's layout from the rest of the page, while `contain: paint` isolates the element's painting. To avoid layout thrashing, developers can use techniques such as using `transform` instead of `top` and `left` properties, and avoiding frequent changes to an element's width and height.

## One exercise or command
Try adding the `contain: layout` property to a complex component in your web application and observe the performance improvements. You can use the Chrome DevTools to profile the page and measure the impact of containment on performance.

## Further reading
* The CSS Containment specification: https://www.w3.org/TR/css-contain-1/
* Layout Thrashing and How to Avoid it: https://www.youtube.com/watch?v=zH_3ZCIyiL4
* CSS Containment and Layout Thrashing: https://developer.mozilla.org/en-US/docs/Web/CSS/contain
* Optimizing Performance with CSS Containment: https://web.dev/optimize-css-containment/
