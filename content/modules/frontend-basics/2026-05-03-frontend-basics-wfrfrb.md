# CSS Containment and Layout Thrashing Basics
## What
CSS containment is a technique used to isolate an element from the rest of the document, improving performance by reducing the scope of layout and paint operations. Layout thrashing occurs when the browser is forced to continuously recalculate the layout of a page due to frequent changes in element sizes or positions.

## Why
Understanding CSS containment and layout thrashing is essential for building high-performance web applications. By containing elements, developers can prevent layout thrashing, reduce the time spent on layout and paint operations, and improve the overall user experience.

## How
To apply CSS containment, developers can use the `contain` property, which can have one of the following values: `none`, `layout`, `paint`, `size`, or `strict`. The `layout` value, for example, isolates the element's layout from the rest of the document, while `paint` isolates the element's paint operations.

## One exercise or command
Try adding the following CSS rule to an element that is being frequently updated: `contain: layout;` and measure the performance improvement using the browser's DevTools.

## Further reading
* [MDN Web Docs: CSS Containment](https://developer.mozilla.org/en-US/docs/Web/CSS/contain)
* [Web Fundamentals: Avoiding layout thrashing](https://web.dev/avoiding-layout-thrashing/)
* [CSS-Tricks: CSS Containment](https://css-tricks.com/css-containment/)
* [W3C: CSS Containment Module Level 1](https://www.w3.org/TR/css-contain-1/)
