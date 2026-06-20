# Responsive Typography with clamp()
## What
Responsive typography is an essential aspect of web design, ensuring that text is readable and visually appealing across various devices and screen sizes. The `clamp()` function is a CSS property that allows developers to define a minimum, preferred, and maximum value for a font size, enabling responsive typography.

## Why
Using `clamp()` for responsive typography provides several benefits, including:
* Improved readability on different devices and screen sizes
* Enhanced user experience through consistent and adaptable font sizes
* Simplified CSS code, reducing the need for complex media queries

## How
The `clamp()` function takes three values: a minimum size, a preferred size, and a maximum size. The syntax is as follows: `font-size: clamp(min, pref, max)`. For example, `font-size: clamp(1rem, 2.5vw, 2rem)` sets the font size to at least 1rem, preferably 2.5vw (2.5% of the viewport width), and at most 2rem.

## One exercise or command
Try setting a responsive font size for a heading element using `clamp()`: `h1 { font-size: clamp(1.5rem, 4vw, 3rem); }`

## Further reading
* CSS-Tricks: [A Complete Guide to CSS Clamp](https://css-tricks.com/a-complete-guide-to-css-clamp/)
* MDN Web Docs: [clamp()](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp)
* Smashing Magazine: [Responsive Typography: Using Clamp For Better Font Sizing](https://www.smashingmagazine.com/2020/07/responsive-typography-clamp-font-sizing/)

## Senior interview checkpoint

**Prompt:** Audit a page for accessibility regressions after a redesign; list highest-risk fixes first.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
