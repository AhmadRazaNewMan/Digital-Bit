# Responsive Typography with clamp()
## What
Responsive typography is an essential aspect of web design, as it ensures that text is readable and visually appealing across various devices and screen sizes. The `clamp()` function is a CSS property that allows developers to define a minimum, maximum, and optimal font size, making it easier to manage responsive typography.

## Why
Using `clamp()` for responsive typography provides several benefits, including:
* Improved user experience: text is always readable and well-proportioned
* Simplified styling: `clamp()` reduces the need for multiple media queries
* Enhanced accessibility: text can be easily scaled up or down for users with visual impairments

## How
The `clamp()` function takes three values: a minimum font size, an optimal font size, and a maximum font size. The syntax is `font-size: clamp(min, opt, max)`. For example: `font-size: clamp(1rem, 2.5vw, 2rem)`. This means the font size will be at least 1rem, ideally 2.5vw (2.5% of the viewport width), and at most 2rem.

## One exercise or command
Try using `clamp()` in your CSS to create a responsive heading: `h1 { font-size: clamp(1.5rem, 5vw, 3rem); }`. Observe how the font size changes as you resize the browser window.

## Further reading
* CSS-Tricks: [A Complete Guide to CSS Clamp](https://css-tricks.com/complete-guide-to-css-clamp/)
* Mozilla Developer Network: [clamp()](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp)
* Smashing Magazine: [Responsive Typography: Using Clamp To Set Perfectly Scaled Headings](https://www.smashingmagazine.com/2020/05/responsive-typography-clamp/)

## Senior interview checkpoint

**Prompt:** Explain hydration mismatch root causes and debugging strategy in SSR apps.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
