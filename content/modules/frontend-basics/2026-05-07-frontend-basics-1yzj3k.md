# CSS Containment and Layout Thrashing Basics
## What
CSS containment allows developers to define a scope for CSS styles and layout, improving performance by limiting the area that the browser needs to recalculate when changes occur. Layout thrashing, on the other hand, refers to the repeated and expensive process of recalculating layouts when the DOM is modified.

## Why
Understanding CSS containment and layout thrashing is crucial for optimizing the performance of web applications. By using containment, developers can prevent unnecessary layout recalculations and reduce the risk of layout thrashing, resulting in faster and more efficient rendering of web pages.

## How
To use CSS containment, developers can apply the `contain` property to an element, specifying the type of containment (e.g., `layout`, `paint`, or `size`). This tells the browser to isolate the element's layout and styles, reducing the scope of layout recalculations. To avoid layout thrashing, developers can also use techniques such as batching DOM updates, using `requestAnimationFrame`, and minimizing the number of DOM modifications.

## One exercise or command
Try applying the `contain: layout` property to a container element in your HTML, and observe how it affects the performance of your web page when making changes to the DOM.

## Further reading
* The CSS Containment specification: https://www.w3.org/TR/css-contain-1/
* MDN documentation on CSS Containment: https://developer.mozilla.org/en-US/docs/Web/CSS/contain
* Techniques for avoiding layout thrashing: https://developer.mozilla.org/en-US/docs/Web/Performance/Critical_rendering_path/Optimizing_JavaScript#avoid_layout_thrashing

## Senior interview checkpoint

**Prompt:** Explain hydration mismatch root causes and debugging strategy in SSR apps.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
