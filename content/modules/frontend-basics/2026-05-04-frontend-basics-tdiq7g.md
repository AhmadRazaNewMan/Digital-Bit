# Semantic Landmark Regions and Heading Outline
## What
Semantic landmark regions and heading outlines are essential components of accessible web development. Semantic landmark regions refer to the use of HTML elements to define the structure and organization of a webpage, such as headers, footers, and navigation menus. A heading outline, on the other hand, is a hierarchical representation of the headings on a webpage, which helps screen readers and other assistive technologies to understand the page's content and structure.

## Why
The use of semantic landmark regions and heading outlines is crucial for several reasons. Firstly, it improves the accessibility of a webpage, making it easier for users with disabilities to navigate and understand the content. Secondly, it enhances the overall user experience by providing a clear and consistent structure to the webpage. Finally, it also benefits search engine optimization (SEO) by helping search engines to better understand the page's content and structure.

## How
To implement semantic landmark regions and heading outlines, developers can use HTML elements such as `header`, `footer`, `nav`, `main`, and `section` to define the structure of the webpage. They can also use the `h1` to `h6` elements to create a hierarchical heading outline. It is essential to ensure that the heading outline is logical and consistent, with each heading level representing a subheading of the previous one.

## One exercise or command
To test the accessibility of a webpage, you can use the WAVE Web Accessibility Evaluation Tool or the Lighthouse extension in Chrome DevTools. Run the command `npm install -g lighthouse` to install Lighthouse globally, then run `lighthouse <url>` to audit the webpage's accessibility.

## Further reading
* W3C Web Accessibility Initiative (WAI) guidelines
* HTML5 semantic elements documentation
* A11y project resources and tutorials
* WebAIM articles on web accessibility and heading outlines
* Mozilla Developer Network (MDN) documentation on HTML structure and accessibility

## Senior interview checkpoint

**Prompt:** Explain hydration mismatch root causes and debugging strategy in SSR apps.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
